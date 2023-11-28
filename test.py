import datetime


'''
time = datetime.datetime.fromtimestamp(sec)
print(time)
print('年:',time.year)
print('月:',time.month)
print('日:',time.day)
'''

#UNIX時間から日付の文字列の出力

sec = 1577804400

def get_time_str(unix_time):
    time = datetime.datetime.fromtimestamp(unix_time)
    time_string = str(time.year)+'年'+ str(time.month) +'月'+str(time.day) +'日'
    return time_string
#print(get_time_str(sec))


#タスク情報の出力
Task_sample = [['task1',5,1701356400,1701874800], ['task2',7,1701615600,1701961200]]

def print_task_info(task_list):
    for task in task_list:
        print(task[0],'  ','所要時間:',task[1],'時間')
        print('開始:',get_time_str(task[2]),'  ','終了:',get_time_str(task[3]))

print_task_info(Task_sample)