import os
import sqlite3 as sql
con=sql.connect("restaurent")
print("connection established")
curs=con.cursor()
lists=[]
total=0
print("The Tiffine list :")
print("sno item   cost")
print("1 idli      50.0\n2 pesarattu 70.0\n3 parota    55.0\n4 upma      40.0\n5 puri      45.0\n6 chapati   30.0\n7 dosa      45.0\n8 bonda     60.0")
ch="y"
while ch=="y":
    item=input("enter item id:")
    q="select  itemname,cost  from hotel where itemid=?"
    data=(item,)
    curs.execute(q,data)
    j=curs.fetchall()
    if len(j)>0:
        item=j[0][0]
        cost=j[0][1]
        print("itemname :",item)
        print("cost    :",cost)
        quantity=int(input('enter quantity :'))
        billamount=quantity*cost
        print("current bill is:",billamount)
        total=total+billamount
        lists.append([item,cost,quantity,billamount])
        ch=input("if you wnat to add otehr item(y/n):")  
    else:
        print("item  not available")
        print("please enter correct item given in the list ex:1,2,3,4,5:")
        item=input("if you wnat to continue plese enter ""y"" else ""n"":")
        if item=="y":
            pass
        else:
            break
print('name          cost        quantity          amount')
for i in lists:
    for j in i:
        print(j,end='\t\t')
    print()     
print("--------------------------------------")          
print("total amount is:",total)
cgst=total*(2.5/100)
sgst=total*(3.5/100)
print("cgst is:",cgst)  
print("sgst is:",sgst)
bill=total+cgst+sgst
print("bill amount:",bill)
if bill>500:
    print("your bill crossed 500 you will get 20% off")
    discount=bill*(20/100)
    print("discount amount :",discount)
print("FINAL BILL IS :",bill-discount)    
con.close()
    
