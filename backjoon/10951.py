from sys import stdin

for line in stdin:
    inputs = line.rstrip().split(" ")
    output = int(inputs[0]) + int(inputs[1])
    if output == 0:
        break
    print(output)