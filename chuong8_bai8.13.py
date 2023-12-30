n = int(input("Nhập một số nguyên: "))

A = 0  # Tổng số lẻ
phep_tinh_A = ""

for i in range(1, n + 1):
    if i % 2 != 0:
        A += i
        phep_tinh_A += str(i)
        if i < n:
            phep_tinh_A += " + "

print("A =", phep_tinh_A, "=", A)

B = 0  # Tổng số chẵn
phep_tinh_B = ""

for i in range(1, n + 1):
    if i % 2 == 0:
        B += i
        phep_tinh_B += str(i)
        if i < n:
            phep_tinh_B += " + "

print("B =", phep_tinh_B, "=", B)

C = 1  # Tích từ 1 đến n
phep_tinh_C = ""

for i in range(1, n + 1):
    C *= i
    phep_tinh_C += str(i)
    if i < n:
        phep_tinh_C += " * "

print("C =", phep_tinh_C, "=", C)

D = 1  # Biến tích các số chia hết cho 3 nhỏ hơn hay bằng n
phep_tinh_D = ""

for i in range(1, n + 1):
    if i % 3 == 0:
        D *= i
        phep_tinh_D += str(i)
        if i < n:
            phep_tinh_D += " * "

print("D =", phep_tinh_D, "=", D)

E = 0  # Biến tổng các số nguyên tố nhỏ hơn hay bằng n
phep_tinh_E = ""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, n+1):
    if is_prime(i):
        E += i
        phep_tinh_E += str(i)
        if i < n - 1:
            phep_tinh_E += " + "

print("E =", phep_tinh_E, "=", E)

F = 0  # Biến tổng chuỗi đan dấu
phep_tinh_F = ""

for i in range(1, n + 1):
    if i % 2 == 0:
        F -= i
        phep_tinh_F += "-" + str(i)
    else:
        F += i
        phep_tinh_F += "+" + str(i)

print("F =", phep_tinh_F, "=", F)

