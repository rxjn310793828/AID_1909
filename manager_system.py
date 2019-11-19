"""
    项目计划:
    1. 	数据模型类：StudentModel
		    数据：编号 id,姓名 name,年龄 age,成绩 score
	    逻辑控制类：StudentManagerController
		    数据：学生列表 __stu_list
		    行为：获取列表 stu_list,     只读属性
		         添加学生 add_student   设置学生编号(自增1)
        测试用例:
            创建逻辑控制对象,添加两个学生
            遍历学生列表

    2.     删除学生remove_student    返回是否删除成功
    3.     修改学生 update_student
    4.     输入学生__input_students
           输出学生__output_students
"""

class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0.0):
        self.id = 0
        self.name = name
        self.age = age
        self.score = score

class StudentManagerController:
    """
        学生管理控制器:负责程序核心逻辑处理
    """
    # 初始化编号  类变量(大家)
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    # def add_student(self,name,age,score):
    def add_student(self, stu_info):
        # 为数据生成编号
        self.__generate_id(stu_info)
        # 将数据添加到列表
        self.stu_list.append(stu_info)

    def __generate_id(self, stu_info):
        StudentManagerController.__init_id += 1
        stu_info.id = StudentManagerController.__init_id

    def remove_student(self, stu_id):
        """
            删除学生
        :param stu_id: int类型,需要删除的学生编号
        :return: 是否删除成功
        """
        for item in self.stu_list:
            if item.id == stu_id:
                self.stu_list.remove(item)
                return True  # 删除成功
        return False  # 删除失败

    # def update_student(self,id,new_name,new_age,new_score):
    def update_student(self, stu_info):
        """
            修改学生信息
        :param stu_info:学生对象类型 需要修改的学生信息
        :return:是否修改成功
        """
        for item in self.stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.score = stu_info.score
                item.age = stu_info.age
                return True
        return False

    def order_by_score(self):
        """
            根据成绩升序排列
        """
        for r in range(len(self.stu_list) - 1):
            for c in range(r + 1, len(self.stu_list)):
                if self.stu_list[r].score > self.stu_list[c].score:
                    self.stu_list[r], self.stu_list[c] = self.stu_list[c], self.stu_list[r]

class StudentManagerView:
    """
        学生管理器视图:负责界面逻辑
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1. 添加学生")
        print("2. 显示学生")
        print("3. 删除学生")
        print("4. 修改学生")
        print("5. 按照成绩升序排列")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_order_by_score()

    def __input_students(self):
        name = input("请输入学生姓名:")
        score = float(input("请输入学生成绩:"))
        age = int(input("请输入学生年龄:"))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self):
        for item in self.__manager.stu_list:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        stu_id = int(input("输入需要删除的学生编号:"))
        if self.__manager.remove_student(stu_id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入需要修改的学生姓名:")
        stu.age = input("请输入需要修改的学生年龄:")
        stu.score = input("请输入需要修改的学生成绩:")
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_order_by_score(self):
        self.__manager.order_by_score()
        self.__output_students()

view = StudentManagerView()
view.main()

"""
# 测试...........
manager = StudentManagerController()
# 添加学生
new_stu = StudentModel("孙悟空", 28, 92)
new_stu.id = 1001
stu = StudentModel("悟空", 27, 194)
manager.add_student(stu)
manager.add_student(StudentModel("唐僧", 25, 100))
# 删除学生
print(manager.remove_student(1005))
# 修改学生
manager.update_student(new_stu)
# 排序
manager.order_by_score()
for item in manager.stu_list:
    print(item.id, item.name)
"""
