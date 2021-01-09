def solution(board, moves):
    answer = 0
    N = len(board)
    # N is list and element 0~ 100

    bascetStack = []
    for move in moves:
        for row in board:
            doll = row[move - 1]
            if doll > 0:
                if len(bascetStack) == 0 or bascetStack[-1] != doll:
                    bascetStack.append(doll)
                else:
                    bascetStack.pop()
                    #터질때마다 answer += 2
                    answer += 2
                row[move - 1] = 0
                break


    return answer