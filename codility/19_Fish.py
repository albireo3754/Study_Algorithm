
#100%

def solution(A, B):
    # write your code in Python 3.6
    goUp = [] #0 go 0
    goDown = [] #1 go N

    for i, v in enumerate(B):
        if v == 0:
            while len(goDown) != 0:
                fightFish = goDown.pop()
                if fightFish> A[i]:
                    goDown.append(fightFish)
                    break
            if len(goDown) == 0:
                goUp.append(A[i])
        elif v == 1:
            goDown.append(A[i])
    
    return len(goUp) + len(goDown)