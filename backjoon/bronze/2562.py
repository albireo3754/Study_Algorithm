from sys import stdin

max_val = 0
idx = 0
for i in range(9):
    input_val = stdin.readline().rstrip()
    if max_val < int(input_val):
        max_val = int(input_val)
        idx = i + 1
        
print(max_val)
print(idx)