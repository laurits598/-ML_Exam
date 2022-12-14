import numpy as np
import pandas as pd


def Q15():
    data = [[1,1,1,1,0,1],
              [0,0,0,0,0,0],
              [1,1,0,1,0,0],
              [0,1,1,0,1,0],
              [1,1,1,1,1,1],
              [0,0,0,0,0,0],
              [1,1,0,1,0,0],
              [0,1,1,0,1,0],
              [1,1,1,1,0,1],
              [0,1,1,0,1,0],
              [0,0,0,0,0,0],
              [1,1,0,1,0,0],
              [0,1,1,0,1,0],
              [0,1,1,0,1,0]]
    labelY = ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","P14"]
    labelX = ["x1","x2","x3","x4","x5","y"]
    M = np.matrix(data)
    labels = ["P1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9"]
    df = pd.DataFrame(M, index=labelY, columns=labelX)
    print(df)
    print(data[0][:])






