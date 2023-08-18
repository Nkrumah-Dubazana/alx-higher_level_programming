#!/usr/bin/python3

def search_replace(my_list, search, replace):

    """
    Function that replaces an element of an element by another in a new list

    """

    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

        return new_list


