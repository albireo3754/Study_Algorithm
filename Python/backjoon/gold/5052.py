import sys

input = sys.stdin.readline

T = int(input().rstrip())
for i in range(T):
    n = int(input().rstrip())
    dictionary = set()
    flag = False
    phone_numbers = [input().rstrip() for i in range(n)]
    phone_numbers.sort(key = lambda x: len(x))
    # print(phone_numbers)
    for j in range(n):
        phone_number = phone_numbers[j]
        temp = ""
        for p in phone_number:
            temp += p
            if temp in dictionary:
                flag = True
            if flag:
                break
        if flag:
            break
        dictionary.add(phone_number)
    if flag:
        print("NO")
        continue
    print("YES")