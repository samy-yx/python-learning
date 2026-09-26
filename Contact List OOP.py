import json

class Contact:

    def __init__(self,name,phone,age):
        self.name = name
        self.phone = phone
        self.age = age


    def to_dict(self):
        """把自己变成字典，方便存进json """
        return {
            "姓名":self.name,
            "电话":self.phone,
            "年龄":self.age
        }
    @classmethod
    def from_dict(cls,data):
        """从字典造一个联系人对象，读json文件的时候用"""
        return cls(data["姓名"],data["电话"],data["年龄"])

    def update_info(self,phone,age):
        """修改自己的电话和年龄"""
        self.phone = phone
        self.age = age

    def __str__(self):
        """打印该联系人时显示的样子"""
        return f"姓名：{self.name}\n 电话：{self.phone}\n 年龄：{self.age}\n"


class ContactBook:
    """通讯录：存放联系人，还负责读写文件和显示菜单"""
    def __init__(self,file_path = "contacts.json"):
        self.file_path = file_path #数据文件名
        self.contacts = [] #里面装的是Contact联系人对象
        self.load()  #一造出来就读取文件

    def load(self):
        """从json文件读取联系人：文件不存在就新建一个新的"""
        try:
            with open(self.file_path,"r",encoding = "utf-8") as f:
                data_list = json.load(f) #data_list里面装的是字典，不是COntact对象
            #把从json里读到的每个字典都变成一个Contact对象
            self.contacts = [Contact.from_dict(d) for d in data_list]
        except FileNotFoundError:
            self.contacts = [] #文件不存在，顺便建一个空的
            self.save()

    def save(self):
        """把所有联系人存进 json文件里面"""
        data_list = [c.to_dict() for c in self.contacts]
        with open(self.file_path,"w",encoding = "utf-8") as f:
            json.dump(data_list,f,ensure_ascii = False)

    def add(self,contact):
        """添加联系人对象"""
        self.contacts.append(contact)

    def find_by_name(self,name):
        """按姓名找：找到返回对象，找不到返回None"""
        for c in self.contacts:
            if c.name == name:
                return c
        #找不到返回None
        return None

    def delete(self,name):
        """按姓名删除"""
        contact = self.find_by_name(name)
        if contact:
            self.contacts.remove(contact)
            print("删除成功！")
        else:
            print("查无此人！")

    def show_all(self):
        """显示所欲联系人"""
        if not self.contacts:
            print("还没有存入联系人")
            return

        print("===== 联系人列表 =====")
        for c in self.contacts:
            print(c)
            print()

    def menu(self):
        """打印菜单"""
        print("=" * 30)
        print("     通讯录管理系统     ")
        print(" =" * 30)
        print("1. 添加联系人")
        print("2. 删除联系人")
        print("3. 修改联系人")
        print("4. 查询联系人")
        print("5. 显示联系人")
        print("0. 退出系统")
        print("=" * 30)


    def run(self):
        """主循环"""
        while True:
            self.menu()
            try:
                choice = int(input("请选择："))
            except ValueError:
                print("请输入数字！")
                continue

            if choice == 1:
                name = input("请输入姓名：")
                phone = input("请输入电话：")
                age = int(input("请输入年龄："))
                self.add(Contact(name,phone,age))
            elif choice == 2:
                name = input("请输入要删除的姓名：")
                self.delete(name)
            elif choice == 3:
                name = input("请输入要修改的姓名：")
                contact = self.find_by_name(name)

                if contact:
                    new_phone = input("请输入新的电话：")
                    new_age = input("请输入新的年龄")
                    contact.update_info(new_phone,new_age)
                    print("修改成功")
                else:
                    print("查无此人")
            elif choice == 4:
                name = input("请输入要查询的姓名：")
                contact = self.find_by_name(name)
                if contact:
                    print(contact)
                else:
                    print("查无此人")

            elif choice == 5:
                self.show_all()

            elif choice == 0:
                #运行过程中主要操作内存，退出时持久化到文件
                self.save() # 退出时保存
                print("0.退出系统")
                break

            else:
                print("输入错误，请重新输入")

book = ContactBook()
book.run()



