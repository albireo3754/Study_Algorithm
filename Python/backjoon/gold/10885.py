import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    twoMax = 0
    two = 0
    minusTwo = -1
    minus = False
    answer = 0
    for i in range(N):
        if arr[i] > 0:
            answer = 1
            if arr[i] == 2:
                two += 1
        elif arr[i] == 0:
            two = 0
            minus = False
            minusTwo = -1
        elif arr[i] < 0:
            minus = not minus
            if not minus:
                answer = 1
            if arr[i] == -2:
                two += 1
            if minusTwo == -1:
                minusTwo = two
        print(two, minusTwo)
        if not minus:
            twoMax = max(twoMax, two)
        if minus:
            twoMax = max(twoMax, two - minusTwo)

    for i in range(twoMax):
        answer = (answer * 2) % 1000000007
    print(answer)
