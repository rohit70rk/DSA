def cal(num1,num2,operator):
    if operator == "+":
        sum = num1 + num2
        return sum
    
    elif operator == "-":
        sub = num1 - num2
        return sub

    elif operator == "*":
        mul = num1 * num2
        return mul
    
    elif operator == "/":
        div = num1 / num2
        return div

    elif operator == "//":
        rem = num1 // num2
        return rem

    else :
        print("invalid input")


cal = cal(3,2,"//")
print(cal)