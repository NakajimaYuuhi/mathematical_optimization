import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

sns.set(font='IPAexGothic')
'''
dataset = pd.DataFrame([[100, 200, 50], [300, 400, 600], [50, 300, 60]], #タスクのその日の割り当て数に変更する
                       columns=['A支店', 'B支店', 'C支店'], #dateに変更する
                       index=['4月', '5月', '6月'])#task_nameに変更する

'''
dataset = pd.DataFrame([[1, 2, 1], [3, 1, 1], [1, 1, 1]], #タスクのその日の割り当て数に変更する 0の時に表示がおかしくなる 表示が真ん中じゃない時がある
                       columns=['12月1日', '12月2日', '12月3日'], #dateに変更する
                       index=['課題1', '課題2', '課題3'])#task_nameに変更する


fig, ax = plt.subplots(figsize=(10, 8))
for i in range(len(dataset)):
    ax.bar(dataset.columns, dataset.iloc[i], bottom=dataset.iloc[:i].sum())
    for j in range(len(dataset.columns)):
        plt.text(x=j, 
                 y=dataset.iloc[:i, j].sum() + (dataset.iloc[i, j] / 2), 
                 s=dataset.iloc[i, j], 
                 ha='center', 
                 va='center'
                )
ax.set(xlabel='日付', ylabel='実施時間')
ax.legend(dataset.index)
plt.show()

#使ったサンプルコード
#https://qiita.com/s_fukuzawa/items/6f9c1a3d4c4f98ae6eb1ju


#plt.textの内容
#https://www.yutaka-note.com/entry/2020/01/08/080413#%E6%B0%B4%E5%B9%B3%E6%96%B9%E5%90%91%E3%81%AE%E6%96%87%E5%AD%97%E4%BD%8D%E7%BD%AEhorizontalalignment-%E3%81%BE%E3%81%9F%E3%81%AF-ha
#棒グラフ全般
#https://pythondatascience.plavox.info/matplotlib/%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95