def func(k,v,my_dict={}):
    my_dict[k]=v
    return my_dict

dict1 = func('mom',48)
dict2 = func('dad',56)

print(dict1)

def func(arr1, arr2):
    return any(True if x==y else False for x in arr1 for y in arr2)

print(func([1,2,3],[4,3,2,1]))