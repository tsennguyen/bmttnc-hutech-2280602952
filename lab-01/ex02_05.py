so_gio_lam = float(input("Nhập số giờ làm việc moi tuan: "))
luong_gio = float(input("Nhập số tiền mà bạn nhận được mỗi giờ làm tiêu chuẩnchuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
luong = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print("Lương của bạn là: ", luong)