#  solving two pointer questions 

# Given an array of sorted elements find the number of non-duplicate element in-place.
# [2 , 3, 3, 3, 6, 9,9]
# the return array will be [ 2, 3,6,9] return 4 as the result 
 
# time complexity of O(n) - linear time 
#  space complexity of of O(1) - constant time 


class Solution():
    def __init__(self,arr):
        self.arr = arr

    def remove_duplicates_sorted(self):
        non_duplicate_pointer= 1
        for index in range(1,len(arr)):
            if arr[non_duplicate_pointer-1] != arr[index]:
                arr[non_duplicate_pointer] = arr[index]
                non_duplicate_pointer= non_duplicate_pointer+1
        return non_duplicate_pointer        

    def remove_duplicates_unsorted(self, key):
        non_duplicate_pointer= 0

        for index in range(0,len(arr)):
            if arr[index] != key:
                arr[non_duplicate_pointer] = arr[index]
                non_duplicate_pointer = non_duplicate_pointer+1
        print(arr)        
        return non_duplicate_pointer   



        







if __name__ == '__main__':
    arr = list(map(int,input().rstrip().split())) 

    solution = Solution(arr)
    result = solution.remove_duplicates_unsorted(5)    
    print(result)   