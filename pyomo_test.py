import numpy as np
import pyomo.environ as pyo
from pyomo.opt import SolverFactory

#
# 変数の数
#
I = 2
#
# データ（係数など）
#
## 目的変数の係数
a_data = np.array([4, 0.25])
## ベクトル（各制約式の下限）
lower_data = np.array([0.5, 2])
#
# 辞書(dictionary)へ変換
#
## 目的変数の係数
## 目的変数の係数
a = dict((i, a_data[i-1]) for i in range(1,I+1))
## ベクトル（各制約式の下限）
lower = dict((i, lower_data[i-1]) for i in range(1,I+1))

#モデルのインスタンス生成
model = pyo.ConcreteModel()

#変数の定義　=　辞書のキーの設定

# 変数の添字
model.I = pyo.Set(initialize=range(1, I+1))
# 変数の定義
model.x = pyo.Var(model.I)

model.I.pprint()
model.x.pprint()