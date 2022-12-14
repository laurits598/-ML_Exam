import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

def questionsToFile(n):
    with open(r"C:\Users\lauri\Desktop\Machine-Learning\Exam\Fall2016_Problems.txt", "w") as f:
        for i in range(1,n+1):
            f.write("Question {0}: ".format(i))
            user_input = input("Enter your note for question {0}: ".format(i))
            f.write(user_input + "\n")
        print("File written successfully!")
#questionsToFile()

def writeToFile():
    with open(r"C:\Users\lauri\Desktop\Machine-Learning\Exam\Fall2016_Problems.txt", "w") as f:
        f.write("Problem 1: \n")
        f.write("Problem 2: \n")
        f.write("Problem 3: \n")
        f.write("Problem 4: \n")

        user_input = input("Enter your problem: ")
        f.write(user_input + "\n")
        print("File written successfully!")
#writeToFile()

def clearFile():
    #Create a copy of the file
    shutil.copyfile(r"C:\Users\lauri\Desktop\Machine-Learning\Exam\Fall2016_Problems.txt", r"C:\Users\lauri\Desktop\Machine-Learning\Exam\Fall2016_Problems_Backup.txt")

    #Open the original file and delete the content
    with open(r"C:\Users\lauri\Desktop\Machine-Learning\Exam\Fall2016_Problems.txt", "w") as f:
        f.write("")

    print("File cleared successfully!")


def makeVariables():
    n = int(input("Enter the number of variables: "))
    for i in range(1, n+1):
        exec("Q" + str(i) + " = 0")
    print("Variables created")

def initStart():
     user_in = int(input("Enter the amount of questions: "))
     questionsToFile(user_in)
     return 0
#initStart()


