so_tien_gui = float(input("Số tiền gửi là : "))
so_thang = float(input("Số tháng : "))
lai_suat_nam = float(input("Lãi suất năm : "))
tien_lai = ((so_tien_gui*so_thang)*(lai_suat_nam/1210))

print("Số tiền lãi là : ", tien_lai)

tong_so_tien = so_tien_gui + tien_lai

print("Tổng số tiền sau ", so_thang, " là : ", tong_so_tien)