#!/usr/bin/python3
def weight_average(my_list=[]):
    """print average of a list

    Args:
        my_list: the list

    Returns:
        the average
    """
    new_list = []
    increement = 0
    if len(my_list) == 0:
        return (0)
    for i in my_list:
        new_list.append(i[0] * i[1])
        increement += i[1]
    return (sum(new_list) / increement)
