#1.基本异常处理
def bad_divide(a, b):
    return a / b

try:
    result = bad_divide(10, 0)  # ZeroDivisionError!
except ZeroDivisionError:
    print("错误：不能除以0！")
    result = None
#2.捕获具体异常
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"无法将'{value}'转换为整数")
        return None
#3.捕获多个异常
def process_data(data):
    try:
        # 可能出现多种错误
        result = int(data) / len(data)
        return result
    except ValueError:
        print("类型转换错误")
    except ZeroDivisionError:
        print("除零错误")
    except TypeError:
        print("类型错误")

process_data("abc")
process_data(0)

#5.else 子句（没有异常时执行)
def divide_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("除零错误！")
    else:
        # 只有没有异常时才执行
        print(f"计算成功: {a} / {b} = {result}")
        return result
#6. finally 子句（总是执行）
def read_file(filename):
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"文件'{filename}'不存在")
    finally:
        # 无论是否异常，都会执行
        print("清理资源...")
        try:
            file.close()
            print("文件已关闭")
        except:
            print("没有文件需要关闭")

#7. 完整的异常处理结构
def complete_example(value):
    print(f"\n处理值: {value}")
    try:
        print("  尝试转换...")
        number = int(value)
        print("  尝试除法...")
        result = 100 / number
        print(f"  计算成功!")
        return result
    except ValueError:
        print("  错误: 无法转换为整数")
    except ZeroDivisionError:
        print("  错误: 除零")
    except Exception as e:
        print(f"  未知错误: {e}")
    else:
        print("  else: 没有发生异常")
    finally:
        print("  finally: 清理工作")


#9.自定义异常(略)

#10.异常链(略)

#11.上下文管理器(略)

#12.常见异常类型

print("""
ValueError      - 值错误（如int("abc")）
TypeError       - 类型错误（如"string" + 5）
KeyError        - 字典键不存在
IndexError      - 索引超出范围
FileNotFoundError - 文件不存在
ZeroDivisionError - 除零错误
AttributeError  - 属性不存在
ImportError     - 导入模块失败
RuntimeError    - 运行时错误
""")

