n = int(input())
road_len = list(map(int, input().split()))
city_price = list(map(int, input().split()))
city_price.pop()

result = 0
temp_price = 0

for i in range(len(city_price)):
    if i == 0:
        temp_price = city_price[i]
        result += temp_price * road_len[i]
    else:
        if temp_price >= city_price[i]:
            temp_price = city_price[i]
            result += temp_price * road_len[i]
        else:
            result += temp_price * road_len[i]
            
print(result)