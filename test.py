f = open('test.txt', 'r')
print(f.read())
f.close()

with open ('test.txt', 'a') as file:
    file.write(' we hacked you')

