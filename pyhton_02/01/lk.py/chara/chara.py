import random

class Chara:

    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp
    
    def print(self):
        print(f"{self.__name}({self.__hp})")
    
    def hello(self):
        print("こんにちは")
    
    def getName(self):
        return self.__name
    
    def setName(self, aName):
        self.__name = aName
    
    def getHp(self):
        return self.__hp
    
    def setHp(self, aHp):
        self.__hp = max(0, aHp)

    
    def play(self):
        self.setHp(self.getHp() - 10)
        print(f"遊んだ HP:{self.getHp()}")
    
    def damege(self) -> float:
        """10〜20の範囲でランダムなダメージ値を返す"""
        return random.randint(10, 20)
    
    def attack(self, c: "Chara") -> None:
        """相手キャラクターを攻撃してダメージを与える"""
        damage = self.damege()
        new_hp = c.getHp() - damage
        c.setHp(new_hp)
        print(f"{self.getName()}の攻撃！ {c.getName()}に{damage:.1f}のダメージ！")
        print(f"{c.getName()}の残りHP: {c.getHp():.1f}")
    
    def isAlive(self) -> bool:
        """生きているかどうかを判定"""
        return self.getHp() > 0
