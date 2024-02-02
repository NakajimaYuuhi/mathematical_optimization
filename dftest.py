import pandas as pd

Task_sample = [['task1',4,1701356400, 1701874800],['task2',10,1701356400,1701874800],['task3',5,1701788400,1701874800]]
df=pd.DataFrame({'task':[0,1,2,'total'],'0':[4,8,12,24],'1':[4,8,12,24],'2':[0,0,0,0]})
date_freetime_list = [[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]],[[15,20],[21,23]]]
print(df)

#インデックスでの列の取得
#print(df.iloc[:,0])
'''
#for文で取得
for i in df:
    print(i)#列名が取得されている
'''

#行数の取得
print('行数:',len(df))

#列数の取得
print('列数:',len(df.columns))

#for文で取得
for i in range(0,len(df.columns)):
    if(i != 0):
        print(i,'列目')
        print(df.iloc[:len(df)-1,i])#列の取得
        list = []
        for j in range(0,len(df.iloc[:len(df)-1,i])):
            list.append([Task_sample[j][0],df.iloc[:len(df)-1,i][j]])#jはタスク名に変える2
        #print(list,date_freetime_list[i-1])#ここで渡す
        print(df.iat[len(df)-1,i])

