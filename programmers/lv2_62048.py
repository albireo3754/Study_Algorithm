import math
def solution(w,h):
    return w * h - w - h + math.gcd(w, h)

# import math

# def gcd(a, b):
#     if b>a:
#         a, b = b, a
#     while b != 0:
#         a, b = b, a%b
#     return a
    
# def solution(w, h):
#     answer = 1
    
#     gcd_ = math.gcd(w, h)
#     w_, h_ = w//gcd_, h//gcd_
#     div = h_ / w_
#     before_h = 0
#     remove = 0
#     for i in range(1, w_ + 1):
#         remove += math.ceil(i * div) - before_h
#         before_h = int(i * div)
#     answer = w * h - gcd_ * remove
#     return answer

