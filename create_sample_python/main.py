# main.py
from gen_base_signal import generate_base_signal
from power_fluctuation import add_power_fluctuation
from voltage_fluctuation import add_voltage_sag
from visualization import plot_signal
import matplotlib.pyplot as plt

# 存储所有图形对象
figures = []

# ===== 生成基频信号 =====
t, base = generate_base_signal(duration=10, fs=1000, freq=50)
fig_base = plot_signal(t, base, 'Base Signal', save_path='output/base.png')
figures.append(fig_base)

# ===== 添加功率波动 =====
power_fluctuated = add_power_fluctuation(base, fluctuation_factor=0.1)
fig_power = plot_signal(t, power_fluctuated, 
                       'With Power Fluctuation', 
                       save_path='output/power.png')
figures.append(fig_power)

# ===== 添加电压暂降 =====
final_signal = add_voltage_sag(power_fluctuated, 
                             sag_start=0.5, 
                             sag_duration=0.1,
                             sag_depth=0.3)
fig_final = plot_signal(t, final_signal, 
                       'Final Signal', 
                       save_path='output/final.png')
figures.append(fig_final)

# ===== 统一显示所有图像 =====
# 重新激活所有图形
for fig in figures:
    plt.figure(fig.number)

# 非阻塞显示
plt.show(block=False)

# 保持程序运行（按回车退出）
input("Press Enter to exit...")

# 清理资源
plt.close('all')