def find_identical_pair(t):
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return i, i + 1
    return None

# Get user input for tuple elements
input_str = input("Введите элементы кортежа, разделенные запятыми: ")
input_list = [int(x.strip()) for x in input_str.split(',')]

# Convert the list to a tuple
input_tuple = tuple(input_list)

# Check for identical neighboring elements
result = find_identical_pair(input_tuple)

if result is not None:
    index1, index2 = result
    print(f"Первая идентичная пара находится на позициях {index1} и {index2}.")
else:
    print("Идентичных соседних элементов не найдено.")
