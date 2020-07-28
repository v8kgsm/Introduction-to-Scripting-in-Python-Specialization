# Week 3 Quiz, Question 7
"""
Collatz Conjucture: Consider the simple function f(n)f(n) 
(as defined in the Wikipedia page above) that takes an integer 
nn and divides it by two if nn is even and multiplies nn by 33 and 
then adds one to the result if nn is odd. 
"""

def f(n):
    if n % 2 == 0:
        return n/2
    elif n % 2 == 1:
        return (n * 3) + 1

print(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071)))))))))))))))