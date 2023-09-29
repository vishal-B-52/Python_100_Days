# Set -

"""
Sets are unordered collection of data items. unlike list, tuple and dictionary, sets are the only collections in Python
that store and display items in random order. They allow heterogeneous type and amount of items like any other
collections in Python.

Sets are usually declared with curly braces '{}'. Problem is that the curly braces are used for dictionaries too.
So if user enters only key=value entries, it becomes a dict but if there are only single element entries, it becomes a
set. What about a blank curly braced collection though? In such case, the variable type will be Dictionary only if when
user meant it to be set. A better way to declare set in that manner would be to use '{()}' which clarifies Python about
its type. Another way is how we declare tuples. Just do {"",} or {""} to declare a set.

Another Simpler way is to use set() method and assign it to a variable.

Sets are collection which do not allow duplicate entries. Do not allow means even if you enter number '45' 7 times in
the set visually, at the time of output 45 will be displayed only once. Random order makes it difficult to use index and
access a particular element.
"""
# setter = {()}
# print(type(setter))

# setter = {}
# print(type(setter))

# setget = set()
# print(type(setget))
setget = {""}
print(type(setget))

# setter = {"Vishal", True, 2.344, 5 + 5j, 'c'}
# print(setter)

# Accessing sets through for loop: -
# for i in setter:
#     print(i, end=" ")
