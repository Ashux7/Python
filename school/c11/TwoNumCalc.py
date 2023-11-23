x = int(input("Enter first number:"))
op = input('''Choose operator:
+ Add
- Subtract
/ Divide
// Floor Division
* Multiply
** Exponent
% Remainder
:''')
y = int(input("Enter second number:"))
sum = x+y
sub = x-y
div = x/y
floord = x//y
prod = x*y
exp = x**y
rem = x%y

if op == '+':
    print("Sum of the two numbers is:",sum)
elif op == '-':
    print("Difference of two numbers is:",sub)
elif op == '/':
    print("Division of two numbers give:",div)
elif op == '//':
    print("Floor Division of two numbers give:",floord)
elif op == '*':
    print("Product of two numbers is:",prod)
elif op == '**':
    print("First number raised to power of Second gives:",exp)
else:
    print("Remainder on dividing two numbers is:",rem)
