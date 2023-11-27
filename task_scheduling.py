import pulp
import pandas as pd
problem = pulp.LpProblem('Task_scheduling',pulp.LpMinimize)
#タスク
#タスク名、所要時間、開始時間、終了時間(締め切り)
#開始時間、終了時間はUNIX時間(日本時間)

"""
タスク1:
所要時間:5時間
開始時間:2023,12,01,00:00
終了時間:2023,12,07,00:00
"""
Task_sample = [['task1',5,1701356400,1701874800	]]
#11/30～12/8
Date_list = [1701270000, 1701356400, 1701442800, 1701529200, 1701615600, 1701702000, 1701788400, 1701874800, 1701961200]

def convert_int_to_tuple(A):
    return tuple([A])

def merge_to_tuple(A,B):
    return A+B

#タスク名のリスト:task_nameを生成
task_name = []
for task in Task_sample:
    task_name.append(task[0])

#タスクユニットのリスト:task_unitを生成
task_unit_list = []
for task in Task_sample:
    for i in range(task[1]):
        task_unit_list.append((task[0],i))

#日付のタプルリストを作成
date_tuple_list = []
for date in Date_list:
    date_tuple_list.append(convert_int_to_tuple(date))


#タスクユニットと、日付のペアリストの生成
t_unit_and_date = []
for task_unit in task_unit_list:
    for date_tuple in date_tuple_list:
        t_unit_and_date.append( merge_to_tuple(task_unit, date_tuple) )

#空き時間のリスト、freetime_listの作成
freetime_list = [(5,),(5,),(5,),(5,),(5,),(5,),(5,),(5,),(5,)]

#変数の作成
x = pulp.LpVariable.dicts('x', t_unit_and_date, cat='Binary')
z = pulp.LpVariable('z', cat= 'Continuous')
#print(x[('task1', 0, 1701356400)])
print(t_unit_and_date)

#目的関数
problem += z

#制約条件
#タスクユニットをどこかに割り当てる
for task_unit in task_unit_list:
    problem += pulp.lpSum(x[merge_to_tuple(task_unit, date_tuple)]for date_tuple in date_tuple_list) == 1

#タスクを空き時間より多く、割り当てない
i=0
for date_tuple in date_tuple_list:
    problem += freetime_list[i] - pulp.lpSum(x[merge_to_tuple(task_unit, date_tuple)] for task_unit in task_unit_list) >= 0
    i+=1

#余裕を持たせる
#初期段階として、開始日から締め切りまでの期間に割り当てられればよし

#締め切りまでに終わらせる
for task_unit in task_unit_list:
    for date_tuple in date_tuple_list:
        #タスクの締め切り - x[t_unit,date]
        problem += Task_sample[task_name .index(task_unit[0])][3] - x[merge_to_tuple(task_unit, date_tuple)] >= 0

for task_unit in task_unit_list:
    for date_tuple in date_tuple_list:
        #x[t_unit,date] - タスクの開始日 
        problem += x[merge_to_tuple(task_unit, date_tuple)] - Task_sample[task_name.index(task_unit[0])][2]  >= 0

#solve
status = problem.solve()
print(status)
print(pulp.LpStatus[status])