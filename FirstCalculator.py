x = int(input('Please input the first number: '))
y = int(input('Please input the second number: '))
operator = input('Please enter an operator (+, -, *, or /): ')
ans = 0

if operator == '+':
    ans = x + y
elif operator == '-':
    ans = x - y
elif operator == '*':
    ans = x * y
elif operator == '/':
    ans = x / y
print(x, operator, y, '=', ans)