""""
This is a docstring for the module:
this module demonstrates the solution of merge problem
"""


def move_zeros_to_right(main_arr):
    """"
    This method helps to move zeros to the right in the list
    """
    arr = main_arr[:]
    if len(arr) < 2:
        return arr

    p_1 = 0
    p_2 = 0

    while p_2 < len(arr):
        if arr[p_2] == 0:
            p_2 += 1
        else:
            temp = arr[p_1]
            arr[p_1] = arr[p_2]
            arr[p_2] = temp
            p_1 += 1
            p_2 += 1
    return arr


def merge(arr):
    """"
    This method helps to merge numbers in the list
    """

    # move all zeros to right
    ordered_list = move_zeros_to_right(arr)

    index = 0
    # merge numbers in list
    while index < len(ordered_list)-1:
        if ordered_list[index] != 0 and ordered_list[index+1] != 0:
            if ordered_list[index] == ordered_list[index+1]:
                ordered_list[index] = 2 * ordered_list[index]
                ordered_list[index+1] = 0
                index += 2
            else:
                index += 1

    # move all zeros to right again
    new_ordered_list = move_zeros_to_right(ordered_list)

    return new_ordered_list
