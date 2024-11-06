def liters_to_m3(liters):
    m3 = liters / 1000
    return m3


user = float(input("Enter liters to convert to m3: "))
result_m3 = liters_to_m3(user)
print(result_m3)