"""
    技能系统
        优势:外接一个需求的变化,内部修改一个类.
            增加一个新影响效果,增加一个类.
            某个技能的影响效果改变,无需修改代码.
            [依赖注入:将配置文件中的信息,作为技能释放的效果]
"""


class SkillImpactEffect:
    """
        技能影响效果
    """

    def impact(self):
        pass


class DamageEffect(SkillImpactEffect):
    """
        伤害生命
    """

    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你", self.value, "血量")


class LowerDeffenseEffect(SkillImpactEffect):
    """
        降低防御力
    """

    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("让你", self.time, "秒以内防御力降低", self.value)


class DizzinessEffect(SkillImpactEffect):
    """
        眩晕
    """

    def __init__(self, time):
        self.time = time

    def impact(self):
        print("眩晕", self.time, "秒")


class SkillDeployer:
    """
        技能释放器
    """

    def __init__(self, name=""):
        # 技能名称
        self.name = name
        # 字典类型的配置文件(需求)
        self.__dict_configs = self.__load_config_file()
        # 列表类型的影响效果对象
        self.__list_effect_object = self.__create_effect_object()

    def __load_config_file(self):
        return {
            "少林普攻": ["DamageEffect(50)"],
            "降龙十八掌": ["DamageEffect(200)", "DizzinessEffect(5)", "LowerDeffenseEffect(50,5)"]
        }

    def __create_effect_object(self):
        # self.name  -->  self.__dict_configs --> []
        list_effect_name = self.__dict_configs[self.name]
        list_effect_object = []
        for item in list_effect_name:
            # "DamageEffect(50)" --> DamageEffect(50)
            #  字符串                  python对象
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    def generate_skill(self):
        print(self.name, "释放啦")
        # 将当前技能的所有影响效果执行一遍
        for item in self.__list_effect_object:
            item.impact()


# 测试.............
xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()
xlsbz.generate_skill()

slpg = SkillDeployer("少林普攻")
slpg.generate_skill()
