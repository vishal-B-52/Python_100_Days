# List : -
import sys

# List are python arrays that can store elements of heterogeneous type. That means elements of different class can
# co-exist.
# Lists are defined by square brackets or a variable can be converted to list class by list() method.
# Lists always store and print elements in given order.

lister = [3, 'V', 'vishal', 3 + 5j, True, 1.5674]
# l2 = []
# l1 = list()
# print(type(l2))
# print(type(l1))

# Indexing is useful to access particular element of a list.
# print(lister[1])
# print(lister[-1]) # Simplified form is len(lister)-1

# Check presence of items in list -
# 'in' can be used to check presence of element in list and string as well.
# 'not in' is used to check absence of elements.

# if "vishal" in lister:    # Works in both strings and lists.
#     print("hello")
#
# if (3+1/25)*0+3 not in lister:
#     # arithmetic expression can be used which is calculated first and presence of result is checked
#     print("Booyah")
# else:
#     print("Are mori maiyaa")

# if "is" in lister[2]:   # Check presence of substring in an element accessed by indexing. Works in strings.
#    print("yep")

# print(len(lister))    # Length of list

# Printing list elements in range -
# Lists can be indexed and sliced in list[start:end/stop:step] manner.

# print(lister[:])  # Prints whole list
# print(lister[2:500])  # Indexing in list and strings never gives IndexOutofBound error. Only in loops.
# print(lister[::-1])  # Easy way to reverse a list and print it

# Printing odd numbered index from index 1 to index 4 (len(lister) - 2) with increment of 2
# Thus printing element at indices 1 and 3 only.
# print(lister[1:-2:2])

# Works the same where range is 5:1 which is not traversable (returns [], same results in strings & for loop) unless
# list is reversed. Use of negative step solves problem. Elements with index 1 (len - 1 rule) and even indices are
# skipped.
# print(lister[-1:-5:-2])

# List Comprehension - Generating a list on the fly without declaring it
# Useful if you want to directly create a result where execution creates a list.
# A list comprehension requires an expression inside square brackets
# A usual list comp can be attained by [(expression) <loop with condition> <if-else condition>]
# However, this syntax can change if 'multiple if' or 'nested if' or 'if-else' or nested for loop statements
# are introduced.

# lst = [i for i in range(5)]   # Simple list comp to prepare a list of numbers from 0 to 4.
# print(lst)

# This one preps a list of numbers whose self-multiplication when divided with 2, results in remainder of 0.
# lst = [i * i for i in range(10) if i % 2 == 0]
# print(lst)

# list comp that preps a list of chars which are present in string and not equal to char 'a'
# lster = [i for i in "vishal" if i!='a']
# print(lster)

# list comp that preps a list of numbers which are satisfying multiple if conditions
# ifer = [i for i in range(20) if i%2==0 if i%4==0 if i<=15]
# print(ifer)

# list comp that preps a list of names not containing letter 'V'. Here the order of loop and if-else changes.
# names = ["Vishal", "lokesh", "Sairaj", "Viraj"]
# dec = ["Yes" if "V" in j else "No" for j in names]
# print(dec)

# list comp can be used with nested for loops as well for preparing a matrix too.
