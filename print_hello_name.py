def list():
    list = []
    a = int(input("enter lenght of list : "))
    list.append("\n")
    for i in range (1,a+1):
        name = input("enter name : ")
        conca = "Hello " + name + "!"
        list.append(conca)
    list.append("\n")
    return list

massage = list()
for i in range (0,len(massage)):
    print(massage[i])