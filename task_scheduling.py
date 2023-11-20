import pulp
import pandas as pd
problem = pulp.LpProblem('Task_scheduling', pulp.LpMaximize)
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
Date_list = [1701356400,1701442800]

def convert_int_to_tuple(A):
    return tuple([A])

def merge_to_tuple(A,B):
    return A+B

#タスク名のリスト:task_nameを生成
task_name = []
for task in Task_sample:
    task_name.append(task[0])

#タスクユニットのリスト:task_unitを生成
task_unit = []
for task in Task_sample:
    for i in range(task[1]):
        task_unit.append((task[0],i))

#タスクユニットと、日付のペアリストの生成
t_unit_and_date = []
for t_unit in task_unit:
    for date in Date_list:
        date_tuple = convert_int_to_tuple(date)
        t_unit_and_date.append( merge_to_tuple(t_unit, date_tuple) )


#変数の作成
x = pulp.LpVariable.dicts('x', t_unit_and_date, cat='Binary')
print(x[('task1', 0, 1701356400)])
#print(x)