import sys 
import os
from maths.math_op import MathOperation 

math = MathOperation()


3
a = int(input("'EEnter the number to perform operation "))
b = int(input("'EEnter the number to perform operation "))

op = input('Please the operator to operate ')

if op == '+':
    result = math.add(a,b)
    print("This is a result of addition",result)
elif op == '/':
    result = math.div(a,b)
    print("This is a result of divsion",result)