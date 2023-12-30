import time

def count_down(thoi_gian):
    while thoi_gian >= 0:
        print(thoi_gian)
        time.sleep(1)
        thoi_gian -= 1
    print("Strart!!!")
thoi_gian = int(input("Input number: "))

count_down(thoi_gian)