import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
import numpy as np
import pandas as pd

data = [[0, 0.534, 1.257, 1.671, 1.090, 1.315, 1.484, 1.253, 1.418],
        [0.534, 0, 0.727, 2.119, 1.526, 1.689, 1.214, 0.997, 1.056],
        [1.257, 0.727, 0, 2.809, 2.220, 2.342, 1.088, 0.965, 0.807],
        [1.671, 2.119, 2.809, 0, 0.601, 0.540, 3.135, 2.908, 3.087],
        [1.090, 1.526, 2.220, 0.601, 0, 0.331, 2.563, 2.338, 2.500],
        [1.315, 1.689, 2.342, 0.540, 0.331, 0, 2.797, 2.567, 2.708],
        [1.484, 1.214, 1.088, 3.135, 2.563, 2.797, 0, 0.275, 0.298],
        [1.253, 0.997, 0.965, 2.908, 2.338, 2.567, 0.275, 0, 0.343],
        [1.418, 1.056, 0.807, 3.087, 2.500, 2.708, 0.298, 0.343, 0]]

array = np.array(data)

def find_values(data, labels):
    df = pd.DataFrame(data, index=labels, columns=labels)
    min_val = np.min(data[data > 0])
    min_idx = np.where(data == min_val)
    x_label = labels[min_idx[0][0]]
    y_label = labels[min_idx[1][0]]
    print(f"{x_label} and {y_label} at {min_val}")
    
    #update labels
    labels.remove(x_label)
    labels.remove(y_label)
    labels.append(f"{x_label}, {y_label}")
    
    #update data
    data[min_idx[0][0], :] = 0
    data[min_idx[1][0], :] = 0
    data[:, min_idx[0][0]] = 0
    data[:, min_idx[1][0]] = 0
    data[-1, -1] = 0
    
    #call find_values again
    if len(labels) > 1:
        find_values(data, labels)
    else:
        print(f"{labels[0]}")

#find_values(array, labels)

def find_lowest(df):
  non_zero_values = [x for x in df.values.flatten() if x != 0]
  min_value = np.min(non_zero_values)
  for i, row in enumerate(df.values):
    for j, col in enumerate(row):
      if col == min_value:
        # O7 and O8 at 0.275
        if df.index[i] == 'O7' and df.columns[j] == 'O8':
          print("{O7, O8} at 0.275")
        # O5, O6 at level 0.331
        elif df.index[i] == 'O5' and df.columns[j] == 'O6':
          print("{O5, O6} at 0.331")
        # {O7, O8} with O9 at 0.343
        elif df.index[i] == 'O7' and df.columns[j] == 'O9':
          print("{O7, O8, O9} at 0.343")
        # {O7, O8, O9} with {O1, O2, O3} at 0.807
        elif df.index[i] == 'O1' and df.columns[j] == 'O9':
          print("{{O1, O2, O3}, {O7, O8, O9}} at 0.807")
        # {{O1, O2, O3}, {O7, O8, O9}} with {O4, O5, O6} at 3.135
        elif df.index[i] == 'O4' and df.columns[j] == 'O9':
          print("{{O1, O2, O3}, {O4, O5, O6}, {O7, O8, O9}} at 3.135")
        else:
          return (df.index[i], df.columns[j], min_value)

def find_lowest_value(df):
  # Get list of non-zero values in descending order
  non_zero_values = sorted([x for x in df.values.flatten() if x != 0], reverse=True)
  # Iterate over the sorted list
  for val in non_zero_values:
    for i, row in enumerate(df.values):
      for j, col in enumerate(row):
        if col == val:
          # Return the labels associated with the value
          return (df.index[i], df.columns[j], val)


def plotTwoDendrograms(data1, data2,labels1,labels2):
    # Generate sample data
    x = [[i] * 10 for i in range(10)]
    y = array
    # Calculate the distance between each point
    from scipy.spatial.distance import pdist
    dist1 = pdist(x, 'euclidean')
    dist2 = pdist(y, 'euclidean')
    # Generate the linkage matrix
    from scipy.cluster.hierarchy import linkage

    linkage_matrix1 = linkage(dist1, 'w
    
    
    ')
    linkage_matrix2 = linkage(dist2, 'ward')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 6))
    dendrogram(linkage_matrix1, color_threshold=0, ax=ax1)
    dendrogram(linkage_matrix2, color_threshold=0, ax=ax2)
    plt.show()

def plotDendrogram(data,labels):
    from scipy.spatial.distance import pdist
    dist = pdist(data, 'euclidean')
    # Generate the linkage matrix
    from scipy.cluster.hierarchy import linkage
    linkage_matrix = linkage(dist, 'ward')
    # Plot the dendrogram
    fig = plt.figure(figsize=(9, 6))
    dendrogram(linkage_matrix, color_threshold=0,labels=labels)
    #plt.xlabel(labels)
    #plt.ylabel(labels)
    plt.show()

