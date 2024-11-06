'''
# Catch the zero error when a user tried to multiply to zero
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    total = value / total_value * 100
    print(f"That is {total}%")

except TypeError:
    print("You need to enter a number. Run the program again.")
except ZeroDivisionError:
    print("Your total value cannot be zero.")
'''
'''
# Loop over the colours greater than 50

colors = [11, 34, 98, 43, 45, 54, 54]
for i in colors:
    if i >= 50:
        print(i)
'''
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")
