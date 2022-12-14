from lib2to3.pytree import generate_matches
import numpy as np

# Example from Q2 Spring 2018:

string = "13.5 0 0 0 0 0 0 7.6 0 0 0 0 0 6.5 0 0 0 0 0 0 5.8 0 0 0 0 0 0 3.5 0 0 0 0 0 0 2.0"

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass
lines = "\n".join(lines)

print(lines)

def genArr(string,):
    arr = [ x for x in string.split(' ') ]
    newArr = []
    print(newArr)
    for string in arr:
        c = '.'
        if c in string:
            newArr.append(float(string))
        else:
            newArr.append(int(string))

    print(newArr)
    return newArr

#genArr(string)

