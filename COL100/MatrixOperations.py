def Create(rows:int,cols:int):
	A=[]
	for i in range (0,rows):
			A.append([])
			for j in range (0,cols):
				A[i].append(0.00)
	return A


def PrintMatrix(A:list):
	if A == None:
		print(A)
		return
	rows = len(A)
	cols = len(A[0])
	for i in range(rows):
		for j in range(cols):
			print(A[i][j], end = " ")
		print()


def CheckMatrix(A: list)->bool:
	x=True
	if(len(A)==0):
		x = False
	if (x==True):
		if(len(A[0])>0):
			row = len(A[0])
			for i in range (1,len(A)):
				if(row!=len(A[i])):
					x = False
		else:
			x = False
	if (x==True):
		rows = len(A)
		cols = len(A[0])
		for i in range(0,rows):
			for j in range(0,cols):
				if(type(A[i][j])!=float):
					x = False
	
	return x


def Transpose(A:list) -> list:
	if (CheckMatrix(A)==True):
		rows = len(A[0])
		cols = len(A)
		B = Create(rows,cols)

		for i in range (0,rows):
			for j in range (0,cols):
				B[i][j]=A[j][i]
		return (B)
	else:
		return None


def Multiplication(A:list,B:list) -> list:
	if (CheckMatrix(A)==True and CheckMatrix(B)==True):
		if(len(A[0])!=len(B)):
			return None
		rows = len(A)
		cols = len(B[0])
		C = Create(rows,cols)

		for i in range (0,rows):
			for j in range (0,cols):
				for k in range (0,len(B)):
					C[i][j] = C[i][j] + (A[i][k]*B[k][j])
		return C
	else:
		return None


def Addition(A:list,B:list) -> list:
	if (CheckMatrix(A)==True and CheckMatrix(B)==True):
		if(len(A)!=len(B) or len(A[0])!=len(B[0])):
			return None
		rows = len(A)
		cols = len(A[0])
		C = Create(rows,cols)

		for i in range (0,rows):
			for j in range (0,cols):
				C[i][j] = A[i][j] + B[i][j]
		return C
	else:
		return None


def Symmetric(A: list)->bool:
	if(CheckMatrix(A)==False):
		return False
	if(len(A)!=len(A[0])):
		return False
	x = True
	for i in range (0,len(A)):
		for j in range (0,len(A)):
			if (A[i][j]!=A[j][i]):
				x = False
	return x