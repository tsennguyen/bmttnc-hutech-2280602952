def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập vào một list các số nguyên: ").split()
numbers = list(map(int, input_list))
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong list là: ", tong_chan)