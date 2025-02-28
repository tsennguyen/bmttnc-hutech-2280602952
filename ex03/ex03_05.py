def dem_so_lan_xuat_hien(lst):
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

input_string = input("Nhập vào một list các số nguyên: ")
word_list = input_string.split()

result = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử trong list là: ", result)