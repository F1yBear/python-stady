# 加法
def add(a, b):
    return a + b


# 加法
def subtract(a, b):
    return a - b


# 乘法
def multiply(a, b):
    return a * b  #


# 除法
def divide(a, b):
    return a / b


# 用户输入
print("选择运算：\n{0}\n{1}\n{2}\n{3}".format("1.加法", "2.减法", "3.乘法", "4.除法"))

choice = input("选择运算（1/2/3/4）:")

num1 = int(input("请输入数字："))
num2 = int(input("请输入数字："))
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("输入错误")
