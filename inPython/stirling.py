'''
Implementation of Stirling's Equation for approximating factorials for n
numbers
'''

import math

def stirling(val):
    first_half = math.sqrt(2*3.14*val)
    sec_half = val**val/2.718**val
    complete = first_half*sec_half
    return complete

if __name__ == '__main__':
    number = int(input('Enter number: '))

print(stirling(number))
