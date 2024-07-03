import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#場合分け　値はブロックサイズ
select = 1000

#データセット(x_values...ノード数 y_values_set1...平均ブロック伝搬時間 y_values_set2...標準偏差)
x_values = [10, 100, 1000, 10000]
if select == 0.2:
    y_values_set1 = [1.8597475049900218, 3.315211940298508, 4.397545908183635, 5.288456630109671]  # データセット1
    y_values_set2 = [0.6447543445291268, 1.03327501834653, 1.3735194599911111, 1.4437305624846526]  # データセット2
if select == 0.5:
    y_values_set1 = [1.8868423153692662, 3.4799780439121726, 4.635616383616392, 6.1073874501992025]  # データセット1
    y_values_set2 = [0.7153470600018716, 1.2057554971382913, 1.4011928565583112, 1.8466625484938588]  # データセット2
if select == 1:
    y_values_set1 = [1.8992457542457537, 4.152063745019917, 5.2181327345309425, 6.835490547263678]  # データセット1
    y_values_set2 = [0.669432181851424, 1.7718874758325578, 1.9182055646280383, 2.562563763101399]  # データセット2
if select == 10:
    y_values_set1 = [2.6520667330677297, 15.764970149253735, 19.669640079760708, 25.203860557768895]  # データセット1
    y_values_set2 = [1.6369197668902222, 19.376104780496522, 16.619741509348334, 18.25651684645837]  # データセット2
if select == 100:
    y_values_set1 = [11.235130822596636, 110.9485988428157, 147.87546491228068, 205.95863213939984]  # データセット1
    y_values_set2 = [13.452985676503982, 126.89787472217165, 117.28263966253374, 142.80332544459546]  # データセット2
if select == 1000:
    y_values_set1 = [77.3540557692308, 1299.1862653721687, 1451.864203899267, 2067.7742869496856]  # データセット1
    y_values_set2 = [111.40393982960578, 2413.49485370497, 1494.0347265927176, 2013.3171625263456]  # データセット2
#回帰直線
x_values_np = np.array(x_values)
y_values_set_np = np.array(y_values_set1)
log_x = [np.log(i) for i in x_values_np]
linear = np.polyfit(log_x, y_values_set_np, 1)
y_linear = [linear[0] * x_linear1 + linear[1] for x_linear1 in log_x]

# 折れ線グラフを作成
plt.figure(figsize=(8, 6))

# データセット1をプロット
plt.plot(x_values, y_values_set1, marker='o', linestyle='-', color='b', label='average')

# データセット2をプロット
plt.plot(x_values, y_values_set2, marker='d', linestyle='-', color='g', label='SD')

#回帰直線のプロット
plt.plot(x_values_np, y_linear, linestyle="-", color='k', label='Regression Line')

# 直線の傾きと切片をグラフに表示する
plt.text(0.35, 0.35, f'Regression Line (α: {linear[0]:.3f}, β: {linear[1]:.3f})', transform=plt.gca().transAxes, color='black', fontsize = 14, verticalalignment='top')

# x軸とy軸のラベルとタイトルを設定
plt.xlabel('Number of nodes[nodes]', fontsize=16)
plt.ylabel('Block propagation time[s]', fontsize=16)

# 対数目盛でx軸を表示
plt.xscale('log')
plt.xticks(x_values, x_values)  # x軸の目盛りを指定された値に設定

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 凡例を表示
plt.legend(fontsize=14)

# グリッドを表示
plt.grid(True)

# グラフをファイルに保存する
if select == 0.2:
    plt.savefig('line-graph_regression_line_0.2MB.png', dpi=300)
if select == 0.5:
    plt.savefig('line-graph_regression_line_0.5MB.png', dpi=300)
if select == 1:
    plt.savefig('line-graph_regression_line_1MB.png', dpi=300)
if select == 10:
    plt.savefig('line-graph_regression_line_10MB.png', dpi=300)
if select == 100:
    plt.savefig('line-graph_regression_line_100MB.png', dpi=300)
if select == 1000:
    plt.savefig('line-graph_regression_line_1000MB.png', dpi=300)

# グラフを表示
plt.show()
