import numpy as np
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pprint


#
# 変数の数
#
#I = 2
#
# データ（係数など）
#
## 目的変数の係数
#a_data = np.array([4, 0.25])
## ベクトル（各制約式の下限）
#lower_data = np.array([0.5, 2])
#
# 辞書(dictionary)へ変換
#
## 目的変数の係数
#a = dict((i, a_data[i-1]) for i in range(1,I+1))
#print(a) # {1: 4.0, 2: 0.25}
## ベクトル（各制約式の下限）
#lower = dict((i, lower_data[i-1]) for i in range(1,I+1))

#モデルのインスタンス生成
model = pyo.ConcreteModel()

# 変数の添字の作成(変数のインデックスの作成)
# 添え字をタプルにする、内包表記で書く
# i:タスク,j:タスクユニット,k:日付
model.I = pyo.Set(initialize=((i,j,k)for i in range(1,3) for j in range(1,4)for k in range(1,5) ))
#model.I.pprint()
# 変数の定義
model.x = pyo.Var(model.I)
#model.x.pprint()

#目的関数の設定

#制約条件の設定