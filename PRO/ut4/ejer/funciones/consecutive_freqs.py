# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items, /, as_string=False):
    freqs = []
    if len(items) > 0:
        amount = 1
        previous = items[0]
        for item in items[1:]:
            if item == previous:
                amount += 1
            else:
                freqs.append((previous, amount))
                previous = item
                amount = 1
        freqs.append((previous, amount))
    if as_string:
        freqs = ",".join([f"{element}:{value}" for element, value in freqs])
    return freqs


# freqs = []
# _count = 1
# for item_ind in range(1, len(items)):
#     actual_element = items[item_ind]
#     previous_element = items[item_ind - 1]
#     if actual_element != previous_element:
#         freqs.append((previous_element, _count))
#         _count = 1
#     else:
#         _count += 1
#     if len(items) - 1 == item_ind:
#         freqs.append((actual_element, _count))
# if as_string:
#    freqs = ",".join([f"{element}:{value}" for element, value in freqs])
