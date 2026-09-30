class Entity:
    """本体：所有角色的祖宗：负责名字和坐标"""
    def __init__(self,name,x = 0,y = 0,**kwargs):
        print(f"[Entity] 初始化 {name},出生在({x},{y})")
        super().__init__(**kwargs)
        self.name = name
        self.x = x
        self.y = y

    def show_position(self):
        print(f"{self.name} 当前位置：({self.x},{self.y})")
class Swimmer:
    """会游泳的能力，只管游泳速度和 swim方法"""
    def __init__(self,swim_speed = 1,**kwargs):
        print(f"[Swimmer] 游泳能力就绪，速度{swim_speed} m/s")
        super().__init__(**kwargs)
        self.swim_speed = swim_speed

    def swim(self,dx):
        self.x += dx
        print(f"{self.name} 游了 {dx} 米，速度是{self.swim_speed} m/s")



class Flyer:
    """会飞的能力，只管飞行速度和fly方法"""
    def __init__(self,fly_speed = 1,**kwargs):
        print(f"[Flyer] 飞行能力就绪，速度{fly_speed} m/s")
        super().__init__(**kwargs)
        self.fly_speed = fly_speed

    def fly(self,dx,dy):
        self.x += dx
        self.y += dy
        print(f"{self.name} 飞了一段时间，速度是{self.fly_speed} m/s")



class Duck(Swimmer,Flyer,Entity):
    """鸭子：会游泳，会飞，是个实体"""
    def __init__(self,name,swim_speed = 2,fly_speed = 5):
        print(f"[Duck] 鸭子{name}出生")
        super().__init__(name = name,swim_speed = swim_speed,fly_speed = fly_speed)

print("=== 查看路线图 ===")
print(Duck.__mro__)
print()

print("=== 创建一只鸭子 ===")
donald = Duck(name = "唐老鸭",swim_speed = 2,fly_speed = 6)
print()

print("=== 让鸭子动起来 ===")
donald.swim(10)
donald.fly(5,8)
donald.show_position()



