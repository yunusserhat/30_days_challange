#Day 0
input_string = input()
print('Hello, World.')
print(input_string)

#Day 1
i = 4
d = 4.0
s = 'HackerRank '

i_ys = int(input())
d_ys = float(input())
s_ys = input()

print(i + i_ys)
print(d + d_ys)
print(s + s_ys)

#Day 2

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):

    total_cost =  meal_cost + meal_cost * tip_percent/100 + meal_cost * tax_percent/100
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

