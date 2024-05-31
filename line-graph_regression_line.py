import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#データセット(x_values...ノード数 y_values_set1...平均ブロック伝搬時間 y_values_set2...標準偏差)
x_values = [10, 100, 1000, 10000]
y_values_set1 = [1.8992457542457537, 4.152063745019917, 5.2181327345309425, 6.835490547263678]  # データセット1
y_values_set2 = [0.669432181851424, 1.7718874758325578, 1.9182055646280383, 2.562563763101399]  # データセット2

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
plt.text(200, 4, f'Regression Line (α: {linear[0]:.3f}, β: {linear[1]:.3f})', color='black', fontsize = 14)

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
plt.savefig('block_delay_graph.png', dpi=300)

# グラフを表示
plt.show()
