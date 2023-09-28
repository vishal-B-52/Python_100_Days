# Docstrings in Python: -

"""
Python string literals that appear after definition of a function, class or module areDocstrings. The below given
function 'average' is given a docstring that explains how the function works.

A DocString is not a comment. A comment can be made anywhere in function. Docstrings are specially written just
after function declaration and just before variable declaration or any function related code. In short, before your
start writing code into function, make a docstring.

DocStrings can be written in single and double quotes just like comments which is the only special characteristics.
Thus, string in 'average' classifies as a docstring while printer one is a mere comment
and will return 'None' as output. Docstring can be a word, statement, single line, multi line, paragraph, essay based on
how you chose to describe the function.

Docstring never become part of output until .__doc__ attribute is used.
"""


def average(*args):
    """Takes numbers and returns their average"""
    sum = 0
    for i in args:
        sum += i
    return f"{sum / len(args):.2f}"


def sum(*summ):
    add = 0
    for i in summ:
        add += i
    '''This function takes numbers and adds them'''
    return sum


# print(average(13, 45, 44, 20, 90, 78))

# The __doc__ attribute is given to every function in python to print it's docstring.
# Use function name.__doc__ to get its docstring.
print(average.__doc__)
print(sum.__doc__)


"""
PEP 8 is a document that provides guidelines and best practices on how to write a python code. It's purpose was 
to increase readability and consistency in a python code. Written in 2001 by Guido Von Rossum, Nick Coghlan and Barry
Warsaw.

PEP = Python Enhancement Proposal. There are several of such PEP. PEP also describe features introduced in Python and 
document aspects of python like design and style.

To see one of such PEP 'Zen of python' (written by Tim Peters with 19 aphorisms) in your PC, write 'import this' 
in a cmd/powershell.
"""


