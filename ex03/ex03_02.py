def dao_nguoc_list(lst):
    return lst[::-1]    

input_list = input("Nhập vào một list các số nguyên: ").split()
numbers = list(map(int, input_list))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược là: ", list_dao_nguoc)

