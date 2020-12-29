import sys

is_not_zero = int(sys.stdin.readline().rstrip())

while is_not_zero:
    re_num = 0
    num = is_not_zero
    while num>0:
        re_num = re_num * 10 + num % 10
        num = num // 10
    if re_num == is_not_zero:
        print('yes')
    else:
        print('no')
    is_not_zero = int(sys.stdin.readline().rstrip())