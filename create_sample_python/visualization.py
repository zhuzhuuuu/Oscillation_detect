# visualization.py
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def plot_signal(t, signal, title, save_path=None, show=False):
    """
    通用信号可视化函数
    
    参数:
        t (np.ndarray): 时间序列
        signal (np.ndarray): 信号数据
        title (str): 图像标题
        save_path (str/Path): 图片保存路径，None则不保存
        show (bool): 是否显示图像窗口
    返回:
        matplotlib.figure.Figure: 生成的图像对象
    """
    fig = plt.figure(figsize=(12, 4))
    
    # 主波形图
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(t, signal, color='#2c7bb6', linewidth=1)
    ax1.set_xlabel('Time (s)', fontsize=12)
    ax1.set_ylabel('Amplitude (pu)', fontsize=12)
    ax1.set_title(f'{title} - Time Domain', fontsize=14)
    
    # 频谱图
    ax2 = fig.add_subplot(1, 2, 2)
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(t), t[1]-t[0])
    ax2.semilogy(freqs[:len(freqs)//2], np.abs(fft[:len(freqs)//2]), 
                color='#d7191c', linewidth=1)
    ax2.set_xlabel('Frequency (Hz)', fontsize=12)
    ax2.set_ylabel('Magnitude', fontsize=12)
    ax2.set_title(f'{title} - Frequency Domain', fontsize=14)
    
    plt.tight_layout()
    
    if save_path:
        Path(save_path).parent.mkdir(exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    if not show:
        plt.close(fig)  # 不显示则关闭图形
    
    return fig