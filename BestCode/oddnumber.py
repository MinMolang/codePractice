#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    # Write your code here
    # l = even, r = even
    if l%2==0:
        s = l+1
    else:
        s = l
    if r%2==0:
        return list(range(s,r,2))
    else:
        return list(range(s,r+1,2))

if __name__ == '__main__':
 pass