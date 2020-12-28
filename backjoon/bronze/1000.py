from sys import stdin

input_text = stdin.readline().rstrip()
inputs = input_text.split(" ")
answer = 0

for i in inputs:
    answer += int(i)

print(answer)