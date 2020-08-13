import inspect
from types import FunctionType

from test.assets.typen_testables.classes import Point

print(Point.__name__, 'is class:', inspect.isclass(Point))
print()


def class_member_type(member):
    if isinstance(member, staticmethod): return 'staticmethod'
    if isinstance(member, property): return 'property'
    if isinstance(member, FunctionType): return 'method'
    return None


for key, ob in Point.__dict__.items():
    print(key, ob, type(ob), class_member_type(ob), inspect.isroutine(ob))

print()

for key, ob in inspect.getmembers(Point):  # 获取Page类中的所有成员方法，i返回的是一个元祖,第一个元素是方法名，第二个是内存地址
    print(key, ob, type(ob), class_member_type(ob), inspect.isroutine(ob))
    if inspect.isfunction(ob):  # 判断成员是不是一个函数方法
        print('>', key, type(ob), ob.__doc__)  # 是打印他的doc

# """下面可以写出带序号的方法"""
# driver = []
# print(Page.context_click.__doc__)
# for i in inspect.getmembers(Page):
#     if inspect.isfunction(i[1]):
#         driver.append(i[1].__doc__)
# for i in enumerate(driver):
#     print(i)
