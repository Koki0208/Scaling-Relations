import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
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

#ブロック伝搬時間の抽出(0.2MB...4~6s) 
new_delay_list = []
for delay in delay_list:
   if delay >= 4.0:
       if delay <= 6.0:
           new_delay_list.append(delay)
count, bins, patches = plt.hist(new_delay_list, 30, density=True)

#ここから平均と標準偏差を求めるプログラム
#平均
i = 0
for delay in new_delay_list:
    int_delay = float(delay)
    i += int_delay
average = i / len(new_delay_list)
print("平均:", average)
plt.text(0.6, 0.70, f'average{average:.5f}s', transform=plt.gca().transAxes, color='black', fontsize=14, verticalalignment='top')

#標準偏差
j = 0
for delay in new_delay_list:
    int_delay = float(delay)
    j += (int_delay - average) ** 2
std_dev = math.sqrt(j / len(new_delay_list))
print("標準偏差:", std_dev)
plt.text(0.6, 0.60, f'std_dev{std_dev:.5f}s', transform=plt.gca().transAxes, color='black', fontsize=14, verticalalignment='top')


#確率分布関数
#ガンベル分布
def gumbel(x, mu, eta):
    return (1/eta) * np.exp( -(x-mu)/eta ) * np.exp( - np.exp( -(x-mu)/eta ) )
#正規分布
def normal(x, mu, sigma):
    return (1 / (np.sqrt(2*np.pi) * sigma)) * np.exp( - ((x - mu)**2 / (2*(sigma**2))) )
#フレシェ分布
def frechet(x, mu, eta, alpha):
    return (alpha / eta) * np.power( ((x-mu) / eta), -1-alpha ) * np.exp( - np.power( ((x-mu) / eta), -alpha) )
#指数分布
def exponential(x, l):
    return l * np.exp(- l * x)


# ヒストグラムを描画
bins_mod = []
for i in range(len(bins)-1):
    bins_mod.append( (bins[i] + bins[i+1])/2 )
#ガンベル分布
p0 = [1, 1]
popt, pcov = curve_fit(gumbel, bins_mod, count, p0=p0)
#print('gumbel:', popt, pcov)
gumbel_x_fit = np.linspace(min(bins_mod), max(bins_mod), 30)
gumbel_y_fit = gumbel(gumbel_x_fit, *popt)
plt.plot(gumbel_x_fit, gumbel_y_fit, label='fitted gumbel dist.')
gumbel_error_tmp = 0.0
gumbel_log_likelihood = 0.0
for i in range(len(count)):
    # 対数尤度を計算
    gumbel_log_likelihood += np.log(gumbel_y_fit[i])
    # 平均二乗誤差を計算
    gumbel_error_tmp += (count[i] - gumbel_y_fit[i])**2
print('gumbel mean squared error:', np.sqrt(gumbel_error_tmp))#0.4615428722745656
#正規分布
#p0 = [1, 1]
p0 = [10, 1]
popt, pcov = curve_fit(normal, bins_mod, count, p0=p0)
#print('normal:', popt, pcov)
normal_x_fit = np.linspace(min(bins_mod), max(bins_mod), 30)
normal_y_fit = normal(normal_x_fit, *popt)
plt.plot(normal_x_fit, normal_y_fit, label='fitted normal dist.')
normal_error_tmp = 0.0
for i in range(len(count)):
    normal_error_tmp += (count[i] - normal_y_fit[i])**2
print('normal mean squared error:', np.sqrt(normal_error_tmp))#0.6321805663532972
#フレシェ分布
p0 = [1, 1, 1]
popt, pcov = curve_fit(frechet, bins_mod, count, p0=p0)
#print('frechet:', popt, pcov)
frechet_x_fit = np.linspace(min(bins_mod), max(bins_mod), 30)
frechet_y_fit = frechet(frechet_x_fit, *popt)
plt.plot(frechet_x_fit, frechet_y_fit, label='fitted frechet dist.')
frechet_error_tmp = 0.0
frechet_log_likelihood = 0.0
for i in range(len(count)):
    # 対数尤度を計算
    frechet_log_likelihood += np.log(frechet_y_fit[i])
    # 平均二乗誤差を計算
    frechet_error_tmp += (count[i] - frechet_y_fit[i])**2
print('frechet mean squared error:', np.sqrt(frechet_error_tmp))#0.45380346795363347
#指数分布
p0 = [1]
popt, pcov = curve_fit(exponential, bins_mod, count, p0=p0)
#print('exponential:', popt, pcov)
exponential_x_fit = np.linspace(min(bins_mod), max(bins_mod), 30)
exponential_y_fit = exponential(exponential_x_fit, *popt)
plt.plot(exponential_x_fit, exponential_y_fit, label='fitted exponential dist.')
exponential_error_tmp = 0.0
for i in range(len(count)):
    exponential_error_tmp += (count[i] - exponential_y_fit[i])**2
print('exponential mean squared error:', np.sqrt(exponential_error_tmp))#2.7141347982363895

# ガンベル分布のAIC,BIC
n = len(count)
k = 2
gumbel_aic = 2 * k - 2 * gumbel_log_likelihood
gumbel_bic = np.log(n) * k - 2 * gumbel_log_likelihood
# フレシェ分布のAIC,BIC
l = 3
frechet_aic = 2 * l - 2 * frechet_log_likelihood
frechet_bic = np.log(n) * l - 2 * frechet_log_likelihood
print('gumbel_AIC:', gumbel_aic)#62.93402592058966
print('frechet_AIC:', frechet_aic)#64.43243566954146
print('gumbel_BIC:', gumbel_bic)#65.73642068391398
print('frechet_BIC:', frechet_bic)#68.63602781452792

# ラベルの設定
plt.xlabel('block_propagation_time[s]', fontsize=14)
plt.ylabel('Density', fontsize=14)

# 目盛りのフォントサイズを大きくする
plt.xticks(fontsize=14)
plt.yticks(fontsize=10)

plt.legend()

plt.savefig('newGumbel.png')
plt.clf()
