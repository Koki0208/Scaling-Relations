import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import numpy as np
from math import log

#場合分け　値はノード数
select = 10

# データセット(x_values...ブロックサイズ y_values_set1...フォーク確率(%表記))
x_values = [0.2, 0.5, 1, 10, 100, 1000]
if select == 10:
    y_values_set1 = [0.09990, 0.09990, 0.00000, 0.29910, 0.79365, 3.75361]  # データセット1
if select == 100:
    y_values_set1 = [0.39841, 0.09990, 0.29910, 0.39841, 3.47490, 15.48223]  # データセット1
if select == 1000:
    y_values_set1 = [0.09990, 0.00000, 0.09990, 0.19960, 2.43902, 16.20487]  # データセット1
if select == 10000:
    y_values_set1 = [0.19960, 0.29910, 0.39841, 0.29910, 3.19767, 16.87448]  # データセット1

#非線形フィッティング　Pfork = (1 - e^(-λ*B*log(n))) 100を掛けているのは%表記にするため  Pfork...フォーク確率B...ブロックサイズ,n...ノード数
#nonlinear_fit → 式(5) nonlinear_fit[1,2] → 式A,式B
array_x = np.array(x_values)
array_y = np.array(y_values_set1)
if select == 10:
    def nonlinear_fit(x, a, b):
        return  100*(1 - np.exp(-a*x*log(10)-b))
    param, cov = curve_fit(nonlinear_fit, array_x, array_y)
    def nonlinear_fit1(x, a, b):
        return  100*(1 - np.exp(-a*x*10-b))
    param1, cov1 = curve_fit(nonlinear_fit1, array_x, array_y)
    def nonlinear_fit2(x, a, b):
        return  100*(1 - np.exp(-a*x*10*log(10)-b))
    param2, cov2 = curve_fit(nonlinear_fit2, array_x, array_y)
if select == 100:
    def nonlinear_fit(x, a, b):
        return  100*(1 - np.exp(-a*x*log(100)-b))
    param, cov = curve_fit(nonlinear_fit, array_x, array_y)
    def nonlinear_fit1(x, a, b):
        return  100*(1 - np.exp(-a*x*100-b))
    param1, cov1 = curve_fit(nonlinear_fit1, array_x, array_y)
    def nonlinear_fit2(x, a, b):
        return  100*(1 - np.exp(-a*x*100*log(100)-b))
    param2, cov2 = curve_fit(nonlinear_fit2, array_x, array_y)
if select == 1000:
    def nonlinear_fit(x, a, b):
        return  100*(1 - np.exp(-a*x*log(1000)-b))
    param, cov = curve_fit(nonlinear_fit, array_x, array_y)
    def nonlinear_fit1(x, a, b):
        return  100*(1 - np.exp(-a*x*1000-b))
    param1, cov1 = curve_fit(nonlinear_fit1, array_x, array_y)
    def nonlinear_fit2(x, a, b):
        return  100*(1 - np.exp(-a*x*1000*log(1000)-b))
    param2, cov2 = curve_fit(nonlinear_fit2, array_x, array_y)
if select == 10000:
    def nonlinear_fit(x, a, b):
        return  100*(1 - np.exp(-a*x*log(10000)-b))
    param, cov = curve_fit(nonlinear_fit, array_x, array_y)
    def nonlinear_fit1(x, a, b):
        return  100*(1 - np.exp(-a*x*10000-b))
    param1, cov1 = curve_fit(nonlinear_fit1, array_x, array_y)
    def nonlinear_fit2(x, a, b):
        return  100*(1 - np.exp(-a*x*10000*log(10000)-b))
    param2, cov2 = curve_fit(nonlinear_fit2, array_x, array_y)

# 予測値を計算
y_fit = nonlinear_fit(array_x, *param)
y_fit1 = nonlinear_fit1(array_x, *param1)
y_fit2 = nonlinear_fit2(array_x, *param2)

# 平均二乗誤差を計算(上から式5,式A,式B)
mse = np.mean((array_y - y_fit) ** 2)
mse1 = np.mean((array_y - y_fit1) ** 2)
mse2 = np.mean((array_y - y_fit2) ** 2)
print(mse)#0.01923924919127595 #0.35394919597058166 #0.05832578244365024 #0.188395207027893
print(mse1)#0.019239249191280467 #9370.266830213779 #9409.991405076215 #9340.279776834566
print(mse2)#0.019239249191276068 #9370.26687960985 #9409.991405076215 #9340.279776834566

# 折れ線グラフを作成
plt.figure(figsize=(8, 6))

# データセット1をプロット
plt.plot(x_values, y_values_set1, marker='o', linestyle='-', color='b', label='fork probability')

#非線形フィッティング(式5)をプロット
list_y = []
if select == 10:
    for num in array_x: 
        list_y.append(100*(1 - np.exp(-param[0]*num*log(10)-param[1])))
if select == 100:
    for num in array_x: 
        list_y.append(100*(1 - np.exp(-param[0]*num*log(100)-param[1])))
if select == 1000:
    for num in array_x: 
        list_y.append(100*(1 - np.exp(-param[0]*num*log(1000)-param[1])))
if select == 10000:
    for num in array_x: 
        list_y.append(100*(1 - np.exp(-param[0]*num*log(10000)-param[1])))
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
if select == 10:
    plt.savefig('line-graph_nonlinear_fitting_10node.png', dpi=300)
if select == 100:
    plt.savefig('line-graph_nonlinear_fitting_100node.png', dpi=300)
if select == 1000:
    plt.savefig('line-graph_nonlinear_fitting_1000node.png', dpi=300)
if select == 10000:
    plt.savefig('line-graph_nonlinear_fitting_10000node.png', dpi=300)

# グラフを表示
plt.show()
