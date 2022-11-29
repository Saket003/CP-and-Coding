import pickle
import a5
import time

#Will not check for valid paths or not

print("Opening files (not path checked) ...")
f = open("testcase1.bin","rb")
x1 = pickle.load(f)
f = open("testcase2.bin","rb")
x2 = pickle.load(f)
f = open("testcase3.bin","rb")
x3 = pickle.load(f)
print("Files successfully opened!")
print("")

print("Basic cases starting ...")
y1 = a5.findMaxCapacity(x1[0],x1[1],x1[2],x1[3])
if(y1[0] == 9068):
    print("TC 1 Passed")
    print("Your Path: ",y1[1])
    print("Paths till now: [30, 67, 60, 69]")
else:
    print("TC 1 Failed")
print("")
x1 = None

y2 = a5.findMaxCapacity(x2[0],x2[1],x2[2],x2[3])
if(y2[0] == 992600):
    print("TC 2 Passed")
    print("Your Path: ",y2[1])
    print("Paths till now: (Way too many paths, just check endpoints)")
    print("[581, 35, 492, 365, 554, 91, 249, 259, 391, 52, 61, 353, 262, 131, 127, 68, 208, 136, 255, 73, 325, 233, 98, 187, 312, 25, 3, 173, 772]")
    print("[581, 35, 661, 92, 341, 429, 110, 772]")
        
else:
    print("TC 2 Failed")
print("")
x2 = None

print("Large cases starting ...")

st = time.time()
y3 = a5.findMaxCapacity(x3[0],x3[1],x3[2],x3[3])
print("Time taken:",time.time() - st)
if(y3[0] == 99961228):
    print("TC 3 Passed")
    print("Your Path: ",y3[1])
else:
    print("TC 3 Failed")

x3 = None
print("")

print("Opening files (path checked) ...")
f = open("testcase4.bin","rb")
x4 = pickle.load(f)
print("Files successfully opened!")
print("")

st = time.time()
y4 = a5.findMaxCapacity(x4[0],x4[1],x4[2],x4[3])
if(y4[0] == 999136):#
    print("TC 4 Passed")
    print("Your Path: ",y4[1])
    print("Checking Path:",end="")
    x = 0
    for i in range (len(y4[1])-1):
        a = y4[1][i]
        b = y4[1][i+1]
        wt = x4[1][1000*(min(a,b)-1) + (max(a,b)-min(a,b)-1)][2]
        if(wt>999136):
            print("TC4 Path Invalid")
            x = 1
            break
    if(x==0):
        print("TC4 Path Valid")
else:
    print("TC 4 Failed")