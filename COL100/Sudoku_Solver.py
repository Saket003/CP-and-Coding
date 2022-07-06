from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	return (1+int(((pos[0]-1)/3))*3+int(((pos[1]-1)/3)))

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	#check use get_block_num?
	return (1+3*((pos[0]%3)-1)+((pos[1]-1)%3))

def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	row = 3*(int((x-1)/3))
	col = 3*((x-1)%3)
	block=[]
	l1=[]
	for i in range (row,row+3):
		for j in range(col,col+3):
			block.append(sudoku[i][j])
	return block
	
def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here
	return ((sudoku[i-1]).copy())

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	list2=[]
	for i in range(0,9):
		l2=sudoku[i]
		list2.append(l2[(x-1)])
	return list2

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	# your code goes here

	for i in range (0,9):
		
		for j in range (0,9):
			if(sudoku[i][j]==0):
				return(i+1,j+1)
	return(-1,-1)

def valid_list(lst: List[int])-> bool:
	#lst2=lst.copy()
	'''
	lst.sort()
	for i in range (0,8):
		if(lst[i]!=0 and lst[i]==lst[i+1]):
			return False
	'''
	cnt=[0,0,0,0,0,0,0,0,0]
	for i in range (0,9):
		if(lst[i]==0):
			continue
		cnt[lst[i]-1] += 1
	for i in range (0,9):
		if(cnt[i]>1):
			return False
	return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	# your code goes here
	for i in range(1,10):
		if(valid_list(get_column(sudoku,i))==False or valid_list(get_row(sudoku,i))==False or valid_list(get_block(sudoku,i))==False):
			return False
	return True

def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	if(pos == (-1,-1)):
		return []
	l3=[]
	sudoku_copy = sudoku.copy()
	for i in range (1,10):
		sudoku_copy[pos[0]-1][pos[1]-1] = i
		if(valid_sudoku(sudoku_copy)==True):
		#if(valid_list(get_row(sudoku,pos[0])) and valid_list(get_column(sudoku,pos[1])) and valid_list(get_block(sudoku,get_block_num(sudoku,pos)))):
			l3.append(i)

	return l3

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1] = num
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	# your code goes here
	sudoku[pos[0]-1][pos[1]-1] = 0
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	# your code goes here

	# to complete this function, you may define any number of helper functions.
	# However, we would be only calling this function to check correctness.
	sudoku_copy2 = sudoku.copy()
	p=find_first_unassigned_position(sudoku)
	if(p==(-1,-1) and valid_sudoku(sudoku)):
		return (True,sudoku)
	
	if(p!=(-1,-1)):
		candid = get_candidates(sudoku,p)
		for each in candid:
			sudoku = make_move(sudoku,p,each)
			t = sudoku_solver(sudoku)
			if(t[0]==True):
				return(True,sudoku)
		undo_move(sudoku,p)
	return (False,sudoku)

# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))

# Following is the driver code
# you can edit the following code to check your performance.

if __name__ == "__main__":
	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	#in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)

