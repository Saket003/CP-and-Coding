import random
import pickle

N = 1000
l = []

#No. of vertices
for i in range(N):
    if i!= N-1: l.append((i,i+1,1))
    for j in range(i+2,N):
        if(True):#random.randint(0,1)
            x = random.randint(1,N*N)
            l.append((i,j,x))

f = open("testcase4.bin","wb")
list = [N,l,random.randint(0,N-1),random.randint(0,N-1)]
pickle.dump(list,f)
f.close()