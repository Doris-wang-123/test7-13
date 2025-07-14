from functools import reduce

# 基础 lambda 函数演示
print("=== 基础 Lambda 函数 ===")
print("无参数:", (lambda: "Hello world!")())
print("单参数:", (lambda a: a + 5)(5))
print("双参数:", (lambda a, b: a * b)(5, 6))
print("三参数:", (lambda a, b, c: a + b + c)(1, 2, 3))

# 高阶函数应用
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print("\n=== Lambda 与高阶函数 ===")
print(f"原始数据: {numbers}")
print(f"平方: {list(map(lambda x: x**2, numbers))}")
print(f"偶数: {list(filter(lambda x: x % 2 == 0, numbers))}")
print(f"乘积: {reduce(lambda x, y: x * y, numbers)}")
