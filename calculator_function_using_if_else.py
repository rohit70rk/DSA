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
    
    try:
        if operator == "/":
            div = num1 / num2
            return div

        if operator == "//":
            rem = num1 // num2
            return rem
        
    except ZeroDivisionError:
        print("You can't divide by zero!")

    else :
        return "invalid input"


cal = cal(3,0,"-")
print(cal)