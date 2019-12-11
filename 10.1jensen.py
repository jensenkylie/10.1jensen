def nested_sum(list):
    total = 0
    for element in list:
        total += sum(element)
    return total

list = [[1, 2], [3], [4, 5, 6]]
print nested_sum(list)
