def tao_tuple_tu_list(lst):
    return lst[::-1]

input_list = input("Nhập vào một list các số nguyên: ").split()
numbers = list(map(int, input_list))
tuple_tu_list = tao_tuple_tu_list(numbers)
print("list: ", numbers)
print("tuple tu list: ", tuple_tu_list)
