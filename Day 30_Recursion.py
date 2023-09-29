# Recursion :-

"""
A function calling itself is called as Recursion. It's just like two physical world mirrors placed in front of each
other which will produce images recursively.

Significant use of a recursion on beginner level can be seen in a Factorial function where function repeatedly calls
itself till the base condition is satisfied.

A recursive function is made up of two cases: -
1. Base case - if condition mostly which stops recursion
2. Recursive case - else condition that resumes recursion
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(4))

"""
The above function goes as follows:
4 * factorial(4 - 1) --> 3 * factorial(3 - 1) --> 2 * factorial(2 - 1) <-- 1 returned from base case as n==1 from next 
                                                                            function call 
                                                            |
                                                            |
     4*6             <--         3*2          <--         2 * 1
     |
     |
     24
"""
