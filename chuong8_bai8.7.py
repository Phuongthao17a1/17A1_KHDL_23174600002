def tiendien(kwh):
    if kwh <= 50:
        cost = kwh * 1678
    elif kwh <= 100:
        cost = 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        cost = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    elif kwh <= 300:
        cost = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
    elif kwh <= 400:
        cost = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
    else:
        cost = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + 100 * 2834 + (kwh - 400) * 2927

    return cost

kwh_sudung = int(input("Nhập dữ liệu: "))
chiphi = tiendien(kwh_sudung)

print("Số tiền điện cần thanh toán cho", kwh_sudung, "kWh là", chiphi, "VND")