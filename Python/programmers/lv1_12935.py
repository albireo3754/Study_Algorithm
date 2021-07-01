def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    removed = arr.index(min(arr))

    return arr[:removed] + arr[removed + 1:]