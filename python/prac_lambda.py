""" 람다식 (lambda)
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
"""
print('*' * 50)

# ex 1
x = lambda n : n + 10
print(x(5)) # 15

# ex 2
x = lambda a, b: a * b
print(x(3,3)) # 9


"""
Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number:
"""
print('*' * 50)

def myfunc(n: int):
    return lambda a: a * n

my_doubler = myfunc(n=2)
print(my_doubler(11)) # 22

my_tripler = myfunc(n=3)
print(my_tripler(11)) # 33
