n = int(input())
base_lst = list()

for i in range(n):
    base_lst.append(int(input()))

def bubbleSort(A):
    for bubble in range(len(A)-1,0,-1):
        for i in range(bubble):
            if A[i]>A[i+1]:
                A[i],A[i+1] = A[i+1], A[i]

bubbleSort(base_lst)

for i in range(n):
    print(base_lst[i])           