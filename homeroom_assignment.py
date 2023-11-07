import pulp
import pandas as pd
#pulp.LpProbrem(任意の名前, 解く問題の種類)
prob = pulp.LpProblem('HomeroomAssignmentProblem', pulp.LpMaximize)

#データの読み込み
s_df = pd.read_csv('students.csv')
#日付のリスト
D = [0,1,2,3,4,5,6,7]

#タスクのリスト
T = ['A', 'B', 'C', 'D']
t_unit = [3 ,4 ,5 ,6 ]
pair_taskunit_day = []

#生徒とクラスのペアリスト
SC = [(s,c) for s in S for c in C]
print(SC)

'''

x = pulp.LpVariable('x', cat= 'Continuous')
y = pulp.LpVariable('y', cat= 'Continuous')

#制約条件 probrem に 「+=」をつけて条件式を書く
problem += 1*x + 3*y <= 30
problem += 2*x + 1*y <= 40
problem += x >= 0
problem += y >= 0

#目的関数 「==」、「>=」などがない、ただの関数
problem += x + 2*y

#problem.solve 問題を解いて、statusコードを返す
status = problem.solve()


print('Status:', pulp.LpStatus[status])
#問題を解いてあとは、x.value()のように、値を参照できる
print('x=', x.value(), 'y=', y.value(), 'obj=', problem.objective.value())

'''