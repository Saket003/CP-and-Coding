#Class to define Stack data structure
class Stack:
    def __init__(self):
        self.INITIAL_SIZE = 4
        self._data = [None]*self.INITIAL_SIZE
        #Constructed using a list, with default value set to NoneType
        self._index = 0 
        self._size = 0
        #Stores index of top of Stack
        
    def push(self, n):
        #If size limit is reached, doubles size of list and copies existing elements to new list
        if(self._index >= self.INITIAL_SIZE):
            self.INITIAL_SIZE = 2*self.INITIAL_SIZE
            copy = [None]*self.INITIAL_SIZE
            for i in range(0,self.INITIAL_SIZE//2):
                copy[i] = self._data[i]
            self._data = copy
        self._data[self._index] = n
        self._index = self._index + 1
        self._size = self._size + 1
  
    def top(self):
        return self._data[self._index-1]

    def __len__(self):
        return(self._size)

    def is_empty(self):
        return(self._size == 0)

    def pop(self):
        self._data[self._index-1] = None
        #Top of Stack removed by discarding value and replacing by NoneType
        self._index = self._index - 1
        self._size = self._size - 1


def findPositionandDistance(P):
    
    if(P == ""):
        return [0,0,0,0]
    #Deals with empty string

    Value = Stack() 
    #Stores [x,y,x,d] in progress, with each entry corresponding to that level in brackets
    Multiplier = Stack() 
    #Stores the multiplying factor for that bracket

    if(P[0]=='('):
        P = '1' + P
    else:
        P = '1'+'(' + P+ ')'
    #Converts to a standard form where all operations must lie within multiplying factor and bracket

    x = y = z = d = 0
    #Stores progress in corresponding variables
    temp = 0
    #Multi-purpose variable used to store addition/subtraction/multiplying factor
    P_len = len(P)
    bracket_count = 0
    #Increments on ( and decrements on )

    for i in range (0,P_len):

        if(P[i]=='+'):
            temp = 1
        elif(P[i]=='-'):
            temp = -1
        elif(P[i]=='X'):
            x = x + temp
            d = d + 1
            temp = 0
        elif(P[i]=='Y'):
            y = y + temp
            d = d + 1
            temp = 0
        elif(P[i]=='Z'):
            z = z + temp
            d = d + 1
            temp = 0
        #Deals with operations of *A type(* = +,- ; A = X,Y,Z)


        elif(P[i]=='('):
            if(bracket_count==len(Value)):
                Value.push([x,y,z,d])
                Multiplier.push(temp)
            else:
                temp_val = Value.top()
                temp_val[0] = temp_val[0] + x
                temp_val[1] = temp_val[1] + y
                temp_val[2] = temp_val[2] + z
                temp_val[3] = temp_val[3] + d
                Value.pop()
                Value.push(temp_val)
                Multiplier.push(temp)
            
            bracket_count = bracket_count + 1
            x = y = z = d = 0
            temp = 0
        
        elif(P[i]==')'):
            bracket_count = bracket_count - 1
            temp_val = Multiplier.top()
            Multiplier.pop()
            temp2_val = Value.top()
            Value.pop()
            if(bracket_count==len(Value)):
                temp2_val[0] = temp2_val[0] + temp_val*x
                temp2_val[1] = temp2_val[1] + temp_val*y
                temp2_val[2] = temp2_val[2] + temp_val*z
                temp2_val[3] = temp2_val[3] + temp_val*d
                Value.push(temp2_val)
            else:
                temp3_val = Value.top()
                Value.pop()
                temp3_val[0] = temp3_val[0] + temp_val*temp2_val[0] + temp_val*x# removed + wala
                temp3_val[1] = temp3_val[1] + temp_val*temp2_val[1] + temp_val*y
                temp3_val[2] = temp3_val[2] + temp_val*temp2_val[2] + temp_val*z
                temp3_val[3] = temp3_val[3] + temp_val*temp2_val[3] + temp_val*d
                Value.push(temp3_val)
            x = y = z = d =  0
        #Deals with nesting of brackets
        #tempi_val - temporary variable which stores list

        
        else:
            temp = temp*10 + int(P[i])
        #Calculates multiplying factor
    return Value.top()