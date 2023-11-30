import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

sns.set(font='IPAexGothic')

dataset = pd.DataFrame([[100, 200, 50], [300, 400, 600], [50, 300, 60]], 
                       columns=['A支店', 'B支店', 'C支店'], 
                       index=['4月', '5月', '6月'])

fig, ax = plt.subplots(figsize=(10, 8))
for i in range(len(dataset)):
    ax.bar(dataset.columns, dataset.iloc[i], bottom=dataset.iloc[:i].sum())
    for j in range(len(dataset.columns)):
        plt.text(x=j, 
                 y=dataset.iloc[:i, j].sum() + (dataset.iloc[i, j] / 2), 
                 s=dataset.iloc[i, j], 
                 ha='center', 
                 va='bottom'
                )
ax.set(xlabel='支店名', ylabel='売り上げ')
ax.legend(dataset.index)
plt.show()