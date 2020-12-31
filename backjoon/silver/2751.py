import sys
N = int(input())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

for i in sorted(list(set(nums))):
    print(i)