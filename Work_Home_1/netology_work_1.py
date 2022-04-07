def dir_cook(file_obj):
    keys = ['ingredient_name', 'quantity', 'measure']
    values = []
    cook_book = {}
    with open(file_obj) as file:
        dish = file.readline()
        count = file.readline()
        for i in range(int(count)):
            values += file.readline().split(' | ')
            dictionary = dict(zip(keys, values))
            cook_book[dish] += [dictionary]
            values = []
    return cook_book


print(dir_cook('file.txt'))
