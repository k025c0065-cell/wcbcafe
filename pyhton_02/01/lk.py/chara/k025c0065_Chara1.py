#Chara.pyモジュールを読込む
import chara
#キャラ型のオブジェクトcを宣言し、
# 実体を(名前：マリオ, HP:100)として生成
c= chara.chara("マリオ",100)
#cの名前を「ルイージ」に変更する
c.setName("ルイージ")
#ちゃんと名前を変更できたかを確認するため、名前を取得して表示
print(c.getName())

#変数hit_pointにcのHPの値を代入
hit_point = c.getHp()

#変数hit_pointの値を表示
print(hit_point)
#cのHPを100倍にするS
c.setHp(hit_point * 100)
#最後に確認のため、cのパラメータを表示
c.print()
c.play