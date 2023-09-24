# Use time module to print Good <...> according to the time.
# Good Morning sir Exercise

# Time module
import time

# gmtime() prints current time and date in attributes format if no argument (seconds) given.
# 0 as an arg will print the epoch time for the machine which is usually 1 january, 1970.
# Any random seconds will print all time and date on that particular day.
# print(time.gmtime(0))

# time() methods return the current time in seconds since epoch.
# It returns a floating-point number.
# print(time.time())

# ctime(secs) accepts seconds as an input and converts into readable date and time.
# Either you pass seconds or time.time() method for current date time.
# No arguments return epoch time and date.
# print(time.ctime())

# sleep(secs) method pauses execution of program for amt. of seconds and then resumes it.
# Useful if you want the program to load something before complete execution.
# time.sleep(5)
# print("Resume")


# time.struct_time class attributes :-

# Index   Attribute Name 	    Values
# 0	        tm_year	        0000, …, 9999
# 1	        tm_mon	        1, 2, …, 11, 12
# 2	        tm_mday	        1, 2, …, 30, 31
# 3	        tm_hour	        0, 1, …, 22, 23
# 4	        tm_min	        0, 1, …, 58, 59
# 5	        tm_sec	        0, 1, …, 60, 61
# 6	        tm_wday	        0, 1, …, 6; Sunday is 6
# 7	        tm_yday	        1, 2, …, 365, 366
# 8	        tm_isdst	    0, 1 or -1

# localtime(secs) works just like gmtime() method.
# print(time.localtime())

# mktime() is inverse of local time or gmtime(). It converts the objects into seconds.
# Objects created from gmtime() or localtime() be given as an input to this method.
# obj1 = time.localtime(time.time())
# obj2 = time.gmtime()
# print(time.mktime(obj1))
# print(time.mktime(obj2))


# strftime() takes two args :-
# 1. String with format specifiers (Mandatory)
# 2. localtime() or gmtime() object.
# (Optional, No need if working with current time and date. Just provide format codes) Both take seconds as input and
# current time if no seconds are given.

# obj3 = time.strftime("%H %M %S", time.localtime())
# print(obj3)

# asctime(obj) takes object from localtime() and gmtime() method and converts to proper date and time.
# obj1 = time.localtime(1657894)
# print(time.asctime(obj1))

# strptime() method converts the string representing time to the struct_time object.
string = "Tue, 03 Aug 2021 10:45:08"
obj = time.strptime(string, "%a, %d %b %Y %H:%M:%S")

print(obj)
