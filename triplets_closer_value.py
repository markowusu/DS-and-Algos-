 # Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# [ -3 -1 1 2 ]... key = 1  ==> [-3 1 2 ]
# [-3 -1 1 2 ]
import sys
class Solution():
    def __init__(self,arr, key):
        self.arr = arr 
        self.key = key 
        self.arr.sort()
    max_triple_sum = sys.maxsize
    def search_triplets_pair(self ,arr, target_sum, left):
       
        right = len(arr)-1 
        while left < right :
            
            target_diff = self.key - arr[right]- arr[left]-target_sum
            if target_diff == 0:
                return  self.key- target_diff
            if abs(target_diff) < abs(self.max_triple_sum) or abs(target_diff) ==abs(self.max_triple_sum) and target_diff > self.max_triple_sum:
                self.max_triple_sum = target_diff
            if target_diff > 0:
                left = left +1 
            else :
                right = right +1     
           
        
    
    def triplet_closets_sum(self):
        
        for index in range(len(self.arr)):
           
            self.search_triplets_pair(self.arr,self.arr[index],index+1)
        return((self.key - self.max_triple_sum)  )  

    
if __name__ == '__main__':
    key = int(input())
    arr = list(map(int,input().rstrip().split()))

    solution = Solution(arr,key)
    results = solution.triplet_closets_sum() 
    print(results)