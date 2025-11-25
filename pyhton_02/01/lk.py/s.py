def  add_suffix( names ):
    for i in range (len(names)):
        names [i] = names [i] + "さん"
    return names

before_names = ["マツダ","朝霧","工藤"]


copied_names = list()
for n in before_names:
    copied_names.append(n)
after_names  = add_suffix(copied_names)

print("さんを付けたあと:"+ after_names[0])
print("さんを付け前:"+ before_names[0])

def add_suffix(name):
    name = name + "さん"
    return name
before_name = add_suffix(before_names)
print("さんを付けたあと:"+ after_names)
print("さんを付け前:"+ before_name)


