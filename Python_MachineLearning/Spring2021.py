from ast import Str
from cmath import sqrt
from statistics import *
import toolbox_extended as te
import toolbox_02450 as tb
import numpy as np
import pandas as pd
from exam_toolbox import *
import re
import os
from math import exp
from scipy.integrate import quad

pca = pca_calc()
class exam:

    # ----------------------------------------------- OPG 1-----------------------------------------------
    def opg1():

        return "E"

    # ----------------------------------------------- OPG 2-----------------------------------------------
    def opg2():
        diag_values = [126.15,104.44,92.19,75.07,53.48]
        pca.draw_curve_from_diagonal_values(diag_values)
        # Can also be done by:
        pca.var_explained(diag_values)
        return "E"
    #print(opg2())
    # ----------------------------------------------- OPG 3-----------------------------------------------
    def opg3():

        return "E"

    # ----------------------------------------------- OPG 4-----------------------------------------------
    def opg4():

        return "E"

    # ----------------------------------------------- OPG 5-----------------------------------------------
    def opg5():
        
        x2 = [39.0, 415.0, -7.0,  -6727.0,  143.0]
        x3 = [-0.0,  -7.0,  1.0,    108.0,   -2.0]
        cov = -7.0
        var2 = 415.0
        var3 = 1.0
        res = (cov)/sqrt(var2*var3)
        print("res: ", res)
        
        # The empirical covariance matrix:
        #               x2       x3
        #       143.0   39.0    −0.0    253.0     142.0
        # x2    39.0   (415.0) (−7.0)  −6727.0    143.0
        # x3   −0.0    (−7.0)   (1.0)   108.0    −2.0
        #       253.0  −6727.0   108.0  370027.0 −1403.0
        #       142.0   143.0   −2.0   −1403.0    171.0
        # 
        # cov[x2,x3] = -7.0
        # var_x2     = 415.0
        # var_x3     = 1.0
        #  
        
        return "C"
    #print(opg5())
    # ----------------------------------------------- OPG 6-----------------------------------------------
    def opg6():
        data = [[ 0. ,  5. ,  7.7,  6.1,  4.2, 11. ,  7.3,  9. , 11.3,  1.4],
                [ 5. ,  0. ,  5.4,  4. ,  7.5,  7.9,  5.3,  6.8, 11.9,  3.5],
                [ 7.7,  5.4,  0. ,  5.2,  7.2,  6.1,  7.8,  6.7, 12.9,  6.4],
                [ 6.1,  4. ,  5.2,  0. ,  5.1,  5.4,  8.4,  3.3,  8.1,  4.8],
                [ 4.2,  7.5,  7.2,  5.1,  0. ,  8.7,  8.8,  6.6,  7.7,  4.1],
                [11. ,  7.9,  6.1,  5.4,  8.7,  0. , 12. ,  4.2,  9.3,  9.8],
                [ 7.3,  5.3,  7.8,  8.4,  8.8, 12. ,  0. , 11. , 16.3,  6.7],
                [ 9. ,  6.8,  6.7,  3.3,  6.6,  4.2, 11. ,  0. ,  6.2,  7.8],
                [11.3, 11.9, 12.9,  8.1,  7.7,  9.3, 16.3,  6.2,  0. , 10.4],
                [ 1.4,  3.5,  6.4,  4.8,  4.1,  9.8,  6.7,  7.8, 10.4,  0. ]]
        labels = []
        for i in range(1, 11):
            s = "O" + str(i)
            labels.append(s)
        #print(labels)
        df = pd.DataFrame(data)
        K = 2       # K nearest neighbors
        obs = 2     # O3
        sim = anomaly()
        #print(df.loc["O3", :].values)
        sim.ARD(df, obs, K)
        # The density for observation O3 is 0.18867924528301885 
        # average relative density for observation O3 is 0.6979857215706273
        # So the ARD is approx. 0.7
        return "A"
    #opg6()
    # ----------------------------------------------- OPG 7-----------------------------------------------
    def opg7():
        data = [[ 0. ,  5. ,  7.7,  6.1,  4.2, 11. ,  7.3,  9. , 11.3,  1.4],
                [ 5. ,  0. ,  5.4,  4. ,  7.5,  7.9,  5.3,  6.8, 11.9,  3.5],
                [ 7.7,  5.4,  0. ,  5.2,  7.2,  6.1,  7.8,  6.7, 12.9,  6.4],
                [ 6.1,  4. ,  5.2,  0. ,  5.1,  5.4,  8.4,  3.3,  8.1,  4.8],
                [ 4.2,  7.5,  7.2,  5.1,  0. ,  8.7,  8.8,  6.6,  7.7,  4.1],
                [11. ,  7.9,  6.1,  5.4,  8.7,  0. , 12. ,  4.2,  9.3,  9.8],
                [ 7.3,  5.3,  7.8,  8.4,  8.8, 12. ,  0. , 11. , 16.3,  6.7],
                [ 9. ,  6.8,  6.7,  3.3,  6.6,  4.2, 11. ,  0. ,  6.2,  7.8],
                [11.3, 11.9, 12.9,  8.1,  7.7,  9.3, 16.3,  6.2,  0. , 10.4],
                [ 1.4,  3.5,  6.4,  4.8,  4.1,  9.8,  6.7,  7.8, 10.4,  0. ]]
        #print(labels)
        df = pd.DataFrame(data)
        clu=cluster()
        clu.dendro_plot(df,"complete", sort="descending")
        # First: O1 and O10
        # Sec: O4 and O8
        # Third: O5 and {O1, O10}
        # Fourth: O2 and O7
        # Fifth: O6 and {O4, O8}
        # Sixth: O3 and {O4, O6, O8}
        # Seventh: {O2, O7} and {O1, O5, O10}
        
        # Answer is Dendrogram 1. Can be seen at O5 and {O1, O10}



        return "A"
    #opg7()
    # ----------------------------------------------- OPG 8-----------------------------------------------
    def opg8():
        # M -> dimensions (M >= 4)
        # x1 -> first two elem are 1, rest are 0
        # x2 -> fist M/2 elem are 1, rest are 0
        # Test 1
        M = 6
        x1 = [1,1,0,0,0,0]     
        x2 = [1,1,1,0,0,0]
#            Measure     Value
#        0      Rand  0.666667
#        1   Jaccard  0.444444
        clu = cluster()
        sim = similarity()
        #clu.cluster_similarity(x1,x2)
        sim.measures(x1,x2)
        print("*"*40)
        print("*"*40)
        print("A: ", 4/M)
        print("B: ", ((1/2)*M)/((1/2)*M + 2))
        print("C: ", 2/M)
        print("D: ", 2/((1/2)*M - 2))
        print("*"*40)
        print("*"*40)
        print("*"*40)
        # Test 2
        
        M2 = 16
        x3 = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]     
        x4 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
#        
        sim.measures(x3,x4)
        print("*"*40)
        print("*"*40)
        print("A: ", 4/M2)
        t = (1/2)*M2
        n = (1/2)*M2 + 2
        print("B: ", t/n)
        print("C: ", 2/M2)
        n2 = (1/2)*M2 - 2
        print("D: ", 2/n2)
        '''
                   Measure     Value
        1  Jaccard  0.666667
        ****************************************
        A:  0.6666666666666666
        B:  0.6
        C:  0.3333333333333333
        D:  2.0
        ****************************************
        ****************************************
           Measure  Value
        1  Jaccard  0.250
        ****************************************
        A:  0.25
        B:  0.8
        C:  0.125
        D:  0.3333333333333333
        '''
        # The answer is A = 4/M
        return "A"
    #opg8()
    # ----------------------------------------------- OPG 9-----------------------------------------------
    def opg9():
        # Backwards selection: (M*(M + 1) / 2) + 1
        # M was given as: 
        M = 8
        res = 1 + M+M -1
        # Sooo wtf... Fucking ML bs course
        
        print("res = ", res)
        return "E"
    opg9()
    # ----------------------------------------------- OPG 10-----------------------------------------------
    def opg10():

        return "E"

    # ----------------------------------------------- OPG 11-----------------------------------------------
    def opg11():

        return "E"

    # ----------------------------------------------- OPG 12-----------------------------------------------
    def opg12():

        return "E"

    # ----------------------------------------------- OPG 13-----------------------------------------------
    def opg13():

        return "E"

    # ----------------------------------------------- OPG 14-----------------------------------------------
    def opg14():

        return "E"

    # ----------------------------------------------- OPG 15-----------------------------------------------
    def opg15():

        return "E"

    # ----------------------------------------------- OPG 16-----------------------------------------------
    def opg16():

        return "E"

    # ----------------------------------------------- OPG 17-----------------------------------------------
    def opg17():

        return "E"

    # ----------------------------------------------- OPG 18-----------------------------------------------
    def opg18():

        return "E"

    # ----------------------------------------------- OPG 19-----------------------------------------------
    def opg19():

        return "E"

    # ----------------------------------------------- OPG 20-----------------------------------------------
    def opg20():

        return "E"

    # ----------------------------------------------- OPG 21-----------------------------------------------
    def opg21():

        return "E"

    # ----------------------------------------------- OPG 22-----------------------------------------------
    def opg22():

        return "E"

    # ----------------------------------------------- OPG 23-----------------------------------------------
    def opg23():

        return "E"

    # ----------------------------------------------- OPG 24-----------------------------------------------
    def opg24():

        return "E"

    # ----------------------------------------------- OPG 25-----------------------------------------------
    def opg25():

        return "E"

    # ----------------------------------------------- OPG 26-----------------------------------------------
    def opg26():

        return "E"

    # ----------------------------------------------- OPG 27-----------------------------------------------
    def opg27():

        return "E"

    # -------------------------------- answers dataframe -------------------------------------------------
    def answers(show=True, csv=False, excel=False):
        ans = pd.DataFrame(
            columns=["Student number: s174852"]
        )  # columns = ["OPG", "svar"])

        ans.loc[0] = ""
        ans.loc[1] = "Q01: {}".format(exam.opg1())
        ans.loc[2] = "Q02: {}".format(exam.opg2())
        ans.loc[3] = "Q03: {}".format(exam.opg3())
        ans.loc[4] = "Q04: {}".format(exam.opg4())
        ans.loc[5] = "Q05: {}".format(exam.opg5())
        ans.loc[6] = "Q06: {}".format(exam.opg6())
        ans.loc[7] = "Q07: {}".format(exam.opg7())
        ans.loc[8] = "Q08: {}".format(exam.opg8())
        ans.loc[9] = "Q09: {}".format(exam.opg9())
        ans.loc[10] = "Q10: {}".format(exam.opg10())
        ans.loc[11] = ""

        ans.loc[12] = "Q11: {}".format(exam.opg11())
        ans.loc[13] = "Q12: {}".format(exam.opg12())
        ans.loc[14] = "Q13: {}".format(exam.opg13())
        ans.loc[15] = "Q14: {}".format(exam.opg14())
        ans.loc[16] = "Q15: {}".format(exam.opg15())
        ans.loc[17] = "Q16: {}".format(exam.opg16())
        ans.loc[18] = "Q17: {}".format(exam.opg17())
        ans.loc[19] = "Q18: {}".format(exam.opg18())
        ans.loc[20] = "Q19: {}".format(exam.opg19())
        ans.loc[21] = "Q20: {}".format(exam.opg20())
        ans.loc[22] = ""

        ans.loc[23] = "Q21: {}".format(exam.opg21())
        ans.loc[24] = "Q22: {}".format(exam.opg22())
        ans.loc[25] = "Q23: {}".format(exam.opg23())
        ans.loc[26] = "Q24: {}".format(exam.opg24())
        ans.loc[27] = "Q25: {}".format(exam.opg25())
        ans.loc[28] = "Q26: {}".format(exam.opg26())
        ans.loc[29] = "Q27: {}".format(exam.opg27())

        if excel:
            ans.to_excel(re.sub(".py", "_answers.xlsx", __file__), index=False)
        if csv:
            ans.to_csv(re.sub(".py", "_answers.csv", __file__), index=False)
        if show:
            print(ans)

        return ans


#exam.answers()
