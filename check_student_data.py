import pandas as pd
import matplotlib.pyplot as plt

#csvの読み込み
s_df = pd.read_csv('students.csv')

#データの大きさの確認
print(len(s_df))

#データの中身の確認
print(s_df.head)

#各カラムのデータの確認
print(s_df['student_id'])

#学籍番号の最大値
print(s_df['student_id'].max())

#学籍番号の最小値
print(s_df['student_id'].min())

#1から318までが使われているか確認
print(set(range(1,319)) == set(s_df['student_id'].tolist()))

#男女の人数の確認
print(s_df['gender'].value_counts())

#スコアの確認
print(s_df['score'].describe())

#ヒストグラムの確認
#本に書いてあるコードとは違う
plt.hist(s_df['score'])
#plt.show()

#leader_flagのデータの確認
print(s_df['leader_flag'].value_counts())

#supporrt_flagの確認
print(s_df['support_flag'].value_counts())

#特定ペアデータの確認
s_pair_df = pd.read_csv('student_pairs.csv')
print(len(s_pair_df))
print(s_pair_df.head)
