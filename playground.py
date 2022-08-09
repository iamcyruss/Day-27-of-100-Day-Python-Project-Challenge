def add(*args):
    print(sum(args))

add(3, 5, 7, 9, 22)


def calculate(**kwargs):
    # new_dict = {new_key:new_value for (key,value) in dict.items()}
    new_dict = {key: value for (key, value) in kwargs.items()}
    print(new_dict)

calculate(key='Codename', key2='Alpha')
