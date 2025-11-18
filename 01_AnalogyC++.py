#Python - 动态类型 vs C++ - 静态类型
from cgi import print_form


x = 10;       #自动推导为int
name = "Tom"  #自动推导为str
pi = 3.14     #自动推导为float
x = "hello"   #重新赋值为其他类型
print(name)   #输出Tom
print(pi)     #输出3.14
print(x)      #输出hello

#Python - 缩进代码块
y = 10;
if y >0:
    print("y is positive")
    print("y is positive")
    if y > 5:
        print("y is greater than 5")
else:
    print("y is negative")

#Python - 循环
for i in range(10):
    print(i)

#Python - if语句
age = 20;
if age >=18:
    print("You are an adult")
else:
    print("You are a minor")

#Python - 注释
#这是一个注释

#Python - 列表
numbers = [1, 2, 3, 4, 5]
my_list = [1,"hello",True,3.14]

empty_list = [] #空列表
mixed_list = [1,"hello",True,3.14] #混合列表
fruits = ["apple","banana","cherry"] 
print(fruits[0]) 
print(fruits[1]) 
print(fruits[2]) 

fruits[0] = "pineapple" #修改列表
print(fruits) 

fruits.append("orange") #在末尾添加
print(fruits) 

fruits.insert(1, "orange") #在指定位置插入
print(fruits) 

fruits.extend(["mango", "grape"]) #添加多个元素
print(fruits) 

fruits.remove("banana") #删除指定值
print(fruits) #输出['pineapple', 'cherry', 'orange']
print(f"{fruits[1:3]}") #输出['pineapple', 'cherry', 'orange']

fruits.pop() #删除末尾元素
print(fruits) 

fruits.pop(1) #删除指定位置元素
print(fruits) 

fruits.clear() #清空列表
print(fruits) 

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原列表: {nums}")
print(f"长度: {len(nums)}")         
print(f"最大值: {max(nums)}")
print(f"最小值: {min(nums)}")
print(f"求和: {sum(nums)}")

nums.sort()  # 原地排序（修改原列表）
print(f"排序后: {nums}")

nums2 = [5, 2, 8, 1]
nums2_sorted = sorted(nums2)
print(f"原列表: {nums2}, sorted后: {nums2_sorted}")

nums.reverse() #反转
print(f"反转后: {nums}")

nums = [1, 2, 3, 1, 1, 4, 1]  #计数
print(f"1出现次数: {nums.count(1)}")

print(f"3的索引: {nums.index(3)}") # 查找索引

squares = [x**2 for x in range(10)] #列表推导式
print(f"0-9的平方: {squares}")

evens = [x for x in range(20) if x % 2 == 0] #带条件的列表推导式
print(f"0-19的偶数: {evens}")

# python - 字典dict (相当于c++的map)

#空字典
empty_dict = {}
#初始化字典
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False
}

print(person["name"])
print(person["age"])
print(person["city"])
print(person["is_student"])

# 安全访问（如果键不存在，返回默认值）
print(person.get("email", "default@example.com"))
print(person.get("name"))

#添加元素
person["email"] = "john@example.com"

#修改元素
person["age"] = 31

#批量更新
person.update({"city": "Los Angeles", "is_student": True})

#删除元素
person.pop("city")
print(f"删除city后: {person}")

#删除指定键
del person["age"]
print(f"删除age后: {person}")

#清空字典
person.clear()
print(f"清空后: {person}")

#in操作符
if "name" in person:
    print("name is in person")
else:
    print("name is not in person")

if "phone" not in person:
    print("phone is not in person")
else:
    print("phone is in person")

#遍历键
person.update({"city": "Los Angeles", "is_student": True})
person["name"] = "John"
print(f"{person}")

for key in person.keys():
    print(f"key: {key}")

#遍历值
for name in person.values():
    print(f"value: {name}")

#遍历键值对
for key, value in person.items():
    print(f"key: {key}, value: {value}")

print(f"所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")
print(f"所有键值对: {list(person.items())}")
print(f"字典长度: {len(person)}")

#字典推导式
squares = {x: x**2 for x in range(10)}
print(f"0-9的平方: {squares}")

#筛选字典
scores = {
    "Alice": 95,
    "Bob": 85,
    "Charlie": 90,
    "David": 88
}
passed = {name: score for name, score in scores.items() if score >= 90}
print(f"及格学生: {passed}")

#字典合并
merged = {**person, **scores}
print(f"合并后的字典: {merged}")

#集合 - 三大特性

#特性1: 自动去重
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(f"去重后的集合: {my_set}")

#特性2: 无序
my_set = {1, 2, 3, 4, 5}
# my_set[0]  # 错误！集合不支持索引

#特性3: 不可变 - 元素类型必须是不可变的
my_set = {1, 2, 3, 4, 5}
# wrong_set = {[1, 2], [3, 4]}  # 错误！列表不能放入集合
correct_set = {(1, 2), (3, 4)}  # 正确！元组可以
print(f"正确的集合: {correct_set}")

#集合 - 创建集合
#方式1: 使用花括号
my_set = {1, 2, 3, 4, 5}
print(f"集合: {my_set}")

#方式2: 使用set()函数
my_set = set([1, 2, 3, 4, 5])
print(f"集合: {my_set}")

#方式3: 使用集合推导式
my_set = {x for x in range(10) if x % 2 == 0}
print(f"集合: {my_set}")

#空集合
empty_set = set()
print(f"空集合: {empty_set}")

#添加元素
my_set = {1,2,3}
print(f"添加前: {my_set}")
#方式1: 使用add()方法
my_set.add(4)
print(f"添加后: {my_set}")
#方式2: 使用update()方法 -- 添加多个元素
my_set.update([4,5,6])
print(f"添加后: {my_set}")

#删除元素
my_set = {1,2,3,4,5}
print(f"删除前: {my_set}")
#方式1: 使用remove()方法 -- 删除指定元素
my_set.remove(4)
print(f"删除后: {my_set}")
#方式2: 使用discard()方法 -- 删除指定元素（如果元素不存在，不会报错）(更安全)
my_set.discard(4)
print(f"删除后: {my_set}")
#方式3: 使用pop()方法 -- 删除并返回第一个元素
my_set.pop()
print(f"删除后: {my_set}")
#清空集合
my_set.clear()
print(f"清空后: {my_set}")

#集合 - 集合操作
#并集
set1 = {1,2,3}
set2 = {3,4,5}
print(f"并集: {set1 | set2}")
#交集
print(f"交集: {set1 & set2}")
#差集
print(f"差集: {set1 - set2}")
#子集
print(f"子集: {set1 < set2}")
#超集
print(f"超集: {set1 > set2}")
#对称差集
print(f"对称差集: {set1 ^ set2}")
#集合长度
print(f"集合长度: {len(set1)}")
#集合是否为空
print(f"集合是否为空: {not set1}")
#集合是否为空
print(f"集合是否为空: {not set1}")

#列表去重
numbers = [1,2,3,4,5,1,2,3,4,5]
unique_numbers = list(set(numbers))
print(f"去重后的列表: {unique_numbers}")

#元组 
#1.元组的核心特性
# (不可变 有序 可以包含不同类型 可重复)
#2.创建元组
#创建元组 - 使用圆括号
my_tuple = (1,2,3,4,5)
#创建元组 - 使用tuple()函数
my_tuple = tuple([1,2,3,4,5])
#创建元组 - 空元组
empty_tuple = ()
#创建元组 - 单个元素
single_tuple = (1,)
#3.访问元组
#切片
print(my_tuple[1:3])
#4.元组的常用操作
#拼接
print(my_tuple + (6,7,8))
#重复
print(my_tuple * 2)
#长度
print(len(my_tuple))
#最大值
print(max(my_tuple))
#最小值
print(min(my_tuple))
#求和
print(sum(my_tuple))
#平均值
print(sum(my_tuple) / len(my_tuple))
#是否为空
print(not my_tuple)
#计数
print(my_tuple.count(1))
#查找索引
print(my_tuple.index(1))
#5.遍历元组
for number in my_tuple:
    print(f"number: {number}")
#6.元组解包 
#基本解包
point = (1,2)
x, y = point
print(f"x: {x}, y: {y}")
#部分解包
a, b, *c = my_tuple
print(f"a: {a}, b: {b}, c: {c}")
#多变量交换
a, b = 1, 2
print(f"a: {a}, b: {b}")
a, b = b, a
print(f"a: {a}, b: {b}")
#7.元组作为字典的键
locations  = {
    (0,0):"原点",
    (1,0):"x轴",
    (0,1):"y轴"
}
print(f"locations: {locations}")
print(f"locations[(0,0)]: {locations[(0,0)]}")