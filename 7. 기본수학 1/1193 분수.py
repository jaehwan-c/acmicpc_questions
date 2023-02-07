a=int(input())

index=1
while a > index:
    a -= index
    index += 1
    
if index % 2 ==0:
    top = a
    bot = index - a + 1
else:
    top = index - a + 1
    bot = a
    
print(f'{top}/{bot}')