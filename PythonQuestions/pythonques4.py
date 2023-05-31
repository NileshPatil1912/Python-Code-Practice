def zip_function(list1, list2):
    zipped = zip(list1, list2)
    result = [(a,b) for a, b in zipped if a != b]
    return *result,

list1 = [1,2,3,4,5]
list2 = [1,3,3,4,6]

output = zip_function(list1, list2)

print(output)


'''
Output = ((2,3),(5,6))
zip_functionzips two lists together using zip() function - (1,1),(2,3),(3,3),(4,4),(5,6)
The list comprehension iterates through the zipped pairs and include only those pairs where the elements are not equal
return *result statement uses the unpacking operator (*) to unpack the elements of the result list and create a tuple with
those elements
'''