#budget check
#sum=0
#cart=[250,300,150,100,180]
#budget=1000
#for i in cart:
#    sum=sum+i
#if sum<=budget:
#    print("Under Budget")
#else:
#    print("Over Budget")

#name=input("Enter name:")
#present=["Amit","Sneha","Ravi","Priya","Zara"]
#if name in present:
#    print(name," is present")
#else:
#    print("not present")


#tup=(["Zara",15],["Ravi",22],["Amit",12],["Sneha",92],["Priya",120])
#for i in tup:
#    if i[1]>=1 and i[1]<13:
#        print(i[0]," is an Child")
#    elif i[1]>=20 and i[1]<65:
#        print(i[0]," is an Adult")
#    elif i[1]>=13 and i[1]<20:
#        print(i[0]," is an Teen")
#    elif i[1]>=65 and i[1]<=100:
#        print(i[0]," is a Senior")
#    elif i[1]>100:
#        print(i[0]," is Dead")
#di=dict(tup)
#print(di)

#stu={"Ravi":52,"Zara":75,"Sneha":93,"Amit":84}
#for i in stu.keys():
#   elif stu[i]>=75:
#        print("Grade B")
#    elif stu[i]>=60:
#        print("Grade C")
#    elif stu[i]<60:
#        print("Grade D")
#    else:
#        print("Invalid")

#list=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16]
#eve=0
#odd=0
#for i in list:
#    if i%2==0:
#        eve=eve+1
#    else:
#        odd=odd+1
#print("Even number: ",eve)
#print("Odd number: ",odd)

list=[1,1,2,3,4,4,6,6,7,4,8,9,1,-1,-1]
set1=set(list)
for i in set1:
    if list.count(i)>1:
        print(i)


clA=["Amit","Reena","Zara","Yash"]
clB=["Yash","Reena","Kunal","Farah"]
for i in clA:
    if i in clB:
        print(i)