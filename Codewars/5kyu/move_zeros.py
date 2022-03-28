def move_zeros(array: list) -> list:
    result = []
    nulls = []
    for i in array:
        if i != 0:
            result.append(i)
        else:
            nulls.append(i)
    result.extend(nulls)
    return result
