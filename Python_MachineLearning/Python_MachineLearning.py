import Clustering as cluster
import Probability as prob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from scipy.cluster.hierarchy import dendrogram
import scipy.cluster.hierarchy as sch






#print(df)
def viewData():
    data_dict = {'O1': [0, 0.534, 1.257, 1.671, 1.090, 1.315, 1.484, 1.253, 1.418],
             'O2': [0.534, 0, 0.727, 2.119, 1.526, 1.689, 1.214, 0.997, 1.056],
             'O3': [1.257, 0.727, 0, 2.809, 2.220, 2.342, 1.088, 0.965, 0.807],
             'O4': [1.671, 2.119, 2.809, 0, 0.601, 0.540, 3.135, 2.908, 3.087],
             'O5': [1.090, 1.526, 2.220, 0.601, 0, 0.331, 2.563, 2.338, 2.500],
             'O6': [1.315, 1.689, 2.342, 0.540, 0.331, 0, 2.797, 2.567, 2.708],
             'O7': [1.484, 1.214, 1.088, 3.135, 2.563, 2.797, 0, 0.275, 0.298],
             'O8': [1.253, 0.997, 0.965, 2.908, 2.338, 2.567, 0.275, 0, 0.343],
             'O9': [1.418, 1.056, 0.807, 3.087, 2.500, 2.708, 0.298, 0.343, 0]}
    labels = ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"]
    labelsX_axis = ['O1','O2','O3','O4','O5','O6','O7','O8','O9']
    labelsY_axis = ['O1','O2','O3','O4','O5','O6','O7','O8','O9']

    df = pd.DataFrame(data_dict, index=labelsX_axis, columns=labelsY_axis)
    category = ['Kama','Rosa','Canadian']
   

    #df = pd.DataFrame(data_dict, index=labelsX_axis, columns=labelsY_axis)
    #df = pd.DataFrame(data_dict, index=labels, columns=labels)



    print(df)
#viewData()





