# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['B', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


#  This algorithm is similar to the substrings with no k identical elements in the array or list.

def count_fruits(fruits):
    fruitHashMap = {}
    window_start = 0 
    for index in range(len(fruits)):
        if fruits[index] not in fruitHashMap:
            fruitHashMap[fruits[index]] = 0 
        fruitHashMap[fruits[index]] += 1 
           
    for index , value in enumerate((fruits)):
        while (len(fruitHashMap) > 2 ):
            fruitHashMap[fruits[window_start]] -=1 
            if fruitHashMap[fruits[window_start]] == 0:
                del fruitHashMap[fruits[window_start]]
            window_start += 1

    print(index-window_start+1)

fruits_arr = ['A', 'B', 'C', 'B', 'B', 'A']
count_fruits(fruits_arr)
