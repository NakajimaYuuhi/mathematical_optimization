import numpy as np
import pyomo.environ as pyo
from pyomo.opt import SolverFactory
import pprint


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
print(a) # {1: 4.0, 2: 0.25}
## ベクトル（各制約式の下限）
lower = dict((i, lower_data[i-1]) for i in range(1,I+1))

#モデルのインスタンス生成
model = pyo.ConcreteModel()

# 変数の添字
model.I = pyo.Set(initialize=range(1, I+1))
model.I.pprint()
# 変数の定義
model.x = pyo.Var(model.I)
model.x.pprint()
# 目的関数の数式の定義
def ObjRule(model):
    return sum(a[i] * (model.x[i])**2 for i in model.I)
# 目的関数として設定
model.obj = pyo.Objective(rule = ObjRule, sense = pyo.minimize)

#制約条件
# 制約1
def Construle1(model):
    return model.x[1]*model.x[2] >= 1
model.eq1 = pyo.Constraint(rule = Construle1)
# 制約2
def Construle2(model, i):
    return model.x[i] >= lower[i]
model.eq2 = pyo.Constraint(model.I, rule = Construle2)

# ソルバーの設定
opt = pyo.SolverFactory('ipopt.exe')
# 最適化の実施
res = opt.solve(model)



print(model.display())
print('\n')
print('optimum value = ', model.obj())
print("x = ", model.x[:]())


#参考サイト
#https://www.salesanalytics.co.jp/datascience/datascience138/
#https://helve-blog.com/posts/python/pyomo-nonlinear-programming/

#環境構築
#https://youtu.be/EB_qVoM74Fg?si=ipO7I7tPuL8xCvHb
