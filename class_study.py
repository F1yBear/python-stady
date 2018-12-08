#!/usr/bin/python3


class FlyBear:
    lea = "voe"

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def to_string(self):
        return "姓名：" + self.name + ",年龄：" + str(self.age)


f = FlyBear("王飞雄", 26)


print(f.to_string(), FlyBear.lea)
