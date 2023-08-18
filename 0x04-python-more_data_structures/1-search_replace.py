def search_replace(my_list, search, replace):
    """
    Function that adds all unique
    integers in a list
    
    """

    unique_list = []
    total_sum = 0
    for num in my_list:
        if num != unique_list:
            total_sum += num
            unique_list.append(num)
        return total_sum
