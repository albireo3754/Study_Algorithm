def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = bin(number)
        if bin_num[-1] == '0':
            answer.append(int(bin(number)[:-1] + '1', 2))
        else:
            n = -1
            # print(bin_num)
            for i in range(len(bin_num) - 1, 1, - 1):
                if bin_num[i] == '0':
                    # print(i)
                    # answer.append(int(bin(number), 2) ^ (3 << n))
                    break
                n += 1
            answer.append(int(bin(number), 2) ^ (3 << n))
                
    return answer