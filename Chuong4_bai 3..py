m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (lớn hơn m): "))

print("Các số chia hết cho", m, "trong khoảng từ 1 đến", n, "là:")

for i in range(1, n + 1):
    if i % m == 0:
        print(i)