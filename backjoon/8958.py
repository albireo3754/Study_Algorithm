from sys import stdin

input_N = int(input())

for i in range(input_N):
    test_case = stdin.readline().rstrip()
    acc_score = 0
    output_score = 0
    for isO in test_case:
        if isO == 'O':
            acc_score += 1
            output_score += acc_score
        else:
            acc_score = 0
    print(output_score)
