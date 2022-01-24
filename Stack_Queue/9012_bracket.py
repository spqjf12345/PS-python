import sys
num = int(sys.stdin.readline())

def isValidBracker(s):
    stack = []
    for i in s:
        if(i == '('):
            stack.append('(')
        else:
            if(len(stack) != 0):
                stack.pop()
            else:
                return "NO"

    if(len(stack) > 0):
        return "NO"
    elif(len(stack) == 0):
        return "YES"

for _ in range(num):
    s = list(input())
    print(isValidBracker(s))


