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

#Day 3
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    if N%2!=0:
        print('Weird')
    elif N%2==0 and N in range(1,6):
        print('Not Weird')
    elif N%2==0 and N in range(5,21):
        print('Weird')
    elif N%2==0 and N>20:
        print('Not Weird')

#Day 4
class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young.")
        elif age >= 13 and age < 18:
            print("You are a teenager.")
        else:
            print('You are old.')

    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age = age + 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


#Day 5
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)

