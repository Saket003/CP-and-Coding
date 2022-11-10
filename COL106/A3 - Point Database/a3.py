class Node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None
        self.ylist = None
        self.isLeaf = False

class PointDatabase:
    def __init__(self,pointlist):
        '''
        Constructing a BST in x, and each points to a list sorted in y
        Requirements:
            MergeList
            BSTMaker1d
            BSTMaker2d
        '''
        self.nullcheck = 1
        self.nearbylist = []

        if(len(pointlist) == 0):
            self.nullcheck = 0
            return
        
        pointlist.sort()
        self.root = self.BSTMaker1d(pointlist)
        self.BSTMaker2d(self.root)


    #Check loop instead of recursion
    def BSTMaker1d(self,pointlist):
        if(len(pointlist)==0):
            return None
        if(len(pointlist)==1):
            node = Node(pointlist[0])
            node.isLeaf = True
            return node

        mid = (len(pointlist)-1)//2
        node = Node(pointlist[mid])
        node.left,node.right = self.BSTMaker1d(pointlist[:mid]), self.BSTMaker1d(pointlist[mid+1:])
        return node


    def BSTMaker2d(self,root):
        if(root.isLeaf):
            root.ylist = [root.value,]
            return

        if(root.left == None):
            self.BSTMaker2d(root.right)
            if(root.value[1]>root.right.value[1]):
                root.ylist = [root.right.value, root.value]
            else:
                root.ylist = [root.value,root.right.value]
            return
        
        #Check not needed - one element only case only on 2nd least layer
        #Check not needed - root.right never None

        self.BSTMaker2d(root.left)
        self.BSTMaker2d(root.right)
        #Find better way to add point
        root.ylist = self.MergeList(self.MergeList(root.left.ylist,root.right.ylist),[root.value,])
        return


    def MergeList(self,l1,l2):
        n1 = len(l1)
        n2 = len(l2)
        l3 = [None]*(n1+n2)
        i = 0
        j = 0
        k = 0

        while i < n1 and j < n2:
            if l1[i][1] < l2[j][1]:
                l3[k] = l1[i]
                k = k + 1
                i = i + 1
            else:
                l3[k] = l2[j]
                k = k + 1
                j = j + 1
        
        while i < n1:
            l3[k] = l1[i]
            k = k + 1
            i = i + 1
        
        while j < n2:
            l3[k] = l2[j]
            k = k + 1
            j = j + 1

        return l3

    #-------------------------------------- Query Related ---------------------------------

    def Find1d(self, ylist):
        ly = len(ylist)
        min = self.findNextHighest(ylist,self.y_min,0,ly-1)
        max = self.findNextSmallest(ylist,self.y_max,0,ly-1)
        if max<min:
            return []
        return ylist[min:max+1]

    #Check not exceed recursion stack
    def findNextHighest(self,ylist,x,start,end):
        mid = (start+end)//2

        if(end <= start):
            if(ylist[start][1]>x):
                return start
            else:
                return start + 1

        elif(ylist[mid][1]>x):
            return self.findNextHighest(ylist,x,start,mid-1)
        else:
            if(ylist[mid+1][1]>=x):
                return mid + 1
            else:
                return self.findNextHighest(ylist,x,mid+1,end)


    #Check not exceed recursion stack
    def findNextSmallest(self,ylist,x,start,end):
        mid = (start+end)//2

        if(end <= start):
            if(ylist[end][1]<x):
                return end
            else:
                return end - 1

        elif(ylist[mid][1]<x):
            return self.findNextSmallest(ylist,x,mid+1,end)
        else:
            if(ylist[mid-1][1]<=x):
                return mid - 1
            else:
                return self.findNextSmallest(ylist,x,start,mid-1)
    
    def SplitNode(self,root):
        #Check if should check equality since can be equal to x_min,x_max
        if (root.value[0] > self.x_min and root.value[0] < self.x_max):
            return root
        if (root.value[0] >= self.x_max):
            if(root.left == None):
                return None
            return self.SplitNode(root.left)
        if (root.value[0] <= self.x_min):
            if(root.right == None):
                return None
            return self.SplitNode(root.right)

    def withinRange(self,point):
        if(point[0]>self.x_min and point[0]<self.x_max and point[1]>self.y_min and point[1]<self.y_max):
            return True
        else:
            return False

    def searchNearby(self, q ,d):

        if(self.nullcheck == 0):
            return []
        self.nearbylist = []
        self.y_min = q[1] - d
        self.y_max = q[1] + d
        self.x_min = q[0] - d
        self.x_max = q[0] + d

        subroot = self.SplitNode(self.root)
        if subroot == None:
            return []
        if(self.withinRange(subroot.value)):
            self.nearbylist.append(subroot.value)
        if(subroot.left!=None):
            self.minTraversal(subroot.left)
        if(subroot.right!=None):
            self.maxTraversal(subroot.right)

        return self.nearbylist

    def minTraversal(self,root):
        if(root.value[0]>self.x_min):
            if(root.value[1]<self.y_max and root.value[1]>self.y_min):
                self.nearbylist.append(root.value)
            if(root.right!=None):
                self.nearbylist = self.nearbylist + self.Find1d(root.right.ylist)
            if(root.left!=None):
                self.minTraversal(root.left)
        else:
            if(root.right!=None):
                self.minTraversal(root.right)

    def maxTraversal(self,root):
        if(root.value[0]<self.x_max):
            if(root.value[1]<self.y_max and root.value[1]>self.y_min):
                self.nearbylist.append(root.value)
            if(root.left!=None):
                self.nearbylist = self.nearbylist + self.Find1d(root.left.ylist)
            if(root.right!=None):
                self.maxTraversal(root.right)
        else:
            if(root.left!=None):
                self.maxTraversal(root.left)