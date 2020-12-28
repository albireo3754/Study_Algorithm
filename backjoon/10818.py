from sys import stdin

N = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().rstrip().split(" ")))
top, bot = nums[0] , nums[0]
for i in range(N):
    top = max(top, nums[i])
    bot = min(bot, nums[i])
print(f"{bot} {top}")

    