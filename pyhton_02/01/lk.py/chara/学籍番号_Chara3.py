#Chara.pyモジュールからCharaクラスをimport
from chara import Chara

#キャラクラスのリストオブジェクトcを宣言し、生成
c = []
#c[0]を「名前：リュウ、HP：80」
c.append(Chara("リュウ", 80))
#c[1]を「名前：ベガ、HP：100」
c.append(Chara("ベガ", 100))
#とりあえず「リュウ」が「ベガ」に攻撃
print("先制")
c[0].attack(c[1])
print()

#「リュウ」と「ベガ」のどちらかが死ぬまで戦う
turn = 1
while c[0].isAlive() and c[1].isAlive():
    print(f"ターン {turn}")
    
    # リュウの攻撃
    if c[0].isAlive():
        c[0].attack(c[1])
    
    # ベガの攻撃（ベガが生きている場合のみ）
    if c[1].isAlive():
        c[1].attack(c[0])
    
    print()
    turn += 1

# 勝敗を表示する
print("終了")

print("最終状態:")

c[0].print()
c[1].print()
print()

#勝敗を表示する（両方が死んでいたら引き分けとする）
if not c[0].isAlive() and not c[1].isAlive():
    print("引き分け")
elif c[0].isAlive():
    print(f"結果: {c[0].getName()}の勝利！")
else:
    print(f"結果: {c[1].getName()}の勝利！")








