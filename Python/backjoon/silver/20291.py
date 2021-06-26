import sys

input = sys.stdin.readline

N = int(input())
file_dict = {}
for i in range(N):
    file_name = input().rstrip()
    name, exe = file_name.split('.')

    if exe in file_dict:
        file_dict[exe] += 1
    else:
        file_dict[exe] = 1
    
for exe in sorted(file_dict):
    print(exe, file_dict[exe])