def func(k,v,my_dict={}):
    my_dict[k]=v
    return my_dict

dict1 = func('mom',48)
dict2 = func('dad',56)

print(dict1)