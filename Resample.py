import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
import skimage.transform as skTrans
from matplotlib.patches import Rectangle
from matplotlib.transforms import Bbox
import os
from polyaxon_client.tracking import Experiment

#from sklearn.utils import resample
from functions import *

def resample_bb(new_sampling,path):

    ####################
    ### Resampling
    ####################

    resample_folder = [str(item) for item in new_sampling]
    resample_folder = "".join(resample_folder)
    resample_folder = str(int(resample_folder))
    print(resample_folder)
            
    # create folder Resampling
    if not os.path.exists(path + "/Resample"):
        os.makedirs(path + "/Resample")
    if not os.path.exists(path + "/Resample/"+resample_folder):
        os.makedirs(path + "/Resample/"+resample_folder)

    dirname = path+"/Original"
    files = os.listdir(dirname)
    print(files.size)
    for i in files:        

        path_vol = dirname+"/"+i
       
        # Read NIFTI imgs
        volume = sitk.ReadImage(path_vol)

        # Resample Imgs
        vol_ct_isotropic = resample_img(volume, new_sampling)
        
        sitk.WriteImage(vol_ct_isotropic, path + "/Resample/"+resample_folder+"/"+i)
        
        


# ---------------------
# RUN Resampling and bounding box
# ---------------------
path = "C:/Users/Natalia/Documents/01. Master/2022-WS/02. CS/04. Dataset/01. Liver and Tumor/LITS - Challenge/Training" #'MICCAI/Samples'
# experiment = Experiment()
# data_paths = experiment.get_data_paths()

# files = os.listdir(data_paths['data1']+path)

#resample_bb(new_sampling = [1,1,1], path = data_paths['data1']+path, files=files,outbound = 2)
resample_bb(new_sampling = [1,1,1], path = path)