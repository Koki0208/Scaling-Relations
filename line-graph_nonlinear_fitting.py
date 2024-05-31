import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import numpy as np
from math import log

# データセット(x_values...ブロックサイズ y_values_set1...フォーク確率(%表記))
x_values = [0.2, 0.5, 1, 10, 100, 1000]
y_values_set1 = [0.19960, 0.29910, 0.39841, 0.29910, 3.19767, 16.87448]  # データセット1

#非線形フィッティング　Pfork = (1 - e^(-λ*B*n)) 100を掛けているのは%表記にするため  Pfork...フォーク確率B...ブロックサイズ,n...ノード数
array_x = np.array(x_values)
array_y = np.array(y_values_set1)
def nonlinear_fit(x, a, b):
    return  100*(1 - np.exp(-a*x*b))
param, cov = curve_fit(nonlinear_fit, array_x, array_y)

# 折れ線グラフを作成
plt.figure(figsize=(8, 6))

# データセット1をプロット
plt.plot(x_values, y_values_set1, marker='o', linestyle='-', color='b', label='fork probability')

#非線形フィッティングをプロット
list_y = []
for num in array_x: 
    list_y.append(100*(1 - np.exp(-param[0]*num*param[1])))
#両対数プロット
plt.loglog(array_x, np.array(list_y), marker="", color='k', label='nonlinear fitting')

# x軸とy軸のラベルとタイトルを設定
plt.xlabel('Block size[MB]', fontsize=16)
plt.ylabel('fork probability[%]', fontsize=16)

# 対数目盛でx軸を表示
plt.xscale('log')
#両対数にする
plt.yscale('log')
plt.xticks(x_values, x_values)  # x軸の目盛りを指定された値に設定

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 凡例を表示
plt.legend(fontsize=14)

# グリッドを表示
plt.grid(True)

# グラフをファイルに保存する
plt.savefig('fork_probability_graph_logarithm.png', dpi=300)

# グラフを表示
plt.show()
