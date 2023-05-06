print ("Hello World");

def my_dict():
    d = {"name":"Bob","age":30}
    return len(set(d))

print (my_dict())


languages =["Java","C++","Python","Javascript","Julia","Rust"]
for lang in languages[:]:
    languages.remove(lang)

print(languages)