from dataclasses import dataclass


class MagicList(object):
    def __init__(self, cls_type=None):
        self.cls_type = cls_type
        if cls_type:
            self.cls_instance = self.cls_type()
        self.custom_values = [self.cls_instance] if cls_type else [None]

    def __setitem__(self, index, value):
        if index < len(self.custom_values) - 1 or index > len(self.custom_values):
            self.custom_values[index] = value
        else:
            self.custom_values[index] = value
            self.custom_values.append(self.__init_subclass__self.cls_type)

    def __getitem__(self, index):
        return self.custom_values[index]


@dataclass
class Person:
    age: int = 1
    weight: int = 5


# a = MagicList(cls_type=Person)
# a[0].age = 5
# print(a)
# # a = MagicList()
# # a[0] = 5
# # print(a[0])
# # a[1] = 10
# # print(a[0],a[1])
# # a[3] = 10
# # print(a[0],a[1])
