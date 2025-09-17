def sort_user_list():
    
    user_input = input("Enter numbers separated by spaces: ")
    
    
    num_list = list(map(int, user_input.split()))
    
    
    num_list.sort()
    
    print("Sorted list:", num_list)



sort_user_list()
