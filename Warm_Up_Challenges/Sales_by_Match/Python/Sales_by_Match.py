#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Return the total number of pairs of socks
    
    all_socks = dict()
    
    for sock in ar:
        if sock in all_socks:
            all_socks[sock] += 1
        else:
            all_socks[sock] = 1

    total_sock_pairs = 0
    for color in all_socks:
        total_sock_pairs += all_socks[color] // 2

    return total_sock_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
