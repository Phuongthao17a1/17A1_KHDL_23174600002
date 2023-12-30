def tinh_cuoc_taxi(loai_xe, so_km, thoi_gian_cho):
    if loai_xe == 4:
        gia_mo_cua = 11000
        gia_pham_vi_20km = 12100
        gia_tu_km_21 = 10000
    elif loai_xe == 7:
        gia_mo_cua = 13000
        gia_pham_vi_20km = 14100
        gia_tu_km_21 = 12000
    else:
        print("Loại xe không hợp lệ.")
        return

    if so_km <= 0.8:
        cuoc_khoi_hanh = gia_mo_cua
    elif so_km <= 20:
        cuoc_khoi_hanh = gia_mo_cua + (so_km - 0.8 ) * gia_pham_vi_20km
    else:
        cuoc_khoi_hanh = gia_mo_cua + 19.2 * gia_pham_vi_20km + (so_km - 20) * gia_tu_km_21

    phi_cho = max(0, thoi_gian_cho - 5) * 800 
    cuoc_total = cuoc_khoi_hanh + phi_cho

    print(f"Loại xe: {loai_xe} chỗ")
    print(f"Số km: {so_km} km")
    print(f"Thời gian chờ: {thoi_gian_cho} phút")
    print(f"Cước taxi: {cuoc_total} đồng")


loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))
so_km = float(input("Nhập số km: "))
thoi_gian_cho = int(input("Nhập thời gian chờ (phút): "))

tinh_cuoc_taxi(loai_xe, so_km, thoi_gian_cho)