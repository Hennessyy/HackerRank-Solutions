#Python If-Else HackerRank solution
#!/bin/python3

import math
import os
import random
import re
import sys
'''
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to 2,5 print Not Weird
If n is even and in the inclusive range of  to 6,20 print Weird
If n is even and greater than 20, print Not Weird

'''


if __name__ == '__main__':
    n = int(input().strip())

    if 1 <= n <= 100:
        if n % 2 == 1 or n % 2 == 0 and n in range (6,21):
            print("Weird")
        elif n % 2 == 0 and (n in range (2,6) or n > 20 ):
            print("Not Weird")
        else:
            print("Not Weird")


