def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


nested_list = [1, [2, 2, [3, 4, 5]], 6]
flattened_list = flatten(nested_list)
print("Recursive Flatten", flattened_list)
