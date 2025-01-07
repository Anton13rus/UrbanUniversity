def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25, c = [1,2,3])

values_list = [34, 'Ветер', True]
print_params(*values_list)

values_dict = {'a':False, 'b': 7, 'c':'Maps'}
print_params(**values_dict)

values_list_2 = [0.15, 'Books' ]
print_params(*values_list_2, 42)
