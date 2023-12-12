import pulp
import pandas as pd
import datetime
problem = pulp.LpProblem('Date_Task_scheduling',pulp.LpMaximize)

#関数の定義
#タプルに変換する
def convert_int_to_tuple(A):
    return tuple([A])

#タプルのマージ
def merge_to_tuple(A,B):
    return A+B

#隣合った時間かどうかを返す
def is_adjacent(a,b):
    if (abs(a - b) == 1):
        return True
    else:
        return False

#データの作成
#既に決まっているスケジュールのリスト
schedule_list = [['学校',7,15],['就寝,朝',0,7],['風呂,夕食',19,20],['就寝,夜',23,24]]

#タスクのリスト [タスク名,所要時間]
Task_list = [['task1',2],['task2',3]]

#空き時間のリスト
Freetime_list = [i for i in range(0,24)]


#タスクユニット+辞書作成
#タスクユニット [タスクのインデックス,ユニットの通し番号]
#辞書 {タスクのインデックス:タスク名}
Task_unit_list = []
task_serial_num = 0
task_dictionary = {}
for task in Task_list:
    #辞書作成
    task_dictionary[task_serial_num] = task[0]
    #タスクユニットを作成
    for j in range(task[1]):
        Task_unit_list.append((task_serial_num,j))
    task_serial_num += 1

#空き時間を求める
for schedule in schedule_list:
    for j in range(schedule[1],schedule[2]):
        if(j in Freetime_list):
            Freetime_list.remove(j)

#空き時間のタプルリストを作成
Freetime_tuple_list = []
for freetime in Freetime_list:
    Freetime_tuple_list.append(convert_int_to_tuple(freetime))

#タスクユニットと空き時間のペアリスト
t_unit_and_freetime = []
for task_unit in Task_unit_list:
    for freetime in Freetime_tuple_list:
        t_unit_and_freetime.append( merge_to_tuple(task_unit, freetime) )

#隣り合っているタスクのリストを求める
Adjacent_tasks_list = []
for i in range(len(Task_list)):
    for j in range(Task_list[i][1]):
        for k in range(j+1,Task_list[i][1]):
            Adjacent_tasks_list.append([(i,j),(i,k)])

#隣り合っている空き時間のリストを求める
Adjacent_freetimes_list = []
for j in range(len(Freetime_list)):
    if(j+1 <= len(Freetime_list) -1):
        if(is_adjacent(Freetime_list[j],Freetime_list[j+1])):
            Adjacent_freetimes_list.append([(Freetime_list[j],),(Freetime_list[j+1],)])

print(Adjacent_freetimes_list)
#変数の作成
x = pulp.LpVariable.dicts('x', t_unit_and_freetime, cat='Binary')
#z = pulp.LpVariable('z', cat= 'Continuous')
#print(x[('task1', 0, 1701356400)])
#print(t_unit_and_date)

#目的関数
#同じタスクはより多く隣接させる
#problem += pulp.lpSum(x[merge_to_tuple(task_list[0], freetime_list[0])] * x[merge_to_tuple(task_list[1], freetime_list[1])] + x[merge_to_tuple(task_list[0], freetime_list[1])] * x[merge_to_tuple(task_list[1], freetime_list[0])] for task_list in Adjacent_tasks_list for freetime_list in Adjacent_freetimes_list)
#非線形だから解けない!

#制約条件
#タスクユニットをどこかに割り当てる
for task_unit in Task_unit_list:
    problem += pulp.lpSum(x[merge_to_tuple(task_unit, freetime)]for freetime in Freetime_tuple_list) == 1

'''
#solveする
status = problem.solve()
print(status)
print(pulp.LpStatus[status])
'''