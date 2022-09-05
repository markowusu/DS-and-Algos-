
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        if(len(nums) == 0 ):
            return 0 
        
        index = 0 
        start = 0 
        end = len(nums)-1 
        
        while(index <= end and start < end ):
            if nums[index] == 0 :
                nums[index], nums[start] = nums[start], nums[index]
                start +=1 
                index += 1 
            elif nums[index] == 2:
                nums[index],nums[end] = nums[end], nums[index]
                end -=1 
            else: 
                index +=1 
        
        
        return nums
        
        
        
if __name__ == '__main__':       
    sort_colors = [2,0,2,1,1,0]  
    solution = Solution()      
    result = solution.sortColors(sort_colors)  
    print(result)

        
        
        
        
        
        
        #  The non-optimized version of the solution.  
#         window_start  = 0 
#         for colors in range(len(nums)):
            
#             if nums[colors] == 0 :
#                 nums[colors], nums[window_start] = nums[window_start], nums[colors]
#                 window_start += 1 
#         for colors in range(len(nums)):
#             if nums[colors] == 1 :
#                 nums[colors], nums[window_start] = nums[window_start], nums[colors]
#                 window_start += 1 
                
        
