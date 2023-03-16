# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


# def consecutive_seq(items:list,target_count:int,last_number:int=None,current_count:int=1):
#     if len(items) == 0:
#         return False    
#     current_number = items[0]
#     if last_number == current_number:
#         current_count+=1
#     else:
#         current_count=1
#     if current_count == target_count:
#         return current_number
#     return consecutive_seq(items[1:],target_count,current_number,current_count) #Target count siempre es lo mismo, así que podríamos hacer que todo lo que cambia pase a una función interior como hago abajo:

def consecutive_seq(items:list,target_count:int):
    def helper(current_items:list,current_count:int=1,last_number:int=None):
        if len(current_items) == 0:
            return False
        current_item = current_items[0]
        if last_number == current_item:
            current_count += 1
        else:
            current_count = 1
        if current_count == target_count:
            return current_item
        return helper(current_items[1:],current_count,current_item)
    return helper(items)