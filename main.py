my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)
my_dict['burger'] = my_dict['sandwich']
val = my_dict.pop('sandwich')
print(my_dict['burger'])
