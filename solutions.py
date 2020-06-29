#Python If-Else HackerRank solution
#!/bin/python3

import math
import os
import random
import re
import sys
"""
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to 2,5 print Not Weird
If n is even and in the inclusive range of  to 6,20 print Weird
If n is even and greater than 20, print Not Weird




if __name__ == '__main__':
    n = int(input().strip())

    if 1 <= n <= 100:
        if n % 2 == 1 or n % 2 == 0 and n in range (6,21):
            print("Weird")
        elif n % 2 == 0 and (n in range (2,6) or n > 20 ):
            print("Not Weird")
        else:
            print("Not Weird")





Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    print(a + b)
    print(a - b)
    print(a * b)
    
    
Task
Read two integers and print two lines. The first line should contain integer division,  // . The second line should contain float division,  / .

You don't need to perform any rounding or formatting operations.

    



if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(int(a / b))
    print(float(a / b)) 
    
Task
Read an integer . For all non-negative integers i < N , print i^2.  
     
    

if __name__ == '__main__':
    n = int(input())
    for i in range (0,n):
        print(i**2)


"""
# Operators test on HackerRank

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Complete the solve function below.
    def solve(meal_cost, tip_percent, tax_percent):
        answer = meal_cost + (meal_cost * (tip_percent / 100)) + (meal_cost * (tax_percent / 100))

        print(round(answer))
        return

meal_cost = float(input())

tip_percent = int(input())

tax_percent = int(input())

solve(meal_cost, tip_percent, tax_percent)