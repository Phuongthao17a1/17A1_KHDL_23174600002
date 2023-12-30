n = int(input("Nhập số nguyên n: "))
dem = 0

if n < 2:
    print("n không là số nguyên tố")
else:
    for i in range(2, n - 1):
        if n % i == 0:
            dem = dem + 1

    if dem == 0:
        print("n là số nguyên tố")
    else:
        print("n không là số nguyên tố")
