import pulp
import pandas as pd
import datetime
import plotly.figure_factory as ff
from non_linear_module import non_linear_scheduling
import time

taketime = -1*time.time()

def get_time_str(unix_time):
    unixtime_datetime = datetime.datetime.fromtimestamp(unix_time)
    strdate = d_week[unixtime_datetime.strftime('%a')] + unixtime_datetime.strftime(', %m/%d/%Y')
    return(strdate)

def get_unixtime(month_week_date):    
    month_week_date_time = month_week_date +' 00:00:00'
    datetime_date = datetime.datetime.strptime(month_week_date_time, '%Y/%m/%d %H:%M:%S')
    print(datetime_date)
    unixtime = datetime_date.timestamp()
    return unixtime

def get_datetime(month_week_date):    
    month_week_date_time = month_week_date +' 00:00:00'
    datetime_date = datetime.datetime.strptime(month_week_date_time, '%Y/%m/%d %H:%M:%S')
    return datetime_date

def get_datelist(start,end):
    get_unixtime(start)
    start_datetime = get_datetime(start)
    end_datetime = get_datetime(end)
    'datetimeのlistを作成'
    datelist_datetime = []
    while(start_datetime <= end_datetime):
         datelist_datetime.append(int(start_datetime.timestamp()))
         start_datetime += datetime.timedelta(days=1)
    return datelist_datetime 

taketime = -1*time.time()
d_week = {'Sun':'Sunday','Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday'}
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
#Task_sample = [['task1',5,1701356400,1701874800], ['task2',7,1701615600,1701961200]]
#サンプルタスク
#Task_sample = [['task1',5,1701356400,1701615600],['task2',7,1701615600,1701961200],['task3',8,1701356400,1701874800]]
#課題、レポート、勉強
#Task_sample = [['task1',4,1701356400, 1701874800],['task2',10,1701356400,1701874800],['task3',5,1701788400,1701874800]]
#課題3つ、レポート
#Task_sample = [['report',10,1701356400,1701874800],['homework1',1,1701356400, 1701442800],['homework2',1,1701356400,1701615600],['homework3',1,1701356400,1701788400]]

#課題3つ、レポート new
Task_sample = [['report',10,1701356400,1701874800],['homework1',1,1701356400, 1701442800],['homework2',1,1701529200,1701615600],['homework3',2,1701615600,1701788400]]

#Task_sample = [['report',10,1701356400,get_unixtime('2023/12/25')],['homework1',1,1701356400, get_unixtime('2023/12/25')],['homework2',1,1701529200,get_unixtime('2023/12/25')],['homework3',2,1701615600,get_unixtime('2023/12/25')]]
#1か月用のデータ
#Task_sample = [['report1',10,get_unixtime('2023/12/05'),get_unixtime('2023/12/11')],['homework1',1,get_unixtime('2023/12/05'),get_unixtime('2023/12/06')],['homework2',1,get_unixtime('2023/12/07'), get_unixtime('2023/12/08')],['homework3',2,get_unixtime('2023/12/08'),get_unixtime('2023/12/10')],['report2',10,get_unixtime('2023/12/12'),get_unixtime('2023/12/18')],['homework4',1,get_unixtime('2023/12/12'),get_unixtime('2023/12/13')],['homework5',1,get_unixtime('2023/12/14'), get_unixtime('2023/12/15')],['homework6',2,get_unixtime('2023/12/15'),get_unixtime('2023/12/17')],['report3',10,get_unixtime('2023/12/19'),get_unixtime('2023/12/25')],['homework7',1,get_unixtime('2023/12/19'),get_unixtime('2023/12/20')],['homework8',1,get_unixtime('2023/12/21'), get_unixtime('2023/12/22')],['homework9',2,get_unixtime('2023/12/22'),get_unixtime('2023/12/24')],['report4',10,get_unixtime('2023/12/26'),get_unixtime('2024/01/01')],['homework10',1,get_unixtime('2023/12/26'),get_unixtime('2023/12/27')],['homework11',1,get_unixtime('2023/12/28'), get_unixtime('2023/12/29')],['homework12',2,get_unixtime('2023/12/29'),get_unixtime('2023/12/31')]]

#2週間用
#Task_sample = [['report1',10,get_unixtime('2023/12/05'),get_unixtime('2023/12/11')],['homework1',1,get_unixtime('2023/12/05'),get_unixtime('2023/12/06')],['homework2',1,get_unixtime('2023/12/07'), get_unixtime('2023/12/08')],['homework3',2,get_unixtime('2023/12/08'),get_unixtime('2023/12/10')],['report2',10,get_unixtime('2023/12/12'),get_unixtime('2023/12/18')],['homework4',1,get_unixtime('2023/12/12'),get_unixtime('2023/12/13')],['homework5',1,get_unixtime('2023/12/14'), get_unixtime('2023/12/15')],['homework6',2,get_unixtime('2023/12/15'),get_unixtime('2023/12/17')]]

#1か月スカスカ用
#Task_sample = [['report',10,get_unixtime('2023/12/05'),get_unixtime('2024/01/01')],['homework1',1,get_unixtime('2023/12/05'),get_unixtime('2024/01/01')],['homework2',1,get_unixtime('2023/12/05'),get_unixtime('2024/01/01')],['homework3',2,get_unixtime('2023/12/05'),get_unixtime('2024/01/01')]]

#試作
#Task_sample = [['report',10,1701356400,1701874800],['homework1',1,1701356400, 1701442800],['homework2',1,1701529200,1701615600],['homework3',2,1701356400,1701788400]]
#3週間のデータ
#Task_sample = [['report1',10,get_unixtime('2023/12/05'),get_unixtime('2023/12/11')],['homework1',1,get_unixtime('2023/12/05'),get_unixtime('2023/12/06')],['homework2',1,get_unixtime('2023/12/07'), get_unixtime('2023/12/08')],['homework3',2,get_unixtime('2023/12/08'),get_unixtime('2023/12/10')],['report2',10,get_unixtime('2023/12/12'),get_unixtime('2023/12/18')],['homework4',1,get_unixtime('2023/12/12'),get_unixtime('2023/12/13')],['homework5',1,get_unixtime('2023/12/14'), get_unixtime('2023/12/15')],['homework6',2,get_unixtime('2023/12/15'),get_unixtime('2023/12/17')],['report3',10,get_unixtime('2023/12/19'),get_unixtime('2023/12/25')],['homework7',1,get_unixtime('2023/12/19'),get_unixtime('2023/12/20')],['homework8',1,get_unixtime('2023/12/21'), get_unixtime('2023/12/22')],['homework9',2,get_unixtime('2023/12/22'),get_unixtime('2023/12/24')]]

#11/30～12/8
#Date_list = [1701270000, 1701356400, 1701442800, 1701529200, 1701615600, 1701702000, 1701788400, 1701874800, 1701961200]
#普通の期間
Date_list = [1701356400, 1701442800, 1701529200, 1701615600, 1701702000, 1701788400, 1701874800]

#3週間生成
#date1 ='2023/12/05'
#date2 = '2023/12/25'
#Date_list = get_datelist(date1,date2)

#1か月生成
#date1 ='2023/12/05'
#date2 = '2024/01/01'
#Date_list = get_datelist(date1,date2)

#2か月生成
#date1 ='2023/12/05'
#date2 = '2024/01/29'
#Date_list = get_datelist(date1,date2)

#2週間生成
#date1 ='2023/12/05'
#date2 = '2023/12/18'
#Date_list = get_datelist(date1,date2)

#サンプル
#date_freetime_list = [[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]]]
#空き時間バラバラ
#date_freetime_list = [[[17,19],[23,24]],[[22,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[23,24]],[[7,9],[10,11],[22,24]],[[7,9],[10,12],[13,16],[22,24]]]
#標準2
#date_freetime_list = [[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]]]
#暇2
#date_freetime_list = [[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[8,11],[13,16],[22,24]],[[8,11],[13,16],[22,24]],[[15,19],[23,24]]]
#忙しい2
#date_freetime_list = [[[22,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[23,24]],[[7,10],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]]]
#1か月分標準
#date_freetime_list = [[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]]]
#1か月分暇
#date_freetime_list = [[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[8,11],[13,16],[22,24]],[[8,11],[13,16],[22,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[8,11],[13,16],[22,24]],[[8,11],[13,16],[22,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[8,11],[13,16],[22,24]],[[8,11],[13,16],[22,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[15,19],[23,24]],[[8,11],[13,16],[22,24]],[[8,11],[13,16],[22,24]],[[15,19],[23,24]]]
#評価用空き時間14
#date_freetime_list =[[[16,18]],[[16,18]],[[17,18]],[[16,18]],[[13,16]],[[13,16]],[[17,18]]]

#2週間標準
#date_freetime_list = [[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[16,19],[23,24]],[[17,19],[23,24]],[[16,19],[23,24]],[[7,11],[13,16],[22,24]],[[7,11],[13,16],[22,24]],[[17,19],[23,24]]]

#評価用空き時間スカスカ105
#date_freetime_list =[[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]]]
#評価用空き時間スカスカ1か月
#date_freetime_list =[[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]],[[7,12],[13,19],[20,24]]]
#date_freetime_list =[[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]],[[7,12]]]

date_freetime_list =[[[0,8]],[[0,8]],[[0,8]],[[0,8]],[[0,8]],[[0,8]],[[0,8]]]
#空き時間のリスト、freetime_listの作成
#サンプル空き時間
#freetime_list = [(5,),(5,),(10,),(10,),(5,),(5,),(5,),(5,),(5,)]
#忙しい人用の空き時間
#freetime_list = [(5,),(2,),(2,),(4,),(2,),(2,),(4.9,),(8,),(5,)]
#標準的な空き時間
#freetime_list = [(5,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(5,)]
#空き時間がバラバラ
#freetime_list = [(3,),(2,),(4,),(3,),(1,),(5,),(9,)]
#標準2
#freetime_list = [(4,),(4,),(3,),(4,),(8.9,),(9,),(3,)]
#暇2
#freetime_list = [(5,),(5,),(5,),(5,),(8,),(8,),(5,)]
#忙しい2
#freetime_list = [(2,),(4,),(3,),(1,),(5,),(9,),(3,)]

#1か月分標準
#freetime_list = [(4,),(4,),(3,),(4,),(8.9,),(9,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(3,)]
#1か月分暇
#freetime_list = [(5,),(5,),(5,),(5,),(8,),(8,),(5,),(5,),(5,),(5,),(5,),(8,),(8,),(5,),(5,),(5,),(5,),(5,),(8,),(8,),(5,),(5,),(5,),(5,),(5,),(8,),(8,),(5,)]
#評価用空き時間14
#freetime_list = [(2,),(2,),(1,),(2,),(3,),(3,),(1,)]
#評価用空き時間スカスカ105
#freetime_list = [(15,),(15,),(15,),(15,),(15,),(15,),(15,)]
#評価用空き時間スカスカ1か月
#freetime_list = [(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,),(15,)]
#標準2 2週間
#freetime_list = [(4,),(4,),(3,),(4,),(8.9,),(9,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(3,)]
#3週間
#freetime_list = [(4,),(4,),(3,),(4,),(8.9,),(9,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(3,),(4,),(4,),(3,),(4,),(8.9,),(9,),(3,)]
freetime_list = [(8,),(8,),(8,),(8,),(8,),(8,),(8,)]

def convert_int_to_tuple(A):
    return tuple([A])

def convert_str_to_tuple(A):
    return tuple([A])

def merge_to_tuple(A,B):
    return A+B

def get_viable_date(start, end):
    flag = 0
    viable_date = []
    for date in Date_list:
        if(date == start):
            flag = 1
        if(flag == 1):
            viable_date.append(convert_int_to_tuple(date))
        if(date == end):
            flag = 0
    return viable_date

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



#変数の作成
x = pulp.LpVariable.dicts('x', t_unit_and_date, cat='Binary')
z = pulp.LpVariable('z', cat= 'Continuous')
#print(x[('task1', 0, 1701356400)])
#print(t_unit_and_date)

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

#for task in Task_sample:
    #problem += pulp.lpSum(pulp.lpSum( x[merge_to_tuple( merge_to_tuple(convert_str_to_tuple(task[0]), convert_int_to_tuple(i)), date )] for date in get_viable_date( task[2],task[3]) ) for i in range(task[1])) - task[1] == 0
    #print(get_viable_date( task[2],task[3]))

for task in Task_sample:
    for date_tuple in date_tuple_list:
        if(not(date_tuple[0]>= task[2] and  date_tuple[0] <= task[3])):#タスクを実行不可能な日を抽出
            print(task[0],task[2],task[3],date_tuple[0])
            problem += pulp.lpSum( x[merge_to_tuple( merge_to_tuple(convert_str_to_tuple(task[0]), convert_int_to_tuple(i)), date_tuple )] for i in range(task[1]) )  == 0 #実行不可能な日に割り当てない
            
#maxを記述する制約条件
#一日の作業時間はz以下
'''
for date_tuple in date_tuple_list:
    problem += pulp.lpSum( x[merge_to_tuple(task_unit, date_tuple)] for task_unit in task_unit_list ) <= z
'''            
for i in range(0,len(date_tuple_list)):
    problem += (pulp.lpSum( x[merge_to_tuple(task_unit, date_tuple_list[i])] for task_unit in task_unit_list ))/freetime_list[i][0] <= z


#zは作業時間の最大値なので、非負制約が必要
problem += z >= 0



def print_task_info(task_list):
    for task in task_list:
        print(task[0],'  ','所要時間:',task[1],'時間')
        print('開始:',get_time_str(task[2]),'  ','終了:',get_time_str(task[3]))

#solve
status = problem.solve()
print(status)
print(pulp.LpStatus[status])

#解いた後どうするか


def tuple_task_unit_date_print(tuple):
    #print('(')
    #print(tuple[0],',',tuple[1],',',get_time_str(tuple[2]))
    #print(')')
    return str(tuple[0])+','+str(tuple[1])+','+get_time_str(tuple[2])
    

#print('最大作業時間:',z.value())

#print('全部表示')
#print_task_info(Task_sample)
result_date_list = []
count = 0
for task in Task_sample:
    result_date_list.append([])
    for index in range(task[1]):
        for date_tuple in date_tuple_list:
            if(x[merge_to_tuple((task[0],index), date_tuple)].value()==1.0):
                result_date_list[count].append(date_tuple[0])
                #print('x[',tuple_task_unit_date_print(( merge_to_tuple((task[0],index), date_tuple) )),']:')
                #print(x[merge_to_tuple((task[0],index), date_tuple)].value())
    count += 1
count = 0         
for task in Task_sample:
    result_date_list.append([])
    #print(task[0],':')
    #for date_tuple in date_tuple_list:
        #print(get_time_str(date_tuple[0]),':',result_date_list[count].count(date_tuple[0]))
    count += 1

#print('合計:')
for date_tuple in date_tuple_list:
    list = 0
    for i in range(count):
        list += result_date_list[i].count(date_tuple[0])
    #print(get_time_str(date_tuple[0]),':',list)
#1のやつ抽出
result_date_list2 = []
for i in t_unit_and_date:
    if (x[i].value() != 0):
        #print("x(" ,i,")= ", x[i].value())
        result_date_list2.append(i)
#print(result_date_list2)

#データフレーム作成
#タスクのリスト作成
#task_num_data= [i for i in range(0,len(Task_sample))]
task_num_data= [i[0] for i in Task_sample]
task_num_data.append('Total')
#日付はDate_listを使う
#結果をまとめるリストの作成
result_data = [[0 for i in range(0,len(Task_sample))] for j in Date_list]
#結果を記録
for i in result_date_list2:
    result_data[Date_list.index(i[2])][task_name.index(i[0])]+=1
#合計の追加
result_total = [0 for i in range(0,len(Date_list))]
for i in range(0,len(result_data)):
    for j in result_data[i]:
        result_total[i] += j
#print(result_total)
for i in range(0,len(result_data)):
    result_data[i].append(result_total[i])
#辞書作成
result_data_dic = {}
#タスクの追加
result_data_dic['Tasks']=task_num_data
#結果の追加
for i in range(0,len(result_data)):
    result_data_dic[get_time_str(Date_list[i])] = result_data[i]
#print(result_data_dic)
#print(result_data)
#データフレームに入れる
df=pd.DataFrame(result_data_dic)
#df=pd.DataFrame(data=result_list,index=Freetime_linear_list)
#df=pd.DataFrame.from_dict(result_dic, orient='index')

print(df)
df.to_csv("task_scheduling_1st.csv", encoding="shift-jis")

#グラフ化、出力
fig = ff.create_table(df)
fig.update_layout(
    autosize=False,
    width=500,
    height=200,
    title_xanchor = "center",
    title_yanchor = "middle",
    legend_xanchor= "center",
    legend_yanchor= "middle"
)
#fig.write_image("task_schediling_result.png", scale=2)
#文字が長すぎておさまってないが一応できてる

#ここから2段階目
#for分で最適化
#for文で取得
result_final_dic = {}
for i in range(0,len(df.columns)):
    if(i != 0):
        #print(i,'列目')
        #print(df.iloc[:len(df)-1,i])#列の取得
        list = []
        for j in range(0,len(df.iloc[:len(df)-1,i])):
            list.append([Task_sample[j][0],df.iloc[:len(df)-1,i][j]])#jはタスク名に変える2
        #print(get_time_str(Date_list[i-1]),list,date_freetime_list[i-1])
        #割り当てが0の時は2段階をスルー
        if(df.iat[len(df)-1,i] != 0):
            result_final_dic[get_time_str(Date_list[i-1])]=non_linear_scheduling(list,date_freetime_list[i-1])#ここで渡す
        else:
            result_final_dic[get_time_str(Date_list[i-1])]={}
        #print(result_final_dic)

#結果をデータフレームに入れる
#データフレームの作成
dfdata = [] 
for i in range(0,24):
    dfdata.append([-1 for i in Date_list])
dfindex = [i for i in range(0,24)]
dfcolumns =  [get_time_str(i) for i in Date_list]
result_final_df = pd.DataFrame(data=dfdata, index=dfindex, columns=dfcolumns)

#データフレームに値を入れる
for i in result_final_dic.keys():
    for j in result_final_dic[i].keys():
        result_final_df.at[j, i]=result_final_dic[i][j]
# 結果出力
print(result_final_df)
result_final_df.to_csv("task_scheduling_2nd.csv", encoding="shift-jis")
taketime+=time.time()
print(taketime)

#unix時間の扱い
#https://python.civic-apps.com/unixtime-now/
#datetime型からの数値の取り出し方
#https://di-acc2.com/programming/python/22894/#index_id12
#Pythonのmatplotlibで積み上げ棒グラフを作成しデータラベルを追加してみた
#https://qiita.com/s_fukuzawa/items/6f9c1a3d4c4f98ae6eb1
#Matplotlib 日本語の表示方法｜簡単にいろんな日本語フォントを使う方法
#https://www.yutaka-note.com/entry/matplotlib_japanese
'''
result_date_list = []
stock_str = ' '
print_task_info(Task_sample)
for task_unit in task_unit_list:
    for date_tuple in date_tuple_list:
        if(x[merge_to_tuple(task_unit, date_tuple)].value()==1.0):
            #リストに、実施日を保存していく
            if(task_unit[0] == stock_str or stock_str == ' '):
                result_date_list.append(date_tuple[0])
                stock_str = task_unit[0]
            else:
                #1つのタスクの実施日を入れ終えていたら、出力し、リストをリセット
                print(stock_str,':')
                stock_str = task_unit[0]
                for date_tuple in date_tuple_list:
                    print(get_time_str(date_tuple[0]),':',result_date_list.count(date_tuple[0]))
                result_date_list = []
                result_date_list.append(date_tuple[0])

            print('x[',merge_to_tuple(task_unit, date_tuple),']:')
            print(x[merge_to_tuple(task_unit, date_tuple)].value())
    #タスクをいつ、何時間やるか出力する
print(stock_str,':')
for date_tuple in date_tuple_list:
    print(get_time_str(date_tuple[0]),':',result_date_list.count(date_tuple[0]))
#print(sorted(result_date_list))
'''

#1か月 3.128261089324951