def stud_list():

    stud_list = []
    a = int(input("\nenter total number of students to add details : "))
    print("\n+---------------------+\n+---------------------+\n")

    for i in range (1,a+1):
        for j in range (0,1):
            dumy_list = []
            dumy_list.append(i)
            name = input("enter name : ")
            dumy_list.append(name)
            course = input("enter course : ")
            dumy_list.append(course)
        stud_list.append(dumy_list)
        print("\n")
    print("+---------------------+\n+---------------------+\n")
    return stud_list

dumy_list = stud_list()
for i in range (0,len(dumy_list)):
    print(f"roll no : {dumy_list[i][0]}")
    print(f"name : {dumy_list[i][1]}")
    print(f"course : {dumy_list[i][2]}")
    print("\n+---------------------+\n")