import sys
def sieve(maxval):
    nums = [i for i in range(maxval + 1)]
    prime = []
    nums[1] = 0
    for num in nums:
        if num==0:
            continue
        isprime = num
        prime.append(isprime)
        while isprime<maxval+1:
            nums[isprime] = 0
            isprime += num
    return prime

N = input()
checks = map(int, sys.stdin.readline().rstrip().split(" "))
prime = sieve(1000)
cnt = 0
for num in checks:
    if num in prime:
        cnt += 1
print(cnt)
