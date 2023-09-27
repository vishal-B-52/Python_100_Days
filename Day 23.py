# List methods -

myList = [11, 23, 2.56, 'vis', 'B', 3 + 6j, None]
nummer = [23, 56, 44, 49, -120, 111]
stringer = ['enum', 'delicious', 'Dettol', 'asthma', 'HIV', 'Egypt']

# append(element) adds an element too the end of list.
# myList.append(False)
# print(myList)


# sort() sorts list in ascending and descending order by terms of alphabets and Numbers. A mixed list won't work.
# nummer.sort()
# print(nummer)

# If list contains lowercase and uppercase elements, Uppercase are sorted first and lowercase are sorted later.
# stringer.sort() --> ['Egypt', 'HIV', 'asthma', 'delicious', 'dettol', 'enum']
# print(stringer)

# To sort in descending order, use 'reverse=True' in sort() method.
# stringer.sort(reverse=True)   --> ['enum', 'delicious', 'asthma', 'HIV', 'Egypt', 'Dettol']
# print(stringer)


# reverse() method reverses the original order of list. In short, Mirroring. [31, 24, 55] --> [55, 24, 31]
# nummer.reverse()
# print(nummer)

# index(element) returns first occurrence of the element.
# print(myList.index(11))

# count(element) return the amt. of time the element appeared in the list.
# print(stringer.count("Vishal"))

# copy() method creates a replica of the original list. Operation done on this list do not change OG list.
# copier = myList.copy()
# print(copier)
# copier.append("Checker")
# print(copier)
# print(myList)

# To create a list which is linked to OG one, just assign that list to one more variable.
# Operation performed on the OG list will be reflected upon linked one.
# conn = myList
# conn.append("ConnObject")
# conn.append(2.4443)
# print(conn, " <- -> ",myList)

# insert() method takes target index and element. The element will be inserted at the target index while pushing the
# element present on same index after the inserted element. So, element already present at index 2 will be pushed to
# index 3.
# nummer.insert(2, 4667)    # 4667 is inserted at 2nd index and 44 is pushed to index 3.
# print(nummer)

# extend() method takes a dictionary, list, tuple and adds it to an existing list.
# nummer.extend(myList)
# print(nummer)

# concatenating two lists - Concatenation adds second list elements to first one and assigns it to the variable.
# This can be used to simplify joining two lists together where extend() is not used.
# Anything performed on this list does not reflect on other
# k = myList + nummer
# print(k)

# clear() clears all elements of the list.
# nummer.clear()

# pop(index) methods removes element at the specified index position. If no index is mentioned, -1 is taken as index
# which means last item.
# stringer.pop(4)
# print(stringer)

# remove(element) method takes an element and removes its first occurence in the list.
# Element can be a string, number, list, etc.
# myList.remove(3+6j)
# myList.remove(None)
# print(myList)
