N = int(input())
s = input()

answer = 0

for i, v in enumerate(s):
    answer += (31 ** i) * (ord(v) - 96)

print(answer % 1234567891)