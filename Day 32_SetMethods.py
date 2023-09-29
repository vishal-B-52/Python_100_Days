# Set Methods -

"""
Sets in python works the same way in Mathematics.
Thus, it ultimately allows you to function in almost the same way.
"""

# union(set) method allows you to merge two sets where duplicate values will be eliminated.
# intersection(set) method allows you to form a set of common elements between both sets.
set1 = {1, 34, 5, "V", 24, "Vishal", 1+4j, 23.55, False}
set2 = {34, 1, "V", "Vishal", 23.55}
# print(set1.union(set2))
# print(set2.intersection(set1))

# update(set) method updates a set with elements present in set2. set2 remains unaffected while set1 changes.
# set1.update(set2)
# print(set1)

# intersection_update(set) finds intersection in both sets, clears set1 and puts the intersection set elements in it.
# set1.intersection_update(set2)
# print(set1)

# symmetric_difference(set2) finds union of set1 and set2 and then eliminates element common between both sets from
# the resulting set, i.e removal of intersection set. Resulting set is the symmetric diff for you which contains
# elements that are not common.
# set3 = set1.symmetric_difference(set2)
# print(set3)

# symmetric_difference_update(set2) performs the above method and clear & updates set1. No sets are returned.
# set2.symmetric_difference_update(set1)
# print(set2)

# difference(set2) method subtracts elements common in set1 and set2 and returns set1. Also written as A-B.
# print(set2.difference(set1))

# difference_update(set2) method finds difference (see above method) and updates set1 with the returned set.
# set1.difference_update(set2)
# print(set1)

# isdisjoint(set2) method checks whether elements of set1 are present in set2. If even 1 element is common, False is
# returned. Else True. In short, if intersection is possible then target set is not disjoint.
# Set1 is not-disjoint as 1 and "V" are present in both sets. Same goes to set2.
# print(set1.isdisjoint(set2))

# issuperset(set2) checks whether set1 contains all elements in set2. Returns true if all elements are part of set1.
# print(set1.issuperset(set2))

# issubset(set2) checks whether all elements in set1 are part of set2. Return True if set1 is subset of set2. Supersets
# and subsets are opposite.
# If set1 is superset of set2, it can never be subset of set2. In case of subset, same logic can be used.
# print(set1.issubset(set2))

# add(element) adds single element to the set.
# set1.add("One Lakh")
# print(set1)

# update(collection) method can be used to add multiple elements from a collection into the set.
# This collection can be a list, tuple, dictionary, set, etc.
# set2.update(set1)

# remove(element) method remove an element from set. Raises error if element not present.
# set2.remove("V")

# discard(element) method remove an element from set. DOES NOT raises any error if element not present.
# set2.remove("V")

# pop() method removes and returns the last element in set. Since sets are randomized every time, we don't know what the
# last element will be. pop(index) variation of the method works only for list and tuple and not for sets.
# c = set1.pop()
# print(set1)
# print(c)

# 'del <collection_name>' can be used to delete an entire set and printing such collection raises NameError.
# del keyword can be used in same manner for dict, list and tuples.
# del set2
# print(set2)

# clear() method clears all items within the set. Printing such sets shows "set()". No empty "{}" or "{()}"
# set2.clear()
# print(set2)




