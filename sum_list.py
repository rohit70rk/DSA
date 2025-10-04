def sum(num):
    sum = 0
    for i in range (0,len(num)):
        sum += num[i]
    return sum


num = [2,4,1,3]
print(sum(num))