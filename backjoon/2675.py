from sys import stdin

test_count = int(stdin.readline().rstrip())
for i in range(test_count):
    inputs = stdin.readline().rstrip().split(" ")

    re_num = int(inputs[0])
    text = inputs[1]
    output = ''
    for j in text:
        output += j * re_num
    print(output)
