# # 65 = A      90 = Z
# ch = 90
# for i in range(1,27):
#     print(i,chr(ch))
#     ch-=1

x = int(input("No. of elements:"))
list = []
list2 = []
for i in range(x):
    elem = input("Enter name:")
    list.append(elem)
print(list)
for i in range(len(list)):
    list2.append(list[i][1:-1])
print(list2)