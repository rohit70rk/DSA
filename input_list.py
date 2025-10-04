def list():
    list = []
    a = int(input("enter lenght of list : "))
    for i in range (0,a):
        b = int(input("enter a number : "))
        list.append(b)
    return list

print(list())