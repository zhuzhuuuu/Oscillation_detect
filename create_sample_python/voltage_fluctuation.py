# voltage_fluctuation.py 
def add_voltage_sag(signal, sag_start, sag_duration, sag_depth):
    """添加电压暂降特征"""
    modified = signal.copy()
    start_idx = int(sag_start*len(signal))
    end_idx = start_idx + int(sag_duration*len(signal))
    modified[start_idx:end_idx] *= (1 - sag_depth)
    return modified