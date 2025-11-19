#1.基本函数定义
#基础语法
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)
#多参数函数
def add(a, b):
    return a + b
print(f"3+5 = {add(3, 5)}")
#无返回值函数
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")
print_info("Alice", 25)
#多返回值函数
def get_person_info(name, age):
    return name, age
name, age = get_person_info("Alice", 25)
print(f"Name: {name}, Age: {age}")

#2.类型提示 -- 给程序员增加安全感
# 普通类型提示
def add(a: int, b: int) -> int:
    return a + b
print(add(1, 2))

#3.默认参数
#默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))
print(greet("Alice", "Hi"))
#多个默认参数
def greet(name, greeting="Hello", title="Mr."):
    return f"{title}, {greeting}, {name}!"
print(greet("Alice"))
print(greet("Alice", "Hi"))
print(greet("Alice", "Hi", "Ms."))

#4.关键字参数
def introduce(name, age, city):
    return f"我是{name}，{age}岁，来自{city}"
# 位置参数（和C++一样）
print(introduce("张三", 25, "北京"))

# 关键字参数（指定参数名，顺序可以乱）
print(introduce(age=25, city="北京", name="张三"))  # 顺序不重要！

# 混合使用（位置参数必须在前）
print(introduce("李四", city="上海", age=30))

#5.任意数量参数
def print_numbers(*numbers):
    print(f"Received numbers: {numbers}")
print_numbers(1, 2, 3, 4, 5)
# *args 解包：把列表/元组展开为多个参数
numbers = [5,6,7]
print_numbers(*numbers)  # 等价于 sum_all(1, 2, 3, 4, 5)

#6. 任意数量关键字参数 **kwargs（字典参数）
def print_person_info(**kwargs):
    print(f"Received person info: {kwargs}")
print_person_info(name="张三", age=25, city="北京")
# **kwargs 解包：把字典展开为多个关键字参数
person_info = {"name": "张三", "age": 20, "city": "北平"}
print_person_info(**person_info)

#7.强制关键字参数 --  * 后面的参数必须使用关键字传递
def print_person_info(name, *, age, city):
    print(f"Received person info: {name}, {age}, {city}")
print_person_info("张三", age=20, city="北平")
# 强制关键字参数必须使用关键字参数传递
#print_person_info("张三", 20, "北平")  # 错误！

#8.强制位置参数     / 前面的参数必须使用位置传递 (先略)

#9.Lambda表达式 -- 匿名函数
square = lambda x: x * x
print(square(5))
# 等价于
def square(x):
    return x * x
print(square(5))
# Lambda表达式可以作为参数传递给其他函数
def apply_function(func, x):
    return func(x)
print(apply_function(square, 5))

