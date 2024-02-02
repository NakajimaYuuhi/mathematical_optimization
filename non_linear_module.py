import numpy as np
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pprint
import matplotlib.pyplot as plt
import pandas as pd
import plotly.figure_factory as ff
#最後まで動いた!!


'''
Task_list : (タスク名,所要時間)
task_unit
'''
#タスクリストの作成
Task_list = [['task1',2],['task2',3]]
#空き時間のリスト
Freetime_list = [[15,20],[21,23]]

def non_linear_scheduling(Task_list,Freetime_list):
    #タスク辞書の作成 {通し番号,タスク名}
    Task_dic_list = {}
    Task_num_list = []
    for i in range(0,len(Task_list)):
        Task_dic_list.setdefault(i,Task_list[i][0])
        Task_num_list.append(i)
        



    #タスクユニットリスト作成
    Task_unit_list = [(i,j)for i in Task_num_list for j in range(0,Task_list[i][1])]
    #print(Task_unit_list)

    #空き時間のリストの作成
    Freetime_linear_list  = []
    for i in Freetime_list:
        for j in range(i[0],i[1]):
            Freetime_linear_list.append(j)
            
    #print(Freetime_linear_list)

    #インデックスの作成 ユニットリストと空き時間
    Task_unit_Freetime_list = [(i,j,k)for i in Task_num_list for j in range(0,Task_list[i][1])for k in Freetime_linear_list]

    #print(Task_unit_Freetime_list)

    #隣接時間リストの作成
    Freetime_next_to_list = []
    for i in Freetime_list:
        for j in range(i[0],i[1]-1):
            Freetime_next_to_list.append([j,j+1])


    #モデルのインスタンス生成
    model = pyo.ConcreteModel()

    # 変数の添字の作成(変数のインデックスの作成)
    # 添え字をタプルにする、内包表記で書く
    # i:タスク,j:タスクユニット,k:日付
    model.I = pyo.Set(initialize=((i,j,k)for i in Task_num_list for j in range(0,Task_list[i][1])for k in Freetime_linear_list ))
    #model.I.pprint()
    # 変数の定義
    model.x = pyo.Var(model.I,domain =pyo.Binary)#バイナリに設定した
    #model.x.pprint()

    model.A = pyo.Set(initialize=[i for i in Task_unit_list])
    #model.A.pprint()
    model.B = pyo.Set(initialize=[i for i in Freetime_linear_list])
    model.C = pyo.Set(initialize=[i for i in Task_unit_Freetime_list])
    #目的関数の設定
    def ObjRule(model):
        return pyo.quicksum( pyo.quicksum(pyo.prod( pyo.quicksum(model.x[(i,j,k)]for j in range(0,Task_list[i][1]))for k in freetime_next_to_list)for freetime_next_to_list in Freetime_next_to_list) for i in Task_num_list )
    # 目的関数として設定
    model.obj = pyo.Objective(rule = ObjRule, sense = pyo.maximize)
    #model.obj.pprint()



    #制約条件の設定
    #タスクはすべて割り当てる
    def Construle1(model, i,j):#タプル型の中身が、別々の引数で来ているので、引数は新たに2つ必要
        #print('i:',i)
        #print('j:',j)
        return pyo.quicksum(model.x[(i,j,k)] for k in Freetime_linear_list) == 1
    model.eq1 = pyo.Constraint(model.A, rule = Construle1)#model.Aには、(0,0)のようにタプルが入っているが、引数2つで、別々に渡している

    def Construle2(model, j):#タプル型の中身が、別々の引数で来ているので、引数は新たに2つ必要
        #print('j:',j)
        return pyo.quicksum(model.x[(i)+(j,)] for i in Task_unit_list) <= 1
    model.eq2 = pyo.Constraint(model.B, rule = Construle2)
    #model.eq2.pprint()


    # ソルバーの設定
    opt = pyo.SolverFactory('couenne.exe')
    # 最適化の実施
    res = opt.solve(model)

    #結果の表を入れる場所
    result_dic = {}
    for i in Freetime_linear_list:
            result_dic[i]=-1

    #表示とデータ挿入
    #print(model.display())
    #print('\n')
    #print('optimum value = ', model.obj())
    for i in Task_unit_Freetime_list:
        if (model.x[i]() != 0):
            #print("x(" ,i,")= ", model.x[i]())
            result_dic[i[2]]=i[0]

    #print(result_dic)
    result_val = result_dic.values()


    #データ出力部分
    df=pd.DataFrame({'time':Freetime_linear_list,'task':result_val})
    #df=pd.DataFrame(data=result_list,index=Freetime_linear_list)
    #df=pd.DataFrame.from_dict(result_dic, orient='index')

    #print(df)
    return result_dic


#https://www.mutable.work/entry/import-other-scripts