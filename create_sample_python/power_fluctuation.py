# power_fluctuation.py
import numpy as np
def add_power_fluctuation(signal, fluctuation_factor):
    """添加功率波动特征"""
    return signal * (1 + fluctuation_factor*np.random.randn(len(signal)))