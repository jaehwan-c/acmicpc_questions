a = int(input())

for i in range(a):
    sum = 0
    to_print = 0
    list_calc = list(map(int, input().split()))
    for j in range(1, len(list_calc)):
    	sum += list_calc[j]
    avg = sum/(len(list_calc)-1)
    for k in range(1, len(list_calc)):
    	if list_calc[k] > avg:
    	    to_print += 1
    value_to_print = to_print/(len(list_calc)-1)*100
    print("{:.3f}%".format(value_to_print))
