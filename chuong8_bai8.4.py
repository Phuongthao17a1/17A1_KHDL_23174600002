import math

a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

p = (a + b + c) / 2

S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Diện tích của tam giác là: {S}")
