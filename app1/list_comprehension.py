'''
contents = ['this is the first item', 'this is the second item', 'this is the third item']

filenames = ['doc.txt', 'report.txt', ' presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f'files/{filename}', 'w')
    file.write(content)
    file.close()
'''
'''
filenames = ['files/1.doc.txt', 'files/1.report.txt', 'files/1. presentation.txt']

filename = [filename.replace('.', '-', 1) for filename in filenames] # list comprhension
print(filename)

# for filename in filenames:
#     filename = filename.replace('.', '-', 1)
#     print(filename)
'''
'''
names = ["john smith", "jay santi", "eva kuki"]

new_names = [new_names.title() for new_names in names]
print(new_names)
'''
'''
usernames = ["john 1990", "alberta1970", "magnola2000"]

names_len = [len(username) for username in usernames]

print(names_len)
'''
user_entries = ['10', '19.1', '20']
user_numbers = [float(item) for item in user_entries]
print(sum(user_numbers))