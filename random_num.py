import random
import itertools
from numpy import kaiser
total = random.randrange(1,10+1)

def random_num_list_generate(num):
    list=[]
    while num != 0:
        i = random.randrange(1,num+1)
        num -= i
        list.append(i)

    return list

print(total)
print('空き時間',random_num_list_generate(total))
print('タスク',random_num_list_generate(total))

FreeTime_list = [1,4,1]
Task_list = [4,1,1]
FreeTime_is_scheduled = [-1 for i in range(len(FreeTime_list))]
Task_scheduled_index = [-1 for i in range(len(Task_list))]


#freetimeとtaskの所要時間が一致したものを割り当てる
def scheduling_task(freetime_list,task_list,freetime_is_scheduled,task_scheduled_index):
    for task_index in range(len(task_list)):
        for freetime_index in range(len(freetime_list)):
            #freetimeとtaskの所要時間が一致した、かつまだ割り当てていないものかを判断
            if(task_list[task_index] == freetime_list[freetime_index] and freetime_is_scheduled[freetime_index] == -1 and task_scheduled_index[task_index] == -1):
                freetime_is_scheduled[freetime_index] = 1
                task_scheduled_index[task_index] = freetime_index
                break
    
    return [freetime_is_scheduled,task_scheduled_index]

result = scheduling_task(FreeTime_list,Task_list,FreeTime_is_scheduled,Task_scheduled_index)
#print(result[1])

FreeTime_list = [2]
Task_list = [1,1]
FreeTime_is_scheduled = [-1 for i in range(len(FreeTime_list))]
Task_scheduled_index = [-1 for i in range(len(Task_list))]
#足したもので一致するなら、割り当てる
def scheduling_add_task(freetime_list,task_list):
    for lst in get_combinations(len(task_list)):
        a = 0
        for i in lst:
            a += i
        for freetime in freetime_list:
            if(freetime == a):
                
    
#組み合わせの生成
def get_combinations(end):
    lst = []
    for n in range(2,end+2):
        for team in itertools.combinations([i for i in range(end+1)], n):
	        lst.append(list(team))
    return lst