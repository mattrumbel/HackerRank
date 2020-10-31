#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    numClouds = len(c)
    total_jumps = 0
    currCloud = 0

    while (currCloud < len(c) - 1):
        if (currCloud + 2) < numClouds and c[currCloud + 2] == 0:
            currCloud += 2
        elif (currCloud + 1) < numClouds and c[currCloud + 1] == 0:
            currCloud += 1
        
        total_jumps += 1
    
    return total_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
