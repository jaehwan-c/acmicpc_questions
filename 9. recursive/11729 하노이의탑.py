def hanoi(n, start_pos, final_pos, via):
    if n == 1:
        print(start_pos, final_pos)
        return
    else:
        hanoi(n-1, start_pos, via, final_pos)
        print(start_pos, final_pos)
        hanoi(n-1, via, final_pos, start_pos)

def main():
    a = int(input())
    print(2**a - 1)
    hanoi(a, 1, 3, 2)
    
main()

# https://sikaleo.tistory.com/29