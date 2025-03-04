# config.py
from pathlib import Path
import matplotlib.pyplot as plt

class Config:
    SAVE_PLOT = True  # 全局控制是否保存图片
    SHOW_PLOT = False  # 全局控制是否显示窗口
    OUTPUT_DIR = Path('output')
    PLOT_STYLE = {
        'figure.figsize': (12, 4),
        'font.size': 12,
        'axes.prop_cycle': plt.cycler(color=['#2c7bb6','#d7191c','#fdae61'])
    }
    
    @classmethod
    def initialize(cls):
        cls.OUTPUT_DIR.mkdir(exist_ok=True)
        plt.style.use('seaborn')
        plt.rcParams.update(cls.PLOT_STYLE)