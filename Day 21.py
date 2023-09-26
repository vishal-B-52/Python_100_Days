# Function Arguments: -

# Function arguments are the arguments that are passed by user to the function
# to resume its working.
# Four types of function arguments: -
# 1. Default Args
# 2. Keyword Args
# 3. Required Arguments
# 4. Variable length args


# default arguments don't mind whether value is being passed by user or not
# It will use the value defaulted to it by the programmer and use it.
# If user passes value, then the default value is not considered for calculation.
def defaulter(c, a=8, b=1, ):  # a and b are assigned with default value
    print("Average is", a + b + c)


# Always provide non-default param(c) before default param(a, b). It is convenient and right logic according to
# IDEs cause if you don't follow the order (like putting c in between of a and b), you might have to end up
# providing all params just to get the function to understand which value belongs to which param.

# For ex:- In this case, we are testing execution of function with default args where we need to provide only c.
# Putting c anywhere after a or b will require you to provide value of args that come before c as Python accepts param
# for arguments in the order which is mentioned in function definition. According to definition of
# defaulter(a=9, c, b=12), You should provide value of 'a' first and then value of 'c' just to be clear about
# which value belongs to the place where param of 'c' is supposed to be.

# defaulter(90)
# defaulter(2)  # Automatically assumes 8 and 1 for a and b
# defaulter(3, 4)  # a is set to 4 and b will be assumed as 1 since it is not provided.
# defaulter(2, 9, 3)  # Both default values will be masked by given values.

# Keyword args: - Importance of Keyword args is that, you can directly mention the args while equating it to
# a parameter in any order irrelevant to the function definition.
# While doing this, params & args should not violate function definition (like mentioning extra arg which do not exist)
# and also, no arg should be mentioned twice. For ex:- putting f=7 and 9 at the place of 'f' arg in same function call.
def intel(d, e, f):
    print("Average =", d + e + f / 3)


# intel(3, 5, 7)  # Params are provided to d, e and f according to function definition.
# intel(e=0, d=6, f=4)   # Params are assigned to d, e and f according to keyword arguments.
# intel(d=6, f=4, 5)    # Function definition violated as keyword arg 'f' and positional arg 'f' are conflicting.

# Required args:- These args are declared in the function definition. Such arguments should be provided with values
# They are also called non-default args which means in case we do not provide key=param syntax in function call, we
# need to provide appropriate param according to number of args and their positions which matches function definition.

def replica(x, y, z=10):
    print("Result =", x - y + z)


# replica(2, 4)  # while z is optional, x and y param depend upon user. Not providing these param yields exception.

# Variable length args: -
# a. Arbitrary args - When creating a function definition, rather than passing different args such as a, x, m, etc.
# pass '*<arg_name>'. This function definition accepts parameters by processing them in a tuple during function call.

def compress_this(*floater):  # Defined an arbitrary arg
    # If you want to print only specific args in the tuple, use indexing on the arbitrary arg.
    # for ex:- floater[0], floater[3] will return "hello" and 23.
    print(floater[0], floater[3])

    # If you want to see every param you passed, iterate over the arbitrary argument.
    for i in floater:
        print(i)


# The function call can contain any amount and type of params the user want to pass.
# compress_this("hello", 2.14, ['VISHAL', 'bawane'], 23)

# Keyword Arbitrary Args: - Same as Arbitrary arg but when creating a function pass '**<var_name>'.
# The previous one access in form of a tuple and this one access in form of dictionary.
# It's called Keyword Arb Argument cause keyword args follow the same 'arg=param' syntax when passed in function call.
def dictator(**bloke):  # Defining a keyword arbitrary argument
    print(bloke.keys())  # prints args passed
    print(bloke.values())  # prints params passed
    print(bloke['lname'], ['height'])  # Printing only specific parameters

# This function call should be in a key=value syntax since arbitrary arg works like a dictionary.
# dictator(name="Vishal", height="180cm", Weight=70, lname="Bawane")

# return statement - returns a vale once function call ends. To catch the value, assign a variable to the function call
# or simply print it like a statement using print() function.
# If you do not use a return statement and catch value from function call, it would be 'None' (NoneType class)
