# tuples -
tuplesh = (25, "tuples", "Lokesh", 3.226, 5, 'K', 15)
tups = (23, 'V', "Stringer", 4.56, 56, 23.23, True)
# Tuples are one of the sequence datatypes such as List. They can store many elements with heterogeneous datatype in
# the same collection.
# tuples are type of collection which are immutable. Thus, no insert(), remove() or append() can be used on a tuple.
# If you still want to perform operation on elements of tuple, convert it into a list, do the changes and then convert
# back to tuple.
# tuplesh = (25, "tuples", "Lokesh", 3.226, 5, 'K', 15)
# print(tuplesh)
# conv = list(tuplesh)
# conv.append(55j)
# conv[7] = "Replacement"
# print(conv)
# tuplesh = tuple(conv)
# print(tuplesh)

# Declaring a tuple - Take an identifier and assign it simple brackets with few elements or use tuple() method to
# declare a tuple without an element.

# Note: - If tuple is being declared with only one element without using tuple() method, better put
# more than one item in the tuple or if it is just going to be only one element,
# then put a comma(,) right after first element.

# In the first case the tuple is not considered tuple if there is only one element followed by a comma.
# Python interpreter treats a t=(5) and t=5 same as it treats if '(i>5)' and 'if i>5' the same.
# Simple brackets on one element do not make it a collection in Python. You need something that makes Interpreter
# understand that there are more elements to come in the simple bracket. Hence, the comma.
# Thus, type/class of variables with only one simple bracketed element have any other datatype (int/str/float etc.
# totally depends on first element) than expected 'tuple' datatype.
# In given example, tups is not considered a tuple but 't' is. tups needs a comma after first element like tupes.
# tups = (5)
# tupes = (5,)
# t = tuple()
# print(type(tups))
# print(type(tupes))
# print(type(t))
