# Find Minimum in Rotated Sorted Array
#  Suppose you are given an array sorted in ascending order and rotated at some pivot that is not known to you beforehand.
#  An example will be [ 1,2 ,3 ,4 5, 6, 7] and the rotation being at [ 3,4, 5 ,6 ,7, 0,1, 2 ]

#  Logic on how you will approach this question.
#  Checking the rotated array all the elements are greater than the values that come before it except for the minium value in the array. This brings to the point that we need. to search for the minimum element based on the condition the value before it  is greater than it. i.e for 7 and 0, 0 is less than 7.



def find_Min_Element(nums):
    #  special condition:
    # when there's no value we return negative one. 

    if len(nums) < 0 : 
        return -1 

    # Binary search is used to find the minimum element 

    left = 0
    right = len(nums)-1

    while( left <= right ):
        mid_point = left + (right-left) // 2 

        if nums[mid_point] < nums[mid_point-1]:
            return nums[mid_point]
        elif (mid_point > 0 and nums[left] <= nums[mid_point] and nums[mid_point] > nums[right] ) :
            left= mid_point +1
        else: 
            right = mid_point -1      


nums = [4, 5,6,7,0,1,2,3]
print(find_Min_Element(nums))
