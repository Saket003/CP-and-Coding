a = []

def Highest():
    max=(a[0])[1]
    maxI=0
    for i in range(0,len(a)):
        b = a[i]
        if(b[1]>max):
            max = b[1]
            maxI = i
    return maxI

def Order(orderID: int, BillValue:int):
    a.append([int(orderID),int(BillValue)])
    return

def Serve():
    del a[Highest()]
    return


n=int(input())
l = []
for i in range (0,n):
    l.append(input())

for i in range (0,n):
    if (l[i]=="Serve"):
        if (len(a)>0):
            Serve()
        else:
            print("Invalid")
    elif (l[i]=="Highest"):
        if (len(a)>0):
            print((a[Highest()])[0])
        else:
            print("Invalid")
    else:
        c=l[i].split()
        Order(int(c[1]),int(c[2]))