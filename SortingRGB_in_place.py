# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

#  This makes sure all values of R are placed in the first section of the array before G 
#  At the end of the first iteration, G will be rightly swaped to it sorted position at the end of the iteration.
def swap (value1, value2,arr):
    arr[value1], arr[value2] = arr[value2], arr[value1]


def segregate_string(arr):  
    start = 0 
    index = 0 
    end = len(arr)-1

    while( index <= end and start < end ):
        if arr[index] == "R":
            arr[index], arr[start] = arr[start], arr[index]
            start +=1 
            index += 1
        elif arr[index] == "B":
            arr[index] , arr[end] = arr[end] , arr[index]  
            end -= 1
        else : 
            index +=1     




#  this an inplace algorithm the runs in one pass and ensures the increase in time of the computation

    # The non-optimized version of the code 
    # length_ = len(arr)
    # window_start = 0 
    # for window_end in range(length_):
    #     if arr[window_end] == 'R':
    #         swap(window_start,window_end,arr)
    #         window_start += 1 

    # for window_end in range(length_):
    #     if arr[window_end] == 'G':
    #         swap(window_start,window_end,arr)
    #         window_start +=1       

    return arr


arr_value_  = ['G','B','R', 'R', 'B', 'R', 'G']
result = segregate_string(arr_value_)
print(result)


#  The time complexity is O(n) 
#  the space complexity is O(1) -- reason; I did not add any additional data structure for computing the algorithm, hince we have a constant space complexity 
