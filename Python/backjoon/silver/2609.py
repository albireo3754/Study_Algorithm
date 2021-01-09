A ,B = map(int, input().split(" "))

ab = A * B
if B > A:
    temp = 0
    temp = B
    B = A
    A = temp


while B>0:
    gcd = A % B
    A = B
    B = gcd

gcd = A

lcm = ab // gcd

print(gcd, lcm)
    