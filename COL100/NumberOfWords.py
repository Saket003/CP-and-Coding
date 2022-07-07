def numwords(a):
    a[0] = a[0].replace(","," ")
    a[0] = a[0].replace("."," ")
    min = len(a[0].split())
    for x in a:
        x = x.replace(","," ")
        x = x.replace("."," ")
        l = len(x.split())
        if(min>l):
            min=l
    return(min)
    

n = int(input())
a = []

for i in range (0,n):
    a.append(input())

print('%.2f' %(numwords(a)))