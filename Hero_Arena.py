
import random
#基类
class Hero:
    def __init__(self,name,hp,attack_power,skill_name):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.skill_name = skill_name

    # def take_damage(self):
    #     print(f"{self.name}受到伤害")
    # def is_alive(self):
    #     print(f"{self.name}还剩{self.hp}点血量")
    # def attack(self):
    #     print(f"{self.name}造成{self.attack_power}点普通伤害")
    # def use_skill(self):
    #     print(f"{self.name}释放：{self.skill.name}")

    def take_damage(self,damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0 #血量最低归0，不出现负数
        print(f"{self.name}受到{damage}点伤害，剩余血量{self.hp}")

    def is_alive(self):
        return self.hp > 0

    def attack(self,target):
        print(f"{self.name}对{target.name}发动普通攻击")
        target.take_damage(self.attack_power) #让目标受伤

    def use_skill(self,target):
        print(f"{self.name}使用了技能：{self.skill_name}")
        target.take_damage(self.attack_power * 2) #技能伤害 = 普攻 * 2

# h1 = Hero("测试英雄",100,20,"测试技能")
# h2 = Hero("沙包",100,0,"无")
# h1.attack(h2)
# print("h2还活着吗",h2.is_alive())
# h1.use_skill(h2)
# print("h2还活着吗",h2.is_alive())

#战士
class Warrior(Hero):
    def __init__(self):
        super().__init__("狂铁",350,20,"破釜沉舟")

    def use_skill(self,target):
        print(f"{self.name}使用了技能：{self.skill_name}")
        target.take_damage(60)


#法师
class Mage(Hero):
    def __init__(self):
        super().__init__("炎姬",200,30,"火焰风暴")

    def use_skill(self,target):
        print(f"{self.name}使用了技能：{self.skill_name}")
        target.take_damage( 80)

#刺客
class Assassin(Hero):
    def __init__(self):
        super().__init__("影",260,25,"暗影突袭")

    def use_skill(self,target):
        print(f"{self.name}使用了技能：{self.skill_name}")
        if random.random() < 0.5:#random.random() 的范围：[0.0, 1.0)
            damage = 100
            print("暴击！伤害翻倍")
        else:
            damage = 50
        target.take_damage(damage)

warrior = Warrior()
assassin = Assassin()
mage = Mage()
#
# dummy = Hero("沙包",1000,0,"无")
#
# warrior.use_skill(dummy)
# mage.use_skill(dummy)
# assassin.use_skill(dummy)

#竞技类
class Arena:
    def battle(self,h1,h2):
        print(f"对战开始：{h1.name} VS {h2.name}")
        round_num = 1
        while h1.is_alive() and h2.is_alive():#两个都活着才能继续战斗
            print(f"——————{round_num} 回合——————")
            self.take_turn(h1,h2)
            # h1.attack(h2)#先手攻击
            if not h2.is_alive():
                break # h2倒了，不用反击了
            self.take_turn(h2,h1)
            # h2.attack(h1)# h2反击
            round_num += 1

        if h1.is_alive():
            print(f"{h1.name}获胜！")
        else:
            print(f"{h2.name}获胜！")
    #50％概率发动技能
    def take_turn(self,attacker,defender):
        if random.random() < 0.5:
            attacker.use_skill(defender)
        else:
            attacker.attack(defender)

# arena = Arena()
# arena.battle(Warrior(), Assassin())
if __name__ == "__main__":
    arena = Arena()

    print("===== 第一场：狂铁 VS 影 =====")
    arena.battle(Warrior(),Assassin())
    print()
    print("===== 第二场：炎姬 VS 狂铁 =====")
    arena.battle(Mage(), Warrior())
