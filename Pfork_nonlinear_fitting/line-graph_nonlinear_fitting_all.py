import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import numpy as np
from math import log

# データセット(x_values...ブロックサイズ y_values_set...フォーク確率(%表記)[1,2,3,4]...[10,100,1000,10000])
x_values = [0.2, 0.5, 1, 10, 100, 1000]
y_values_set1 = [0.09990, 0.09990, 0.00000, 0.29910, 0.79365, 3.75361]  # データセット1
y_values_set2 = [0.39841, 0.09990, 0.29910, 0.39841, 3.47490, 15.48223]  # データセット2
y_values_set3 = [0.09990, 0.00000, 0.09990, 0.19960, 2.43902, 16.20487]  # データセット3
y_values_set4 = [0.19960, 0.29910, 0.39841, 0.29910, 3.19767, 16.87448]  # データセット4

array_x = np.array(x_values)
array_y1 = np.array(y_values_set1)
array_y2 = np.array(y_values_set2)
array_y3 = np.array(y_values_set3)
array_y4 = np.array(y_values_set4)

#非線形フィッティング　Pfork = (1 - e^(-λ*(αB*log(n)+β)) 100を掛けているのは%表記にするため  Pfork...フォーク確率B...ブロックサイズ,n...ノード数
def nonlinear_fit1(x, a, b):
    return  100*(1 - np.exp(-a*x*np.log(10)-b))
param1, cov1 = curve_fit(nonlinear_fit1, array_x, array_y1)
def nonlinear_fit2(x, a, b):
    return  100*(1 - np.exp(-a*x*np.log(100)-b))
param2, cov2 = curve_fit(nonlinear_fit2, array_x, array_y2)
def nonlinear_fit3(x, a, b):
    return  100*(1 - np.exp(-a*x*np.log(1000)-b))
param3, cov3 = curve_fit(nonlinear_fit3, array_x, array_y3)
def nonlinear_fit4(x, a, b):
    return  100*(1 - np.exp(-a*x*np.log(10000)-b))
param4, cov4 = curve_fit(nonlinear_fit4, array_x, array_y4)

# 折れ線グラフを作成
plt.figure(figsize=(8, 6))

# データセット1をプロット
plt.plot(x_values, y_values_set1, marker='o', linestyle='-', color='b', label='10node')
plt.plot(x_values, y_values_set2, marker='o', linestyle='-', color='r', label='100node')
plt.plot(x_values, y_values_set3, marker='o', linestyle='-', color='g', label='1000node')
plt.plot(x_values, y_values_set4, marker='o', linestyle='-', color='m', label='10000node')

#非線形フィッティングをプロット
list_y1 = []
for num in array_x:
    list_y1.append(100*(1 - np.exp(-param1[0]*num*np.log(10)-param1[1])))
list_y2 = []
for num in array_x:
    list_y2.append(100*(1 - np.exp(-param2[0]*num*np.log(100)-param2[1])))
list_y3 = []
for num in array_x:
    list_y3.append(100*(1 - np.exp(-param3[0]*num*np.log(1000)-param3[1])))
list_y4 = []
for num in array_x:
    list_y4.append(100*(1 - np.exp(-param4[0]*num*np.log(10000)-param4[1])))
#両対数プロット
plt.loglog(array_x, np.array(list_y1), marker="", color='navy', label='nonlinear fitting(10node)')
plt.loglog(array_x, np.array(list_y2), marker="", color='tomato', label='nonlinear fitting(100node)')
plt.loglog(array_x, np.array(list_y3), marker="", color='darkolivegreen', label='nonlinear fitting(1000node)')
plt.loglog(array_x, np.array(list_y4), marker="", color='purple', label='nonlinear fitting(10000node)')

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
plt.savefig('line-graph_nonlinear_fitting_all.png', dpi=300)

# グラフを表示
plt.show()
