# coding: utf-8
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys

#1000.txtを開く
infilename = '1000.txt'
with open(infilename, 'r') as infile:
  node_list = []
  edge_list = []
  for line in infile:
    node_list.append( line.split()[0] )
    node_list.append( line.split()[1] )
    edge_list.append( (line.split()[0],line.split()[1]) ) 

G = nx.Graph()
# 頂点の追加
for node_id in node_list:
  G.add_node( node_id )
# 辺の追加
for edge_pair in edge_list:
  G.add_edge( edge_pair[0], edge_pair[1] )
# print(G.number_of_nodes()) # 頂点数の表示
# print(G.number_of_edges()) # 辺数の表示
# print(nx.is_connected(G)) # 連結性の確認

# 最大連結成分を調べる(本研究ではネットワークは連結しているため意味はない(GをSGにする必要なし))
max_size = 0
for c in list(nx.connected_components(G)):
  if nx.number_of_nodes(G.subgraph(c)) > max_size:
    SG = G.subgraph(c)
    max_size = nx.number_of_nodes(SG)
print("頂点数:", SG.number_of_nodes()) # 頂点数の表示
print("辺数:", SG.number_of_edges()) # 辺数の表示
print("平均次数:", np.average(list(dict(nx.degree(SG)).values()))) # 平均次数の表示
print("ネットワークの直径", nx.diameter(SG))
print("平均クラスタ係数:", nx.average_clustering(SG)) # 平均クラスタ係数の表示
print("平均頂点間距離:", nx.average_shortest_path_length(SG)) # 平均頂点間距離の表示
# print("連結性:", nx.is_connected(SG)) # 連結性の確認
nx.draw(SG, node_size=5) # ネットワークを描画
plt.savefig("Network_structure.png")

