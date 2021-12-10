import pydicom
import numpy as np 
from matplotlib import pyplot as plt 
from glob import glob
import pandas as pd
import seaborn as sns
data = sorted(glob("stage_2_images/*.dcm")) # create a list containing paths to all files
# For the convenience of analysis, we will create a dataframe with metadata
patients = []
for t in data:
    data = pydicom.dcmread(t)
    patient = {}
    patient["UID"] = data.SOPInstanceUID 
    patient["Age"] = data.PatientAge 
    patient["Sex"] = data.PatientSex 
    patient["Modality"] = data.Modality 
    patient["BodyPart"] = data.BodyPartExamined 
    patient["ViewPosition"] = data.ViewPosition 
    patients.append(patient)
    df_patients = pd.DataFrame(patients, columns=["UID", "Age", "Sex", "Modality", "BodyPart", "ViewPosition"])
    df_patients["Age"] = pd.to_numeric(df_patients["Age"])
# Let's make a histogram
sorted_ages = np.sort(df_patients["Age"].values) 
plt.style.use('seaborn-whitegrid') 
plt.figure(figsize=(15, 5))
plt.hist(sorted_ages[:-2], bins=[i for i in range(100)]) 
plt.title("Distribution by age", fontsize=18, pad=10) 
plt.xlabel("Age", labelpad=10)
plt.xticks([i*10 for i in range(11)]) 
plt.ylabel("Count", labelpad=10) 
plt.show()
plt.savefig('output/box.png')