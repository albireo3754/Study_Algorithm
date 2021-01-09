def solution(prices):
    answer = [0] * len(prices)
    prices.pop()
    for i,v in enumerate(prices):
        for j in range(i, len(prices)):
            if prices[j] >= v:
                answer[i] += 1
            else:
                break
    return answer
