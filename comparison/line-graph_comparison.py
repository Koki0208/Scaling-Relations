import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import numpy as np
from math import log

# ブロック伝搬時間は1,フォーク確率は2
select = 2

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

#スケーリング関係式 τfork = αBlog(n)+βにする (Blog(n)をxとしている)(τfork...ブロック伝搬時間B...ブロックサイズ,n...ノード数)
x_values1 = [value * log(10) for value in x_values]#10node
x_values2 = [value * log(100) for value in x_values]#100node
x_values3 = [value * log(1000) for value in x_values]#1000node
x_values4 = [value * log(10000) for value in x_values]#10000node

#比較対象 τfork = αBn + β...x1_values  τfork = αBnlog(n) + β...x2_values
x1_values1 = [value * 10 for value in x_values]
x1_values2 = [value * 100 for value in x_values]
x1_values3 = [value * 1000 for value in x_values]
x1_values4 = [value * 10000 for value in x_values]
x2_values1 = [value * 10*log(10) for value in x_values]
x2_values2 = [value * 100*log(100) for value in x_values]
x2_values3 = [value * 1000*log(1000) for value in x_values]
x2_values4 = [value * 10000*log(10000) for value in x_values]

#全てのデータセットを結合
if select == 1:
    all_x_values = np.concatenate([x_values2, x_values3, x_values4])
    all_x1_values = np.concatenate([x1_values2, x1_values3, x1_values4])
    all_x2_values = np.concatenate([x2_values2, x2_values3, x2_values4])
    all_y_values = np.concatenate([y_values_set2, y_values_set3, y_values_set4])
if select == 2:
    all_x_values = np.concatenate([x_values1, x_values2, x_values3, x_values4])
    all_x1_values = np.concatenate([x1_values1, x1_values2, x1_values3, x1_values4])
    all_x2_values = np.concatenate([x2_values1, x2_values2, x2_values3, x2_values4])
    all_y_values = np.concatenate([y_values_set1, y_values_set2, y_values_set3, y_values_set4])

# データをソート
sorted_indices = np.argsort(all_x_values)
sorted_scaled_x_values = all_x_values[sorted_indices]
sorted_indices1 = np.argsort(all_x1_values)
sorted_scaled_x1_values = all_x1_values[sorted_indices1]
sorted_indices2 = np.argsort(all_x2_values)
sorted_scaled_x2_values = all_x2_values[sorted_indices2]
sorted_all_y_values = all_y_values[sorted_indices]
sorted_all_y1_values = all_y_values[sorted_indices1]
sorted_all_y2_values = all_y_values[sorted_indices2]

#非線形フィッティング　τfork = αBlog(n)+β  τfork...ブロック伝搬時間B...ブロックサイズ,n...ノード数
def nonlinear_fit(x, a, b):
    return  a*x + b
param, cov = curve_fit(nonlinear_fit, sorted_scaled_x_values, sorted_all_y_values)
#非線形フィッティング 比較対象
def nonlinear_fit1(x, a, b):
    return  a*x + b
param1, cov1 = curve_fit(nonlinear_fit1, sorted_scaled_x1_values, sorted_all_y1_values)
def nonlinear_fit2(x, a, b):
    return  a*x + b
param2, cov2 = curve_fit(nonlinear_fit2, sorted_scaled_x2_values, sorted_all_y2_values)

# 予測値を計算
y_fit = nonlinear_fit(sorted_scaled_x_values, *param)
y_fit1 = nonlinear_fit1(sorted_scaled_x1_values, *param1)
y_fit2 = nonlinear_fit2(sorted_scaled_x2_values, *param2)

# 平均二乗誤差を計算
mse = np.mean((sorted_all_y_values - y_fit) ** 2)
mse1 = np.mean((sorted_all_y1_values - y_fit1) ** 2)
mse2 = np.mean((sorted_all_y2_values - y_fit2) ** 2)
print(mse)#4298.802996953852    #1.9885007458998052
print(mse1)#153524.29015326916    #16.528892554865305
print(mse2)#160879.2970513498  #17.055771075363168

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
array_y_fit = param[0] * sorted_scaled_x_values + param[1]
if select == 1:
    plt.loglog(sorted_scaled_x_values, np.array(array_y_fit), marker="", color='k', label='nonlinear fitting\n(except 10node)')
if select == 2:
    plt.loglog(sorted_scaled_x_values, np.array(array_y_fit), marker="", color='k', label='nonlinear fitting')

# フィッティング結果のパラメータを表示
fit_text = f"Fitting parameters:\na = {param[0]:.4f}\nb = {param[1]:.4f}"
plt.text(0.4, 0.95, fit_text, transform=plt.gca().transAxes, fontsize=16, verticalalignment='top')

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
if select == 1:
    plt.savefig('Scaling_Relations_propagation.png', dpi=300)
if select == 2:
    plt.savefig('Scaling_Relations_fork.png', dpi=300)

# グラフを表示
plt.show()
