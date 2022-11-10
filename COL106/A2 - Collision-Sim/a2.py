#INF = float('inf')

class Node:
    def __init__(self,i,m1,x1,v1,m2,x2,v2,INF):
        self.posn = i
        self.m1 = m1
        self.x1 = x1
        self.v1 = v1
        self.m2 = m2
        self.x2 = x2
        self.v2 = v2
        self.tlc = 0 #Last collision time
        if((v1<=0 and v2>=0) or (v1*v2>0 and v2>=v1) or (v1==v2)):
            self.time = INF
            self.x = INF
        else:
            self.time = (x2-x1)/abs(v2-v1)
            self.x = x1+v1*self.time
        


def collision(node,D,P_Q,l,INF):  
    m1 = node.m1
    v1 = node.v1
    m2 = node.m2
    v2 = node.v2
    t = node.time
    vf1 = v1*((m1-m2)/(m1+m2)) + 2*v2*m2/(m1+m2)
    vf2 = 2*m1*v1/(m1+m2) - v2*((m1-m2)/(m1+m2))
    node.v1 = vf1
    node.v2 = vf2
    x = node.x
    node.x1 = x
    node.x2 = x
    node.time = INF
    node.x = INF
    node.tlc = t
    
    if(node.posn>0):
        a = P_Q[D[node.posn - 1]] #Type Node
        a.v2 = vf1
        a.x2 = x
        a.x1 = a.x1 + max(t-a.tlc,0)*(a.v1)
        a.tlc = t if a.tlc < t else a.tlc
        if(((a.v1<=0) and (a.v2>=0)) or (a.v1*a.v2>0 and a.v2>=a.v1)  or (a.v1==a.v2)):
            a.time = INF
            a.x = INF
        else:
            if(t==INF):
                a.time = (a.x2-a.x1)/abs(a.v2-a.v1)
            else:
                a.time = t + (a.x2-a.x1)/abs(a.v2-a.v1)
            if(x == INF):
                a.x = vf1*(a.x2-a.x1)/abs(a.v2-a.v1)
            else:
                a.x = x + vf1*(a.x2-a.x1)/abs(a.v2-a.v1)
        heap_up(P_Q,D,D[node.posn - 1],l)

    if(node.posn<l-2):
        a = P_Q[D[node.posn + 1]] #Type Node
        a.v1 = vf2
        a.x1 = x
        a.x2 = a.x2 + max(t-a.tlc,0)*(a.v2)
        a.tlc = t if a.tlc < t else a.tlc
        if((a.v1<=0 and a.v2>=0) or (a.v1*a.v2>0 and a.v2>=a.v1) or (a.v1==a.v2)):
            a.time = INF
            a.x = INF
        else:
            if(t==INF):
                a.time = (a.x2-a.x1)/abs(a.v2-a.v1)
            else:
                a.time = t + (a.x2-a.x1)/abs(a.v2-a.v1)
            if(x == INF):
                a.x = vf2*(a.x2-a.x1)/abs(a.v2-a.v1)
            else:
                a.x = x + vf2*(a.x2-a.x1)/abs(a.v2-a.v1)
        heap_up(P_Q,D,D[node.posn + 1],l)
    
    heap_down(P_Q,D,0,l,INF)

    return x,t

def build_heap(M,x,v,l,INF):
    P_Q = [None]*(l-1)
    node = Node(0,M[0],x[0],v[0],M[1],x[1],v[1],INF)
    P_Q[l-2] = node

    for i in range (1,l-1):
        node = Node(i,M[i],x[i],v[i],M[i+1],x[i+1],v[i+1],INF)
        index = l-2-i
        P_Q[index] = node

        while(2*(index)+1<l-1):
            left = P_Q[2*(index+1)-1]
            right = P_Q[2*(index+1)] if 2*(index+1)<l-1 else INF
            l_time = left.time
            r_time = right.time if 2*(index+1)<l-1 else INF
            if(l_time<r_time and l_time<node.time):
                P_Q[index] = left
                P_Q[2*index + 1] = node
                index = 2*index + 1

            elif(r_time<l_time and r_time<node.time):
                P_Q[index] = right
                P_Q[2*(index+1)] = node
                index = 2*index + 2
            else:
                break

    return P_Q


def store_index(P_Q,l):
    D = [None]*(l-1)
    for i in range (0,l-1):
        D[P_Q[i].posn] = i
    return D


def heap_down(P_Q,D,index,l,INF):
    while(index<l-1):
        parent = P_Q[index]
        left = P_Q[2*index + 1] if 2*index+1<l-1 else INF
        right = P_Q[2*index + 2] if 2*index+2<l-1 else INF
        l_time = left.time if 2*index+1<l-1 else INF
        r_time = right.time if 2*index+2<l-1 else INF

        if(l_time<r_time and l_time<parent.time):
            D[parent.posn] = 2*index+1
            D[left.posn] = index
            P_Q[index] = left
            P_Q[2*index+1] = parent
            index = 2*index + 1

        elif(r_time<l_time and r_time<parent.time):
            D[parent.posn] = 2*index+2
            D[right.posn] = index

            P_Q[index] = right
            P_Q[2*index+2] = parent
            index = 2*index + 2

        elif(l_time==r_time and l_time<parent.time):
            if(left.posn<right.posn):
                D[parent.posn] = 2*index+1
                D[left.posn] = index
                P_Q[index] = left
                P_Q[2*index+1] = parent
                index = 2*index + 1
            else:
                D[parent.posn] = 2*index+2
                D[right.posn] = index
                P_Q[index] = right
                P_Q[2*index+2] = parent
                index = 2*index + 2

        else:
            break
    return

def heap_up(P_Q,D,index,l):
    while(index>2):# Ensures does not interfere with 0
        child = P_Q[index]
        parent = P_Q[(index-1)//2]
        p_posn = parent.posn
        c_posn = child.posn
        if(parent.time>child.time):
            P_Q[(index-1)//2] = child
            P_Q[index] = parent
            D[p_posn] = index
            D[c_posn] = (index-1)//2
            index = (index-1)//2
        else:
            break
    return


def listCollisions(M,x,v,m,T):
    l = len(M)
    if(l==1):
        return []
    P_Q = build_heap(M,x,v,l,T+1)
    D = store_index(P_Q,l) #Behaves as a dictionary mapping to store indices

    Answer = []
    collisions = 0
    while(collisions<m):
        i_collision = P_Q[0].posn
        x_collision,t_collision = collision(P_Q[0],D,P_Q,l,T+1)
        if(t_collision>T):
            break
        Answer.append((t_collision,i_collision,x_collision))
        collisions = collisions + 1
    
    Answer.sort()
    Final = []
    for x in Answer:
        Final.append((round(x[0],4),round(x[1],4),round(x[2],4)))
    return(Final)