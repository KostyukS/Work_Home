def dir_cook(file_obj):
    keys = ['ingredient_name', 'quantity', 'measure']
    cook_book = {}

    def interior_func():
        dish = file.readline().strip()
        count = file.readline()
        values = []
        cook_book[dish] = []
        for i in range(int(count)):
            values += file.readline().strip().split(' | ')
            dictionary = dict(zip(keys, values))
            cook_book[dish] += [dictionary]
            values = []
        if file.readline() == '\n':
            interior_func()

    with open(file_obj) as file:
        interior_func()

    return cook_book


cook_book = dir_cook('file.txt')


def get_shop_list_by_dishes(dishes, person_count):
    dict_ingr = {}
    for item in dishes:
        if item in cook_book:
            for val in cook_book[item]:
                count_ingr = int(val['quantity']) * person_count
                if val['ingredient_name'] in dict_ingr:
                    mean = int(dict_ingr[val['ingredient_name']]['quantity'])
                    dict_ingr[val['ingredient_name']]['quantity'] = str(mean + count_ingr)
                else:
                    dict_ingr[val['ingredient_name']] = {'measure': val['measure'],
                                                         'quantity': str(int(val['quantity']) * person_count)}
    return dict_ingr


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
