mid_exp = input().rstrip()
add = ['+', '-']
mul = ['*', '/']

def compiler(mid_exp):
    stack_size = [0]
    exp_stack = []
    answer = ''
    for i in mid_exp:
        if i.isalpha():
            answer += i
        else:
            if i in add:
                if len(exp_stack) == stack_size[-1]:
                    exp_stack.append(i)
                elif exp_stack[-1] in add:
                    answer += exp_stack.pop()
                    exp_stack.append(i)
                elif exp_stack[-1] in mul:
                    while len(exp_stack) > stack_size[-1]:
                        answer += exp_stack.pop()
                    exp_stack.append(i)
            elif i in mul:
                if len(exp_stack) == stack_size[-1]:
                    exp_stack.append(i)
                elif exp_stack[-1] in add:
                    exp_stack.append(i)
                elif exp_stack[-1] in mul:
                    answer += exp_stack.pop()
                    exp_stack.append(i)
            elif i == "(":
                stack_size.append(len(exp_stack))
            elif i == ")":
                pop_end = stack_size.pop()
                while len(exp_stack) > pop_end:
                    answer += exp_stack.pop()
    while exp_stack:
        answer += exp_stack.pop()
    return answer
print(compiler(mid_exp))
# print(compiler(pre_compiler(mid_exp)))