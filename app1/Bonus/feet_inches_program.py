from converters import convert
from parsers import parse

feet_inches = input("Enter your feet inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")