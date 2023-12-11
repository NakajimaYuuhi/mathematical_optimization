import pulp
import pandas as pd
import datetime
problem = pulp.LpProblem('Task_scheduling',pulp.LpMinimize)

#データの作成
#既に決まっているスケジュールのリスト
schedule_list = [['学校',7,17],['就寝,朝',0,7],['風呂,夕食',19,20],['就寝,夜',22,24]]

#タスクのリスト [タスク名,所要時間]
Task_list = []

#デフォルトの空き時間のリスト
default_free_time_list = [[0,24]]

#タスクユニット作成


#タスクユニットと空き時間のペアリスト


#関数
#隣合った時間かどうかを返す
def are_next_to_each_other(a,b):
    if (abs(a - b) == 1):
        return True
    else:
        return False

#変数の作成
x = pulp.LpVariable.dicts('x', t_unit_and_date, cat='Binary')
z = pulp.LpVariable('z', cat= 'Continuous')
#print(x[('task1', 0, 1701356400)])
#print(t_unit_and_date)

#目的関数
#同じタスクはより多く隣接させる

#制約条件
#タスクユニットをどこかに割り当てる

#solveする
status = problem.solve()
print(status)
print(pulp.LpStatus[status])