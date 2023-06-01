def func_stack():
    stack = ["car","candy","fruit","bike"]
    results = (stack.pop(1) if stack.pop(0) != "candy" else stack.pop())
    return results

print(func_stack())


'''
First stack.pop(1) is executed so "candy" is popped
Then if condition is checked
stack.pop(0) which is equal to "car" is removed
As the condition is filled then again stack.pop(1) i.e removing "bike" is executed
'''