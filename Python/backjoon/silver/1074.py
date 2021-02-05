N, r, c = map(int, input().split(' '))

global answer
answer = 0
def find(x, y, n):
    global answer
    print(x, y, n, answer)

    if x == r and y == c:
        print(answer)
        return;
    if r >= x and r < x + n and c >= y and c < y + n:
        find(x, y, n >> 1)
        find(x, y + (n >> 1), n >> 1)
        find(x + (n >> 1), y, n >> 1)
        find(x + (n >> 1), y + (n >> 1), n >> 1)
    else:
        answer += n ** 2
    return answer
find(0, 0, 1 << N)