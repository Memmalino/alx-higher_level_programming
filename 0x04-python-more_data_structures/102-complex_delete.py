#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """complex delete in a dictionary

    Args:
        a_dictionary: the dictionary
        value in the dictionary

    Returns:
        the dictionary with change value
    """
    keys_to_delete = []

    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
