

#  The time complexity of the solution is O(N) where N is the number od elements in the array 

#  Then the space complexity would be O(N) where N is the number of elements stored in the square array 


class Solution():
    def __init__(self,arr):
        self.arr = arr 

    def square_arrs(self):
        square_length = len(arr)-1
        square =[0]*len(arr)
        left = 0
        right = len(arr)-1
        while left < right:
            left_square = arr[left]**2
            right_square = arr[right]**2
            if left_square > right_square:
                square[square_length] = left_square
                left = left +1 
            else:
                square[square_length] = right_square
                right= right -1 
            square_length = square_length -1 

        return square

if __name__ == '__main__':
    arr = list(map(int,input().rstrip().split()))
    solution= Solution(arr)
    results = solution.square_arrs()
    print(results)