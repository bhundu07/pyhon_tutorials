num1 = int(input('Enter any number you want: '))
num2 = int(input('Enter another number you want: '))
operator = input('Enter a math operator you want (+, -, *, /, %): ')

if(operator == '+'):
    print(num1 + num2)
elif(operator == '-'):
    print(num1 - num2)
elif(operator == '*'):
    print(num1 * num2)
elif(operator == '/'):
    print(num1 / num2)
elif(operator == '%'):
    print(num1 % num2)
else:
    print('Sorry, but I cannot understand your operation')
