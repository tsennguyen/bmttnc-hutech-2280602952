def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)  # Chuyển đổi từ nhị phân sang thập phân
    
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False

# Nhập chuỗi số nhị phân và xử lý
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (Phân cách bởi dấu phẩy): ")
so_nhi_phan = chuoi_so_nhi_phan.split(",")  # Tách chuỗi nhị phân thành list

so_chia_het_cho_5 = [so for so in so_nhi_phan if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    print("Có các số chia hết cho 5:", so_chia_het_cho_5)
else:
    print("Không có số nào chia hết cho 5 trong chuỗi đã nhập.")
