# break and continue statement -

# break statement is used to get out of the loop while continue
# statement helps in skipping expected possibility.
# If you use continue statement in while loop, always remember
# to increment first before the condition with continue arrives.
# else the loop will be stuck as continue is sending the same
# number again and again without any change in it.

i = 0
while i < 10:
    i += 1
    if i == 6:
        break
    if i == 2 or i == 4:
        continue
    print(i)

