check_num = int(input())
print_num = check_num

for i in range(check_num):
    to_check = input()
    for j in range(0, len(to_check)-1):
        if to_check[j] == to_check[j+1]:
            pass
        elif to_check[j] in to_check[j+1:]:
            print_num -= 1
            break            

print(print_num)