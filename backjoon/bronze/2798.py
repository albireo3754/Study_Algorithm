import sys
from itertools import combinations
def black_jack():
    first_line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    blackjack = first_line[1]

    cardsets = combinations(nums, 3)
    near_blackjack = 0
    for cardset in cardsets:
        isblackjack = sum(cardset)
        if isblackjack < blackjack:
            near_blackjack = max(near_blackjack, isblackjack)
        elif isblackjack == blackjack:
            return blackjack
    return near_blackjack
print(black_jack())

# def black_jack():
#     first_line = list(map(int, sys.stdin.readline().rstrip().split(" ")))
#     nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))


#     near_blackjack = 0
#     blackjack = first_line[1]

#     nums.sort()

#     stack = [-1]
#     # print(nums)
#     isblackjack = nums[-1]
#     while len(stack) > 0:
#         j = stack.pop()
#         isblackjack -= nums[j]
#         for i in range(j + 1, len(nums)):
#             # print(isblackjack)
#             if isblackjack < blackjack:
#                 isblackjack += nums[i]
#                 stack.append(i)
                
#             elif isblackjack == blackjack:
#                 return blackjack
#             elif isblackjack > blackjack:
#                 isblackjack -= nums[stack.pop()]
#                 near_blackjack = max(near_blackjack, isblackjack)
#                 break
#     return near_blackjack
# print(black_jack())

