#  This is to solve a two sums problem 

#  [ 2 , 3 ,5 ]  target = 8 
#  nums[index] +nums[index+x] = target ; x as index + n-1
#  target - nums[index] = nums[index+x]
#  search for the nums[index+x]
#  return the index of that element 




class Solution:
    def search_remainder(self, left ,right, search_target, nums):
        if search_target in nums[left:right]:
            return nums[left:right].index(search_target)+left 


    def two_sum(self , nums,target ):
        for index in range(len(nums)):
            search_element = target-nums[index]

            result = self.search_remainder(index+1, len(nums),search_element,nums)

            if result :
                if nums[index]+ nums[result] == target:
                    return  [index, result]





if __name__ == '__main__':
    target = int(input())
    nums= list(map(int,input().rstrip().split()))

    solution = Solution()
    results = solution.two_sum(nums,target)
    print(results)
