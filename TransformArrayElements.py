#  This was a question asked by a Microsft interviewer during a mock interview session organized by Ivy 


#  You receive an Mx N matrix 
#  you change the matrix such that if an element is 0 ,ist row and ,column become 0

# example 
# [ 
#   1 1 1
#   1 0 1
#   1 1 1
#        ]

# solution 
# [ 
#   1 0 1
#   0 0 0
#   1 0 1
#        ]

def swap_elements(matrix_2,row,col):
    for j in range(len(matrix)):

        if row-j >= 0 and col < len(matrix_2[0]): 
            matrix_2[row-j][col] = 0 # upward
        
        if row+j < len(matrix) and col < len(matrix_2[0]):
            matrix_2[row+j][col]  = 0  # downward
            
    for i in range(len(matrix[0])):
        if col-i >= 0 and row < len(matrix_2):
            matrix_2[row][col-i] = 0 # left
        if col+i < len(matrix[0]) and row < len(matrix_2):
            matrix_2[row][col+i] = 0 # right

def transform_matrix(matrix,matrix_2):
    row_matrix = len(matrix)
    col_matrix =len(matrix[0])

    matrix_2  
    for row_ in range(row_matrix):
        for col_ in range(col_matrix):
         
            if matrix[row_][col_] == 0:
#                 print(row_,col_).  # This prints the row and col for the zero element
                swap_elements(matrix_2,row_,col_)
    print(matrix_2)

if __name__ == "__main__":
    matrix = [[1,1,1],[1,1,1],[1,1,1],[1,1,0],[1,0,1],[1,1,1]]
    matrix_2 = [[1,1,1],[1,1,1],[1,1,0],[1,0,1],[1,0,1],[1,1,1]]
    transform_matrix(matrix,matrix_2)


# This will result in a time complexity of O(n^2) and a space complexity of O(nxm) because of the addition copy of the array used for the transformation. This can be improved to have a space complexity of O(1), by keeping trzck of the vidited columsn and skipping them in next iterations. 
#  This is a brute force approach to handle the problem.
