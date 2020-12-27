from sys import stdin

a, b = stdin.readline().rstrip().split(" ")

if int(a) > int(b):
    print(">")
elif int(a) == int(b):
    print("==")
else:
    print("<")
