a = []

def PickPlate():
    if (len(a)>0):
        del a[len(a)-1]
    else:
        print("Invalid")
    return

def AddPlate(PlateID: int):
    a.append(PlateID)
    return


def Check():
    if (len(a)>0):
        print(a[len(a)-1])
    else:
        print("Invalid")
    return


n = int(input())
l = []
for i in range (0,n):
    l.append(input())

for i in range (0,n):
    if(l[i]=="Check"):
        Check()
    if(l[i]=="PickPlate"):
        PickPlate()
    s = l[i].split()
    if(s[0]=="AddPlate"):
        AddPlate(s[1])