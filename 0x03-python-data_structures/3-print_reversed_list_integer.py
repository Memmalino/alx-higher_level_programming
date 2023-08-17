#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print list in reverse order

    Args:
        my_list: the list to reverse

    Returns:
        Null
    """
    if my_list is None:
        return ('')
    if len(my_list) == 0:
        return ('')
    length = len(my_list) - 1
    while length >= 0:
        print("{}".format(my_list[length]))
        length -= 1
