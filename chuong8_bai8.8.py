def tien_phong(loai_phong, so_dem):
    gia_phong = {
        1: 1260000,   # Standard
        2: 1550000,   # Superior Garden View
        3: 1830000,   # Superior Ocean View
        4: 1830000,   # Garden View Bungalow
        5: 2120000,   # Pool View Bungalow
        6: 2120000,   # Family Room
        7: 2540000,   # Beach Front Bungalow
        8: 4800000    # VIP Sea View
    }

    if so_dem >= 4:
        phan_tram_giam = 0.3
    else:
        phan_tram_giam = 0.25

    gia_phong_giam = gia_phong[loai_phong] - gia_phong[loai_phong] * phan_tram_giam
    thanh_tien = gia_phong_giam * so_dem

    return thanh_tien

loai_phong = int(input("Nhập loại phòng (từ 1-8): "))
so_dem = int(input("Nhập số đêm: "))
thanh_tien = tien_phong(loai_phong, so_dem)
print("Thành tiền =", thanh_tien, "VNĐ")