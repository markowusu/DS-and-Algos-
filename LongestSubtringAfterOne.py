#  This is the longest substring after one .


# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.


#  [ 0 1 1 1 0 1 1 1 0 ] k =2 
#  This is a sliding window problem  where we are going to have a start window value and an end window value.  we wil move through every element of the array and check the number of 0's in the current subarry. We also persist the max number of 1's in the substring and check if the number of 0's in the subtring which can be replaced is no more than the k values 
 

#  this problem will use a sliding window solution 
#  I count the number of ones in a window section and persit it 
#  for every window, I make sure I have the same number of replaceale ones which are allowed to be replaced with a 1.
#  If the number of replaceable o's are more than k, then I shrink the string by increasing the start window . 

# [ 1 0 1 0 0 0]
class Solution:
    def __init__(self,arr,k):
        self.arr = arr 
        self.k = k 

    def get_longest_subtring(self):
        window_start = 0
        max_length = 0 
        max_ones_count = 0 
        for window_end in range(len(arr)):
            if arr[window_end] == 1:
                max_ones_count += 1 
            replaceable_zeros = window_end-window_start +1 - max_ones_count

            if replaceable_zeros > k:
                if arr[window_start] == 1:
                    max_ones_count -=1 
                window_start += 1    

            max_length = max(max_length, window_end-window_start+1)

        return max_length




if __name__ == "__main__":
    k = int(input())
    arr = list(map(int,input().rstrip().split()))
    solution = Solution(arr,k)
    results = solution.get_longest_subtring()
    print(results)
    





















# class Solution:
#     def __init__(self,arr, k ):
#         self.arr = arr 
#         self.k = k

#     def get_longest_subtring(self):

        
#         window_start = 0 
#         max_ones_count = 0 
#         max_length = 0 
#         for window_end in range(len(arr)):
#             if arr[window_end] == 1:
#                 max_ones_count +=1 

#             replaceable_zeros = window_end - window_start+1 - max_ones_count 
#             if replaceable_zeros > k:
#                 if arr[window_start] == 1 :
#                     max_ones_count -=1
#                 window_start += 1    
#             max_length = max(max_length,window_end- window_start+1)

#         return max_length




# if __name__ == "__main__":
#     k = int(input())

#     arr = list(map(int,input().rstrip().split()))

#     solution = Solution(k,arr)
#     results = solution.get_longest_subtring()
#     print(results)