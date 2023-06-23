x = bool([])
y = all([])
z = any([])

print(x==z and y)

#Output : True
#bool() of Empty list returns Fale.
#all() returns True if all elements in the given iterable are True, if not it returns False. all([]) returns True
#any() checks if any function of given iterable is True and if not then returns False. Since there are no Elements, it returns False
#(False == False) returns True. True and True returns True.