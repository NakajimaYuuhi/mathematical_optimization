'''
「pythonで始める数理最適化」
P16 線形計画問題をPythonの数理最適化ライブラリで解く
'''

import pulp

#pulp.LpProbrem(任意の名前, 解く問題の種類)
problem = pulp.LpProblem('LP', pulp.LpMaximize)


x = pulp.LpVariable('x', cat= 'Continuous')
y = pulp.LpVariable('y', cat= 'Continuous')

#制約条件 probrem に 「+=」をつけて条件式を書く
problem += 1*x + 3*y <= 30
problem += 2*x + 1*y <= 40
problem += x >= 0
problem += y >= 0

#目的関数 「==」、「>=」などがない、ただの関数
problem += x + 2*y

#problem.solve 問題を解いて、statusコードを返す
status = problem.solve()


print('Status:', pulp.LpStatus[status])
#問題を解いてあとは、x.value()のように、値を参照できる
print('x=', x.value(), 'y=', y.value(), 'obj=', problem.objective.value())

'''
出力結果
command line - C:\Users\yuuhi\AppData\Local\Programs\Python\Python311\Lib\site-packages\pulp\solverdir\cbc\win\64\cbc.exe C:\Users\yuuhi\AppData\Local\Temp\8440aaccdbf0418fb273c5dd68aff1bb-pulp.mps max timeMode elapsed branch printingOptions all solution C:\Users\yuuhi\AppData\Local\Temp\8440aaccdbf0418fb273c5dd68aff1bb-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 9 COLUMNS
At line 18 RHS
At line 23 BOUNDS
At line 26 ENDATA
Problem MODEL has 4 rows, 2 columns and 6 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Presolve 2 (-2) rows, 2 (0) columns and 4 (-2) elements
0  Obj -0 Dual inf 2.999998 (2)
2  Obj 26
Optimal - objective value 26
After Postsolve, objective 26, infeasibilities - dual 0 (0), primal 0 (0)
Optimal objective 26 - 2 iterations time 0.002, Presolve 0.00
Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.01   (Wallclock seconds):       0.00


Status: Optimal
x= 18.0 y= 4.0 obj= 26.0

x,y 変数の値 obj 目的関数
'''