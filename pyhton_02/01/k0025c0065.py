data = [-10, 1, -200, 4, 0]
result = sorted(data)
print(result, data)
result = data.sort()
print(result, data)

num = 10
print(num.bit_length())
num = 128
print(num.bit_length())

test = "tazahogetaz"
print(test.replace("t","").replace("a",""))
tpl = "3人は{}さん"
names = ["松田","浅木"]
names.append("工藤")
message = tpl.format(names[2])
print(message)

def add(x,y):
    return x + y

print(type(add))
newadd = add
print(type(newadd))
print(newadd(4,5))

int_value1 = 1
int_value2 = int()
int_value3 =int(9)
int_value4 =int(9.1)
print(int_value4)
list_valu1 = []
list_valu2 = list()
print(list_valu2)
data = ("マツダ","浅木")
print(type(data))
list_valu3 = list(data)
print(list_valu3)

class Hero:
    #初期化メソッド(コンストラクタ)
    def __init__(self):
        self.name = "勇者ヨシヒコ"
        self.hp = 100

    def heal(self):
        self.hp += 10
    
    def is_allove(self):
        return self.hp > 0
    
    def print(self):
        print(f"{self.name} : {self.hp}")
yoshihiko = Hero() #ヒーロークラスのオブジェクト生成
yoshihiko.print()
yoshihiko.heal()
yoshihiko.print() 









roto = Hero()
roto.print()
roto.set_name("ヨシヒコ")
roto.heal()
roto.print()
print(roto)

""""""
属性
- 名前
- 種族
- 年齢
- 色
-場所
-飼い主
-機能
走る()
吠える()
食べる()
寝る()
遊ぶ()
""""""""



