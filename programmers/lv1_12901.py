def solution(a, b):
    answer = ''
    weeks = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
#     a = 1 b = 1 week ='FRI' - counter 0 idx counter // 7 
    month = sum(months[:a])
    day = b - 1
    counter = month + day
    answer = weeks[counter%7]
    return answer