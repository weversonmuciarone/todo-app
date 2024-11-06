'''
filenames = ['1. Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)
'''

ips = ['100.122.133.105', '100.122.133.111', '123.456.789']

for i, ip in enumerate(ips):
    number = int(input('Enter the index of the IP you want: '))
    user = ips[number]
    row = f'You choose {user}'
    print(row)
    break