x = int(input("1st: "))
y = int(input("2nd: "))
z = int(input("3rd: "))

if x > y and x > z:
    max = x
    print("Max:",max)
elif y > x and y > z:
    max = y
    print("Max:",max)
else:
    max = z
    print("Max:",max)

if x < y and x < z:
    min = x
    print("Min:",min)
elif y < x and y < z:
    min = y
    print("Min:",min)
else:
    min = z
    print("Min:",min)

if x > min and x < max:
    print("Middle:",x)
elif y > min and y < max:
    print("Middle:",y)
else:
    print("Middle:",z)
