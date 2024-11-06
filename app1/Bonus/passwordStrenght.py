'''
password = input("Enter new password: ")

This code is fully working however we use the append method to save in a list and at the end we use the all method to get hold of all true from the list
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True
result.append(digit)

upper_case = False
for i in password:
    if i.isupper():
        upper_case = True
result.append(upper_case)

lower_case = False
for i in password:
    if i.islower():
        lower_case = True
result.append(lower_case)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")
'''

# the code below is a copy of the above however we are using a dictionary where we use key value to understand better the code as a programmer.
# This is like a barista with two shelves one with pots with only sugar and another one with diff items labeled each

password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digits"] = digit

upper_case = False
for i in password:
    if i.isupper():
        upper_case = True
result["upper-case"] = upper_case

lower_case = False
for i in password:
    if i.islower():
        lower_case = True
result["lower-case"] = lower_case

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
