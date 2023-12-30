n = int(input("nhập n: "))
x = float(input("nhập x: "))

result = (x*x + x + 1 )**n + (x*x - x + 1)**n 
print("A = (x*x + x + 1 )^n + (x*x - x + 1)^n =", result)