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
count, bins, patches = plt.hist(delay_list, 30, density=False)

# 各棒の上に数値を表示
for rect, c in zip(patches, count):
   height = rect.get_height()
   plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{c:.0f}', ha='center', va='bottom')

#ここから平均と標準偏差を求めるプログラム
#平均
i = 0
for delay in delay_list:
    int_delay = float(delay)
    i += int_delay
average = i / len(delay_list)
print("平均:", average)
plt.text(0.6, 0.95, f'average{average:.5f}s', transform=plt.gca().transAxes, color='black', fontsize=14, verticalalignment='top')

#標準偏差
j = 0
for delay in delay_list:
    int_delay = float(delay)
    j += (int_delay - average) ** 2
std_dev = math.sqrt(j / len(delay_list))
print("標準偏差:", std_dev)
plt.text(0.6, 0.85, f'std_dev{std_dev:.5f}s', transform=plt.gca().transAxes, color='black', fontsize=14, verticalalignment='top')

# ラベルの設定
plt.xlabel('block_propagation_time[s]', fontsize=14)
plt.ylabel('frequency', fontsize=14)

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=10)

plt.savefig('analyze_block_time.png')
plt.clf()
