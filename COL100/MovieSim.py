l=[]

def Issue():
    if(len(l) >0):
        l.pop(0)
    else:
        print("Invalid")
    return

def Join(AadharID: int):
    l.append(AadharID)
    return


def Check():
    if(len(l) >0):
        print(l[0])
    else:
        print("Invalid")
    return

def GetLine():
    if(len(l) >0):
        for each in l:
            print(each,end=" ")
        print()
    else:
        print("Invalid")
    return

n = int(input())
a = []
for i in range (0,n):
    a.append(input())

for i in range (0,n):
    if(a[i]=="Check"):
        Check()
    if(a[i]=="GetLine"):
        GetLine()
    if(a[i]=="Issue"):
        Issue()
    s = a[i].split()
    if(s[0]=="Join"):
        Join(int(s[1]))