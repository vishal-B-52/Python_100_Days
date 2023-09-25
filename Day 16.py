# Match case Statement

# Match case statement is alternative of Switch case statement in C, C++ and Java.
# Match case is useful when multiple if statements have to processed one by one without an actual if-elif-else ladder.
# Match case is only available in Python's 3.10+ versions.
# Python match cases do not require "break" statement at the end of every case.
# Every case is also called as a pattern.
# Syntax:
# x = 0
# match x:  # Equivalent of "Switch(x){} "
#     case  0:
#         print("First case found")
#     case 4:
#         print("Second case matches")
#     case _:  # Equivalent of "default: " statement
#         print("no cases match")

# Each case and default statement can be modified with if statements too which helps program decide
# which specific case or default statement to execute in given situation.
# Also a default statement or a case with no ifs cannot be put before one with conditioned case or default statement.
# Doing so would result in a non-reachable code as it cannot reach the conditional blocks deployed since blank case
# or default statements are blocking their reach and executing first.

x = int(input("Enter a number: "))
match x:
    case  0 | 4:
        print("First case found")
    case _ if 5 < x < 7:
        print("Real nice range")
    case _ if 21 < x <= 100:
        print("Range is too big")
    case _:
        print("no cases match")

# Match cases can tolerate an int, float, char, string value for matching.
# To append many similar case into one use |(OR) operator. & is not acceptable.
# def provideAccess(user):
#     return {
#         "username": user,
#         "password": "admin"
#     }
# def runMatch():
#     user = str(input("Write your username -: "))
#
#     # match statement starts here .
#     match user:
#         case "Om":
#             print("Om do not have access  to the database \
#             only for the api code.")
#         case "Vishal":
#             print(
#                 "Vishal do not have access to the database , \
#                 only for the frontend code.")
#
#         case "Rishabh":
#             print("Rishabh have the access to the database")
#             print(provideAccess("Rishabh"))
#
#         case _:
#             print("You do not have any access to the code")
# runMatch()
