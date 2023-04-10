# d = {}
# stu = int(input('Enter number of student to store data for: '))
# for i in range(stu):
#     name = input("Name: ")
#     marks = float(input("Marks: "))
#     d[name]=marks
# print(d)

d={'ashu':10,'abc':20,'xyz':15,'george':69,'mary':38}

# MAX MARKS
maxm=0
for i in d:
    if d[i] >= maxm:
        maxm = d[i]
    else:
        pass
print("HIGHEST MARKS ARE: ",maxm)

# AVERAGE MARKS
avg = 0
for i in list(d.values()):
    avg += float(i)
print('AVERAGE MARKS OF THE STUDENTS IS: ',avg/int(len(d)))