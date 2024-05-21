import h5py
f = h5py.File(model_final_2_1.h5,'r')
for item in f.keys():
    print(item)