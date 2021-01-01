def solution(n, arr1, arr2):
    answer = [" "*n]*n

    for i in range(n):
        bin_1 = format(arr1[i],'b')[::-1]
        bin_2 = format(arr2[i],'b')[::-1]
        for idx, val in enumerate(bin_1):
            if val == "1":
                answer[i] = answer[i][0:idx] + "#" + answer[i][idx+1:]
        for idx, val in enumerate(bin_2):
            if val == "1":
                answer[i] = answer[i][0:idx] + "#" + answer[i][idx+1:]


    return [i[::-1] for i in answer]

#use bit
#bin arr1[i] | arr2[i]
# and full 0 use rjust function rjust(n,'0')
# or bin arr1[i] | arr2[i] | pow(2,n) --> 0b1 delete