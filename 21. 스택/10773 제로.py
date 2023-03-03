import sys

n = int(sys.stdin.readline())

stack = list()

for i in range(n):
    int_input = int(sys.stdin.readline())
    
    if int_input == 0:
        stack.pop()
    else:
        stack.append(int_input)
        
print(sum(stack))