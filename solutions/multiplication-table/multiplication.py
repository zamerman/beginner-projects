# Multiplication Table
# Python 3.5.10
# Written by alfredmuffin

for num in range(1, 13):
    for i in range(1, 13):
        print(str(i * num).rjust(4), end='')
    print()
