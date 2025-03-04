# save_utils.py
import h5py

def save_signal_hdf5(filename, t, signal, metadata):
    """存储为HDF5格式"""
    with h5py.File(filename, 'w') as f:
        f.create_dataset('time', data=t)
        f.create_dataset('signal', data=signal)
        for key, val in metadata.items():
            f.attrs[key] = val