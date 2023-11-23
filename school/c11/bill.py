items = int(input("no of item to buy: "))
bill={}
for i in range(items):
    details={}
    prodname = input("product name ")
    prodprice = int(input("price "))
    prodqty = int(input("qty "))
    details['Name']=prodname
    details['Quantity']=prodqty
    details['Price']=prodprice
    bill[i+1]=details
print(f"{'SNo.':<15}{'Product':<15}{'Quantity':<15}{'Price':<15}{'Amount':<15}")
for x in range(items):
    qty = bill[(x+1)]['Quantity']
    prc = bill[(x+1)]['Price']
    print(f'''{x:<15}{bill[x+1]['Name']:<15}{bill[x+1]['Quantity']:<15}{bill[x+1]['Price']:<15}{qty*prc:<15}''')