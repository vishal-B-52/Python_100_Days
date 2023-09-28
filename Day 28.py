# f-strings in python -

# Traditional string formatting in Python -
# Usually format(variable=value/variable[with declared value]) method is used on a string to format it in a manner.
# format can accept variables with string, int, float values. To format such variable and their values into the
# string, {} should be used at the required places. These curly braces can contain a variable name or index of that
# variable.

# format() method has a limitation where if there is only one variable to be substituted, it has to be declared or
# assigned value inside the method only (see the below examples). If there are multiple variables, they can be either
# declared first or assigned value in method itself (see the multiple variable example).

# tzt = "I am a {criteria} boy"
# print(tzt.format(criteria="fat"))

# txt = "I have a change for {xxx} dollars"
# print(txt.format(xxx=25))

# .2f is used for float-point numbers. Number after/before decimal determines how many digits to display in result.
# It usually rounds off value accordingly. Result should be 87.46 kg if this format used.

# txt3 = "My weight is {weight:.2f} kg"
# print(txt3.format(weight=87.459999))


# format() method can take multiple variables and substitute them in give order. Number of curly braces and variables in
# format() method should match else program yields IndexError Exception.

# Talking about order, the order in which variables should be formatted can be changed by mentioning index of variable.
# 1st variable in format method gets the 0th index and it increments for next variable. This index can be put in curly
# braces (in the string) to format a particular variable at particular space.

# str1 = "My name is {} and I live in {}."
# str2 = "My name is {0} and I live in {2}. My age is {1}."
# name = "Vishal"
# city = "Amravati"
# age = 18
# height = 159.24
# print(str1.format(name, city))
# print(str2.format(name, city, height))


# f-strings:-

# F-strings in python make it easy to format a variable in a string without use of additional method. It has same syntax
# as format() where you are required to mention curly braces and inside that variable names to get a formatted string.

# Of course, the variables can be either declared and assigned value in string or before that. The braces can contain a
# simple float/string/int/char value without an actual variable need at the place.

# To make a string an f-string, just put an f before a string. f-string also support arithmetic expressions in curly
# braces. Using type() on such string returns class 'str' as result.

# If you want to display the braces as well (may be part of documentation), enclose the brace into
# another pair of braces. ({{var_name}}) this prints '{var_name}' while being in f-string.

cricketer = "Vijay Shekhawat"
centuries = 4
wickets = 15
strike_rate = 134.5677
print(f"{{cricketer}} is a player who has {centuries} centuries and {wickets} wickets in only {10} matches with "
      f"strike rate of {strike_rate:.1f}.")

