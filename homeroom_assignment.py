import pulp
import pandas as pd
#pulp.LpProbrem(任意の名前, 解く問題の種類)
problem = pulp.LpProblem('HomeroomAssignmentProblem', pulp.LpMaximize)

#データの読み込み
s_df = pd.read_csv('students.csv')
s_pair_df = pd.read_csv('students_pairs.csv')

#生徒のリスト
S = s_df['student_id'].tolist()

#クラスのリスト
C = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

#生徒とクラスのペアリスト
SC = [(s, c) for s in S for c in C]

#男子生徒のリスト
S_male = [row.student_id for row in s_df.itertuples() if row.gender == 1]
#女子生徒のリスト
S_female = [row.student_id for row in s_df.itertuples() if row.gender == 0]

#学力を辞書表現に変換
score = {row.student_id:row.score for row in s_df.itertuples()}

#平均点の算出
score_mean = s_df['score'].mean()

#リーダー気質の生徒の集合
S_leader = [row.student_id for row in s_df.itertuples() if row.leader_flag == 1]

#特別な支援が必要な生徒の集合
S_support = [row.student_id for row in s_df.itertuples() if row.support_flag == 1]

#生徒の特定ペアリスト
SS = [(row.student_id1, row.student_id2) for row in s_pair_df.itertuples()]


#生徒をどこのクラスに割り当てられるか変数として定義
x = pulp.LpVariable.dicts('x', SC, cat='Binary')




#制約条件
#(1)各生徒はクラスに割り当てる
for s in S:
    problem += pulp.lpSum([x[s,c] for c in C]) == 1

#(2)各クラスの人数は39人以上40人以下とする
for c in C:
    problem += pulp.lpSum([x[s,c] for s in S]) >= 39
    problem += pulp.lpSum([x[s,c] for s in S]) <= 40

#(3)各クラスの男子生徒、女子生徒の人数は20人以下とする
for c in C:
    problem += pulp.lpSum([x[s,c] for s in S_male]) <= 20
    problem += pulp.lpSum([x[s,c] for s in S_female]) <= 20

#(4)各クラスの学力の平均点は学年平均点±10点とする
for c in C:
    problem += (score_mean - 10) * pulp.lpSum([x[s,c] for s in S]) <= pulp.lpSum([x[s,c] * score[s] for s in S])
    problem += pulp.lpSum([x[s,c] * score[s] for s in S]) <= (score_mean + 10) * pulp.lpSum([x[s,c] for s in S])

#(5)各クラスにリーダー気質の生徒を2人以上割り当てる
for c in C:
    problem += pulp.lpSum([x[s,c] for s in S_leader]) >= 2

#(6)特別な支援が必要な生徒は各クラスに1人以下とする
for c in C:
    problem += pulp.lpSum([x[s,c] for s in S_support]) <= 1

#(7)特定ペアの生徒が同一クラスに割り当てない
for s1, s2 in SS:
    for c in C:
        problem += x[s1,c] + x[s2,c] <= 1



#problem.solve 問題を解いて、statusコードを返す
status = problem.solve()

print(status)
print(pulp.LpStatus[status])
