'''
file = open('files/members.txt', 'r')
my_file = file.readlines()
file.close()

user = input('Add new member: ') + '\n'

my_file.append(user)

file = open('files/members.txt', 'w')
file.writelines(my_file)
file.close()
'''
'''
filenames = ['files/doc.txt', 'files/report.txt', 'files/ presentation.txt']

for filename in filenames:
    file = open(filename, 'r')
    file.read()
    file.close()

    file = open(filename, 'w')
    file.write('hello2')
    file.close
print('Successful')
'''
'''
filenames = ['files/a.txt', 'files/b.txt', 'files/c.txt']

for filename in filenames:
    file = open(filename, 'r')
    files = file.readlines()
    file.close()
    print(files)
'''

file = open("data.txt", 'w')
file.writelines("100.12\n")
file.writelines("111.23")

file.close()