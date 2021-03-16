exp = input()

def sum(exp):
    res = 0
    num = ''
    for i, v in enumerate(exp):
        if v == '-' or v == '+':
            res += int(num)
            num = ''
        else:
            num += v
    else:
        res += int(num)
    return res

def make_min(exp):
    res = 0
    num = ''
    while exp:
        for i, v in enumerate(exp):
            if v == '-':
                res += int(num)
                res -= sum(exp[i + 1:])
                break
            elif v == '+':
                res += int(num)
                num = ''
            else:
                num += v
        else:
            res += int(num)
        
        return res

print(make_min(exp))
    