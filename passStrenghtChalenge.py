user_pass = input("Please enter your password: ")
result = {}


def strenght(password):
    if len(user_pass) >= 8:
        result['Length'] = True
    else:
        result['Length'] = False

    digit = False
    for i in user_pass:
        if i.isdigit():
            digit = True
    result['Digits'] = digit

    upper_case = False
    for i in user_pass:
        if i.isupper():
            upper_case = True
    result['Upper_case'] = upper_case

    lower_case = False
    for i in user_pass:
        if i.islower():
            lower_case = True
        result['Lower_case'] = lower_case

    if all(result.values()):
        print('Strong Password')
    else:
        print('Weak password')


strenght(password=user_pass)





