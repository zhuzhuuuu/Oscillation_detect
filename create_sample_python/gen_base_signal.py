# gen_base_signal.py
import numpy as np
from visualization import plot_signal
from config import Config

def generate_base_signal(duration, fs, freq, show_plot=False):
    """
    生成基频信号并可选可视化
    
    参数:
        duration (float): 信号时长（秒）
        fs (int): 采样率（Hz）
        freq (float): 基频（Hz）
        show_plot (bool): 是否显示图像
        
    返回:
        t (np.ndarray): 时间序列
        signal (np.ndarray): 信号数据
    """
    t = np.linspace(0, duration, int(fs * duration))
    signal = np.sin(2 * np.pi * freq * t)
    
    if Config.SAVE_PLOT or show_plot:
        plot_signal(
            t, signal,
            title=f'Base Signal {freq}Hz',
            save_path=Config.OUTPUT_DIR/f'base_{freq}Hz.png',
            show=show_plot
        )
    
    return t, signal