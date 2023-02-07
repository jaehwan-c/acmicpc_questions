import math

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(math.factorial(b) // (math.factorial(a) * math.factorial(abs(a - b))))
    
