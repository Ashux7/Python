# keys = ['one','two','three']
# values = [1,2,3]
# D = {}
# for x in range(len(keys)):
#     D[keys[x]]=values[x]
# print(D)

a = int(input("How many friend(s)\' details do you want to enter?: "))
diary = {}
for i in range(a):
    name,no = eval(input("Enter name: , Enter number: "))
    no = int(no)
    diary[no]=name
print()
print("Name and phone number of all friends:")
for x in diary:
    print(diary[x],":",x)
print()
print("Add new key-value pair")
new = int(input("How many friends to add?: "))
for nw in range(new):
    name,no = eval(input("Enter name: , Enter number: "))
    diary[no]=name
for x in diary:
    print(diary[x],":",x)