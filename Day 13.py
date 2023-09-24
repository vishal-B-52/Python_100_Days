# Popular methods in String

str = "My name is Vishal.\t"

# upper() makes string uppercased
# lower() makes string lowercased
""" rstrip("<Character>") strips the character off of the string's trailing end. 

The character should be entered in form of a string let it be alphanumeric or alphabetic or special character. 

"!" is acceptable meanwhile "!!" or "!##33" are unacceptable. """

str1 = "trail istermforremnant"
#print(str1.rstrip("l"))

#lstrip("<Character>") strips the character off of the string's leading end. Same crierias as rstrip.

# Replaces all occurences of char/string 1 with char/string 2.
#print(str.replace('i', 'v'))

#split("<character>") splits the string into multiple parts by breaking it from the character and returns all those string in a list.

# print(str.split(" "))  # Brekas string at whitespace and returns list.

# capitalize() capitalizes the starting character of a string.
# print(str1.capitalize())

# center(<int>) divides int by 2 and puts str in middle while distributing the whitespaces (default fillcharacter) equal to divided int on both sides.
#  In case of odd int such as 15, start gets lower amt of whitespace(7) and end gets the higher(8). Second argument is for fillcharacter which can be set to a 
# character ('v' or 's'). Cannot be put into double quotes ("v") or be used more than once ('vvv' or '#!* or ';aada')

# print(len(str1))
# print(str1.center(40, 'v'))

#count(character) allows you to count number of occurences of a 
# character in the string
# print(str.count('i'))

#endswith() returns true or false if the arg string is end of given statement. This arg can be an entire statement, a word, a substring 
# or a character enclosed in double quotes. Endswith also offers two more args, start and end, which takes index as an input and check 
# whether the string input appears at the end of sliced string from start to end.

# print(len(str1))
# print(str1.endswith("term for remnant"))
# print(str1.endswith("term for remnant", 3, 25))

# find("string") accepts a string and looks for the first occurence of that string in original string.
# It returns index where it is located and if it's absent, returns -1.
# Accpetable values are anything which is enclosed in double quotes. Eveen special characters too.
# print(str.find("i"))

# index() method is another copy of find() method but instead of returning -1, it raises an exception.
# print(str.index("i"))

# isalnum() returns True if characters in string do not contain Whitespaces and special characters. 
# Only A-Z, a-z and 0-9 are allowed.
# print(str1.isalnum())

# isalpha() returns True if string contains only Alphabtes(lower or Upper case). Numbers and special chars are not allowed.
# print(str.isalpha())

# islower() returns true if all are lowercase
# print(str1.islower())

# isprintable() returns True if string does not contains any escape sequences or characters which are in string but get translated 
# to make user experience better (\n, \r, \t, \\) etc.
# print(str.isprintable())

# isspace() returns true only if entire string consists of spaces (a blank string)..
# print(str1.isspace())

#istitle() returns True if string's every word's first character is capitalized.
# print(str.istitle())

# isupper() returns True if string is uppercased.
# print(str1.isupper())

# startswith() returns True if string starts with the sub-string you mentioned.
# Follows same criteria and arg as endwith() method.
# print(str1.startswith("term for remnant"))

# swapcase() toggles the cases of each character in the string. Upper to lowercase 
# and vice-versa.  
print(str.swapcase())

# title() capitalizes each word's first char of the string.
print(str1.title())