list_files = ['1.txt', '2.txt', '3.txt']


def sort_file(list_obj):
    list_count_str = []
    for item in list_obj:
        with open(item) as file:
            count = len(file.readlines())
            list_count_str.append(count)
            dict_count = dict(zip(list_files, list_count_str))
            sorted_dict = {}
            sorted_keys = sorted(dict_count, key=dict_count.get)
            for i in sorted_keys:
                sorted_dict[i] = dict_count[i]
    open('Result_file.txt', 'w').close()
    for item in sorted_dict:
        with open(item) as file1:
            name = item
            cnt = sorted_dict[item]
            content = file1.read()
        with open('Result_file.txt', 'a') as file2:
            file2.write(name + '\n')
            file2.write(str(cnt) + '\n')
            file2.write(content + '\n' * 2)


sort_file(list_files)

with open('Result_file.txt') as file:
    print(file.read())
