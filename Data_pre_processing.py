#予定を用意する
schedule_list = [['学校',7,17],['就寝,朝',0,7],['風呂,夕食',19,20],['就寝,夜',22,24]]

#予定から、空き時間を求める
default_free_time_list = [[0,24]]

'''
空き時間が、4時～6時、18時～20時だとすると、
[ [4,6], [18,20] ] とする
'''

#空き時間のリストを作る
#空き時間のリストを編集する関数

def find_freetime(schedule,time_list):
    
    for sche in schedule:
        b = fill_schedule(sche,time_list)
        #変更後のリストを追加
        for i in b[0]:
            time_list.append(i)
        #変更前のリストを削除
        time_list.remove(b[1])

    return time_list

    
#スケジュールから空き時間リストの変更箇所を求める
def fill_schedule(schedule,free_time):
    new_freetime = []
    time_stock = []
    for time in free_time:
        #とりあえず、動く前提で分岐する
        #print(time)
        #print(schedule)
        if (time[0] <= schedule[1]   and schedule[2] <= time[1]):
            #予定を反映して、変更する部分の空き時間を求める
            if(time[0] < schedule[1]):
                new_freetime.append([time[0], schedule[1]])
            
            if(schedule[2] < time[1]):
                new_freetime.append([schedule[2], time[1]])
            time_stock = time
            break

    return [new_freetime,time_stock]

#使い方
default_free_time_list = find_freetime(schedule_list,default_free_time_list)

print(default_free_time_list)
'''
for sche in schedule:
    fill_schedule(sche)

'''