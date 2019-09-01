while True:
    x = float(input("input 1st number:"))
    opr = input("input the operator:")
    y = float(input("input 2nd number:"))
    z = 0
    if opr == '*':
        z = x * y
    elif opr == '/':
        z = x / y
    elif opr == '-':
        z = x - y
    elif opr == '+':
        z = x + y   
    print("the result is:", z)
    b = input('continue?')
    if b == 'False':
        break
    
