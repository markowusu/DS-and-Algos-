# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]



def position_(target,arr_):
    right = len(arr_)
    left = 0
    pivot = left+(right-left)//2

    while(left < right ):
     
        if target == arr_[pivot]:
            return pivot 
        if target > arr_[pivot]:
            left = pivot+1 
        else:
            right= pivot-1    
        pivot = left+(right-left)//2

target= 8
arr_ = [6,7,7,8,8,10]
first_position = position_(target,arr_) 
if arr_[first_position-1] == target:
    print(first_position-1,first_position)
else:
     print(first_position,first_position+1)

 




