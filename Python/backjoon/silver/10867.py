import sys

input = sys.stdin.readline

N = int(input())
arr = set(map(int , input().split()))
print(*sorted(arr))