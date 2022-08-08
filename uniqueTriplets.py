# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
#  for all triplets theres a commmon  
#  To find all unique triplets : x+y+z =0 
# x+y = -z 


class Solution():
    def __init__(self, arr):
        self.arr = arr
        self.arr.sort()
        self.triplets = []
    def get_unique_value(self):
        
        for index in range(len(arr)-2 ):
            #  skip all duplicates or same elements
            if (index > 0  and arr[index] == arr[index-1] ):
                continue
            self.search_for_pairs(arr, -arr[index],index+1,self.triplets)
        return self.triplets    

    def search_for_pairs(self, arr, target_sum,left,triplets):
        
        right = len(arr)-1
        while(left < right ):
            checksum = arr[right] + arr[left]
            print(checksum,target_sum)
            if checksum == target_sum:
                print(checksum,"checksum")
                self.triplets.append([target_sum,arr[right],arr[left]])
                left = left+1
                right = right - 1
                while( left< right and arr[left] == arr[left-1]):
                    left = left+1 
                while( left < right and arr[right] == arr[right+1]):
                    right = right -1      
            elif (checksum > target_sum):
                right = right - 1
            else:
                left= left +1 
        











if __name__ == "__main__":
    arr = list(map(int,input().rstrip().split()))

    solution = Solution(arr)
    result = solution.get_unique_value()
    print(result)
