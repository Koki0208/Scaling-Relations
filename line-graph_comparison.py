import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import numpy as np
from math import log

# ブロック伝搬時間は1,フォーク確率は2
select = 1

if select == 1:
    # データセット(x_values...ブロックサイズ y_values_set(1,2,3,4)...平均ブロック伝搬時間 y_values_set1...10node y_values_set2...100node y_values_set3...1000node y_values_set4...10000node)
    x_values = [0.2, 0.5, 1, 10, 100, 1000]
    y_values_set1 = [1.8597475049900218, 1.8868423153692662, 1.8992457542457537, 2.6520667330677297, 11.235130822596636, 77.3540557692308]  # データセット1
    y_values_set2 = [3.315211940298508, 3.4799780439121726, 4.152063745019917, 15.764970149253735, 110.9485988428157, 1299.1862653721687]  # データセット2
    y_values_set3 = [4.397545908183635, 4.635616383616392, 5.2181327345309425, 19.669640079760708, 147.87546491228068, 1451.864203899267]  # データセット3
    y_values_set4 = [5.288456630109671, 6.1073874501992025, 6.835490547263678, 25.203860557768895, 205.95863213939984, 2067.7742869496856] # データセット4
if select == 2:
    # データセット(x_values...ブロックサイズ y_values_set(1,2,3,4)...平均ブロック伝搬時間 y_values_set1...10node y_values_set2...100node y_values_set3...1000node y_values_set4...10000node)
    x_values = [0.2, 0.5, 1, 10, 100, 1000]
    y_values_set1 = [0.09990, 0.09990, 0.00000, 0.29910, 0.79365, 3.75361]  # データセット1
    y_values_set2 = [0.39841, 0.09990, 0.29910, 0.39841, 3.47490, 15.48223]  # データセット2
    y_values_set3 = [0.09990, 0.00000, 0.09990, 0.19960, 2.43902, 16.20487]  # データセット3
    y_values_set4 = [0.19960, 0.29910, 0.39841, 0.29910, 3.19767, 16.87448] # データセット4

#τfork = αB + β→スケーリング関係式 τfork = αBlog(n)+β  (τfork...ブロック伝搬時間B...ブロックサイズ,n...ノード数)
x_values1 = [value * 10*log(10) for value in x_values]
x_values2 = [value * 100*log(100) for value in x_values]
x_values3 = [value * 1000*log(1000) for value in x_values]
x_values4 = [value * 10000*log(10000) for value in x_values]

#全てのデータセットを結合
all_x_values = np.concatenate([x_values1, x_values2, x_values3, x_values4])
# all_x_values = np.concatenate([x_values2, x_values3, x_values4])
all_y_values = np.concatenate([y_values_set1, y_values_set2, y_values_set3, y_values_set4])
# all_y_values = np.concatenate([y_values_set2, y_values_set3, y_values_set4])
# データをスケーリング
scaling_factor = max(all_x_values)
scaled_x_values = all_x_values / scaling_factor

# データを対数変換
log_x = np.log(scaled_x_values)
log_y = np.log(all_y_values)
# NaNまたは無限大を含むデータを除去
finite_mask = np.isfinite(log_x) & np.isfinite(log_y)
log_x = log_x[finite_mask]
log_y = log_y[finite_mask]

#線形フィッティング　τfork = αBlog(n)+β  τfork...ブロック伝搬時間B...ブロックサイズ,n...ノード数
def linear_fit(x, a, b):
    return  a*x + b
param, cov = curve_fit(linear_fit, log_x, log_y)

# 折れ線グラフを作成
plt.figure(figsize=(8, 6))

# データセット1をプロット
plt.plot(x_values1, y_values_set1, marker='o', linestyle='-', color='b', label='10node')

# データセット2をプロット
plt.plot(x_values2, y_values_set2, marker='o', linestyle='-', color='r', label='100node')

# データセット3をプロット
plt.plot(x_values3, y_values_set3, marker='o', linestyle='-', color='g', label='1000node')

# データセット4をプロット
plt.plot(x_values4, y_values_set4, marker='o', linestyle='-', color='m', label='10000node')

#線形フィッティングをプロット
array_y_fit = param[0] * log_x + param[1]
plt.plot(np.exp(log_x) * scaling_factor, np.exp(array_y_fit), marker="", color='k', label='linear fitting')

# x軸とy軸のラベルとタイトルを設定
plt.xlabel('BlockSize*log(Number of nodes)[MB*log(nodes)]', fontsize=16)
if select == 1:
    plt.ylabel('block_propagation_time[s]', fontsize=16)
if select == 2:
    plt.ylabel('fork_probability[%]', fontsize=16)

# 対数目盛でx軸を表示
plt.xscale('log')
#両対数にする
plt.yscale('log')

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 凡例を表示
plt.legend(fontsize=14)

# グリッドを表示
plt.grid(True)

# グラフをファイルに保存する
plt.savefig('comparison.png', dpi=300)

# グラフを表示
plt.show()
