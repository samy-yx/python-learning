##基类
class Birds:
    def __init__(self,name,color,skill_description):
        self.name = name
        self.color = color
        self.skill_description = skill_description

    def fly(self):
        print(f"{self.name} 正在飞行~~~~~")

    def call(self):
        print(f"{self.name} 发出叫声~~~~~")

    def use_skill(self):
        print(f"{self.name} 使用了技能：{self.skill_description}")

##红鸟子类：继承加重写
class RedBirds(Birds):
    def __init__(self):
        super().__init__("红火","红色","撞击前方障碍物，造成大量伤害")

    def fly(self):
        print("红火以稳定速度向前飞行.....")
    def call(self):
        print("红火发出'wei呀'的叫声")

##黄鸟子类
class YellowBirds(Birds):
    def __init__(self):
        super().__init__("小黄","黄色","瞬间加速，穿透薄障碍物")
    def fly(self):
        print("小黄快速向前飞行.....")
    def call(self):
        print("小黄发出'啾啾啾'的叫声")
#蓝鸟子类
class BlueBirds(Birds):
    def __init__(self):
        super().__init__("小蓝","蓝色","分裂成三只小鸟，分散攻击")

    def fly(self):
        print("小蓝优雅的向前飞行.....")
    def call(self):
        print("小蓝发出'叽叽叽'的叫声")

##障碍物类
class Obstacle:
    def __init__(self,name,strength):
        self.name = name
        self.strength = strength

    def be_attacked(self,bird):
        print(f"{bird.name} 冲向了{self.name}")
        bird.use_skill()
        if isinstance(bird,RedBirds):#这个 "对象" 是不是那个 "类"（或它的子类）造出来的实例
            damage = 80
        elif isinstance(bird,YellowBirds):
            damage = 50
        elif isinstance(bird,BlueBirds):
            damage = 30*3
        self.strength -= damage
        if self.strength <= 0:
            print(f"{self.name}被摧毁了")
        else:
            print(f"{self.name}还剩余{self.strength}点强度")




# test_birds = Birds("小白","白色","测试技能")
# test_birds.fly()
# test_birds.call()
# test_birds.use_skill()
# y_birds = YellowBirds()
# y_birds.fly()
# y_birds.call()
# y_birds.use_skill()
# obstacle1 = Obstacle("木头堡垒",100)
# obstacle1.be_attacked(RedBirds())
if __name__ == "__main__":
    #创建三只小鸟
    red_bird = RedBirds()
    yellow_bird = YellowBirds()
    blue_bird = BlueBirds()

    #创建两个障碍物
    obstacle1 = Obstacle("木头堡垒",100)
    obstacle2 = Obstacle("石头塔楼",200)

    #开始攻击
    obstacle1.be_attacked(red_bird)
    obstacle2.be_attacked(yellow_bird)
    obstacle1.be_attacked(blue_bird)
