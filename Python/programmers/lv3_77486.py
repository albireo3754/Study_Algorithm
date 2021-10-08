import math

def solution(enroll, referral, seller, amount):
    answer = [0 for i in range(len(enroll))]
    edge = {}
    index_dict = {}
    prices = list(map(lambda x: x * 100, amount))
    for index, value in enumerate(enroll):
        index_dict[value] = index
        
    def recursion_give(index, price):
        next_people = referral[index]
        next_price = math.floor(price * 0.1)
        answer[index] += (price - next_price)
        if price < 10:
            return
        if next_people == "-":
            return
        recursion_give(index_dict[next_people], next_price)
    for seller_item, price in zip(seller, prices):
        index = index_dict[seller_item]
        recursion_give(index, price)

    return answer