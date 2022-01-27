i = 0
list_num = []
while i<=100:
    if i%2 == 0:
        list_num.append(i)
        i+=1
        continue
    elif i%3 == 0:
        list_num.append(i)
        i+=1
        continue
    else:
        i+=1
        continue
print(list_num)
for i in list_num:
    print(i)