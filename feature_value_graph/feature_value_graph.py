import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#場合分け 
select = 5

# x軸の値と対応する複数のy軸の値（1MBの場合 ※他のブロックサイズの場合も概ね同じ値であった)
x_values = [10, 100, 1000, 10000]
if select == 1:
    y_values_set = [43, 862, 8639, 86450]  # 辺数
if select == 2:
    y_values_set = [8.6, 17.24, 17.278, 17.29]  # 平均次数
if select == 3:
    y_values_set = [2, 3, 4, 5]  # 直径
if select == 4: 
    y_values_set = [0.961111111111111, 0.18640144200136113, 0.01721248413241548, 0.00179337682213734]  # 平均クラスタ係数
if select == 5:
    y_values_set = [1.0444444444444445, 1.8682828282828283, 2.725025025025025, 3.550706190619062] # 平均頂点間距離

# 折れ線グラフを作成
plt.figure(figsize=(8, 6))

# データセットをプロット
plt.plot(x_values, y_values_set, marker='o', linestyle='-', color='b')

# x軸とy軸のラベルとタイトルを設定
plt.xlabel('Number of nodes[nodes]', fontsize=16)
if select == 1:
    plt.ylabel('Number of edges', fontsize=16)
if select == 2:
    plt.ylabel('average degree', fontsize=16)
if select == 3:
    plt.ylabel('diameter', fontsize=16)
if select == 4:
    plt.ylabel('average Clustering Coefficient', fontsize=16)
if select == 5:
    plt.ylabel('average vertex distance', fontsize=16)

# 対数目盛でx軸を表示
plt.xscale('log')
#両対数にする(辺数と平均クラスタ係数のみ)
if select == 1 or select == 4:
    plt.yscale('log')
# x軸の目盛りを指定された値に設定
plt.xticks(x_values, x_values)  

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# 凡例を表示
# plt.legend(fontsize=14)

# グリッドを表示
plt.grid(True)

# グラフをファイルに保存する
if select == 1:
    plt.savefig('Number_of_edges.png', dpi=300)
if select == 2:
    plt.savefig('average_degree.png', dpi=300)
if select == 3:
    plt.savefig('diameter.png', dpi=300)
if select == 4:
    plt.savefig('average_Clustering_Coefficient.png', dpi=300)
if select == 5:
    plt.savefig('average vertex distance.png', dpi=300)

# グラフを表示
plt.show()
