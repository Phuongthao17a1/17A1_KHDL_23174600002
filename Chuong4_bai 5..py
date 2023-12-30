def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

least_common_multiple = lcm(num1, num2)

print("Số bội chung nhỏ nhất của", num1, "và", num2, "là:", least_common_multiple)