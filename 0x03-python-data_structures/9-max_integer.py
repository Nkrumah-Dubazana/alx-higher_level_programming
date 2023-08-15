#!/usr/bin/Python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
   
   else:
       maxi = my_list[0]
       for num in range(len(my_list)):
        if my_list[num] > maxi:
            maxi = my_list[num]

        return maxi
