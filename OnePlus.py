

#  iteate over the list in  a reverse order 
#  for each index and value  I add  1 to the current value and I get the modulo 10 of that result. This gives me the last value of the result. which should be the same value when it is a single digit 
#  I then add the modulo 10 value to the current index 
# Also, i calculate the carry of the result which should be (item + carry ) // 10 

# cominf out of the for loop I check for the existence of a carry number which if exist will result to a one or checking it to be a true and concating the carry in a list to the nums integer array 
#  else : I just return the digist 




class Solution:

    def one_plus(self,nums):
        carry = 1 
        for index, item in reversed(list(enumerate(nums))):
            nums[index] = (item+carry) % 10 
            carry = (item + carry ) // 10 


        if carry : 
            nums = [carry ]  + nums   
        return nums     


        


if __name__ == '__main__':
    nums = list(map(int,input().rstrip().split()))

    solution = Solution()
    results = solution.one_plus(nums)
    print(results)

