def del_zero(text):
    # dec_val = int(text, 2)
    # zero_cnt = 0
    # while dec_val > 1:
    #     if dec_val % 2 == 1:
    #         dec_val
    len_text = len(text)
    zero_cnt = 0
    new_text = ''
    for i in range(len_text):
        if text[i] == "0":
            zero_cnt += 1
        elif text[i] == "1":
            new_text += "1"

    binary_text = format(len(new_text), 'b')
    return binary_text, zero_cnt

def solution(s):
    answer = [0, 0]
    isThereZero = 1
    while s != "1":

        s, isThereZero = del_zero(s)

        answer[0] += 1
        answer[1] += isThereZero
    return answer