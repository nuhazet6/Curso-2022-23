# ***********************
# SUMANDO CON ANIDAMIENTO
# ***********************


def sum_nested(items:list):
    if len(items) == 0:
        return 0
    current_item = items[0]
    if isinstance(current_item,list) :
        current_item = sum_nested(current_item)
    return current_item + sum_nested(items[1:])


