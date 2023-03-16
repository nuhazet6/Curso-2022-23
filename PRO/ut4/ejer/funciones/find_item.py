def find_item(numbers: tuple, value: int) -> int:
    """Count the number of ocurrences of target in items.
    The operation is:
        1. Return the len of a list with the items from numbers equals to the value
    :param items: Numbers to compare with the value
    :type items: tuple
    :param value: number to found in the tuple numbers
    :type value: int
    :return: times that value is founded in numbers
    :rtype: int
    """
    return len([i for i in numbers if value == i])


print(find_item((3, 4, 1, 2, 3, 1, 2, 1, 5, 1), 1))
