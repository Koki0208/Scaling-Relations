import matplotlib.pyplot as plt
import numpy as np
import math  # 数学関数を使用するために追加


delay_list = []

infilename = 'result_out.txt'
end_flag = False
with open(infilename, 'r') as infile:
    for line in infile:
        data_list = line.replace('\n', '').split(',')
        if len(data_list) == 2:
            if end_flag == False:
                end_flag = True
            data_list_old = data_list
        else:
            if end_flag == True:
                if data_list_old == ['Deprecated Gradle features were used in this build', ' making it incompatible with Gradle 8.0.']:
                       end_flag = False
                       break
                delay = int(data_list_old[1])*0.001
                delay_list.append(delay)
                end_flag = False

with open('pow_block_time.csv', 'w') as outfile:
    for delay in delay_list:
        outfile.write("%f\n" % delay)

#ブロック伝搬時間の抽出 (抽出を行う際はnew_delay_listに切り替える #1)
#new_delay_list = []
#for delay in delay_list:
#    if delay >= 100.0:
#        if delay <= 250.0:
#            new_delay_list.append(delay)
#print(delay_list)
#print(len(delay_list))
#111111111111111111111111111111111111111111111111111111111111111111111111111111111
count, bins, patches = plt.hist(delay_list, 30, density=True)
#count, bins, patches = plt.hist(new_delay_list, 30, density=True)
#111111111111111111111111111111111111111111111111111111111111111111111111111111111

# 各棒の上に数値を表示
#for rect, c in zip(patches, count):
#    height = rect.get_height()
#    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{c:.2f}', ha='center', va='bottom')

# xとyの範囲を取得
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()

# テキストを表示する位置を設定 (右上隅)
x_pos_average = x_max * 0.70
y_pos_average = y_max * 0.85
x_pos_SD = x_max * 0.70
y_pos_SD = y_max * 0.75

#ここから平均と標準偏差を求めるプログラム
#平均
i = 0
#blockheight = 10000
#11111111111111111111111111111111111111111111111111111111111111111111111111111111
for delay in delay_list:
#for delay in new_delay_list:
#11111111111111111111111111111111111111111111111111111111111111111111111111111111
    int_delay = float(delay)
    i += int_delay

#average = i / blockheight
#11111111111111111111111111111111111111111111111111111111111111111111111111111111
average = i / len(delay_list)
#average = i / len(new_delay_list)
#11111111111111111111111111111111111111111111111111111111111111111111111111111111
print("平均:", average)
plt.text(x_pos_average, y_pos_average, f'average{average:.5f}s', color='black', fontsize=14)

#標準偏差
j = 0
#1111111111111111111111111111111111111111111111111111111111111111111111111111111
for delay in delay_list:
#for delay in new_delay_list:
#1111111111111111111111111111111111111111111111111111111111111111111111111111111
    int_delay = float(delay)
    j += (int_delay - average) ** 2

#1111111111111111111111111111111111111111111111111111111111111111111111111111111
std_dev = math.sqrt(j / len(delay_list))
#std_dev = math.sqrt(j / len(new_delay_list))
#1111111111111111111111111111111111111111111111111111111111111111111111111111111
print("標準偏差:", std_dev)
plt.text(x_pos_SD, y_pos_SD, f'std_dev{std_dev:.5f}s', color='black', fontsize=14)

#ガンベル分布
beta = std_dev * np.sqrt(6) / np.pi
mu = average - 0.57721*beta
plt.plot(bins, (1/beta)*np.exp(-(bins - mu)/beta)* np.exp( -np.exp( -(bins - mu) /beta) ), linewidth=2, color='r', label='Gumbel Distribution')

# ラベルの設定
plt.xlabel('block_propagation_time[s]', fontsize=14)
plt.ylabel('Density', fontsize=14)

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=10)

plt.legend()

plt.savefig('pow_block_time_2.png')
plt.clf()
