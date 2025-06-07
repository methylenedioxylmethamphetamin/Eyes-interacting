import numpy as np

# Tọa độ mong muốn (điểm mục tiêu)
desired_coords = [
    (960, 540),
    (500, 400),
    (300, 300),
    (1200, 700),
    (470, 439),
    (492, 427),
    (545, 427),
    (524, 446),
]

# Tọa độ thực tế (điểm được theo dõi)
actual_coords = [
    (955, 540),  
    (505, 405),  
    (295, 303),  
    (1210, 695),  
    (470, 439),  
    (492, 428),  
    (545, 422), 
    (532, 450),  
]

def tinh_do_chinh_xac(toa_do_mong_muon, toa_do_thuc_te, nguong=10):
    """
    Tính độ chính xác của hệ thống theo dõi mắt
    
    Args:
        toa_do_mong_muon: Danh sách tọa độ mục tiêu
        toa_do_thuc_te: Danh sách tọa độ thực tế được theo dõi
        nguong: Ngưỡng sai số cho phép (pixel)
    
    Returns:
        sai_so: Danh sách sai số Euclidean
        do_chinh_xac: Phần trăm độ chính xác
    """
    if len(toa_do_mong_muon) != len(toa_do_thuc_te):
        raise ValueError("Số lượng tọa độ mong muốn và tọa độ thực không khớp!")

    sai_so = []
    diem_chinh_xac = 0

    for mong_muon, thuc_te in zip(toa_do_mong_muon, toa_do_thuc_te):
        sai_so_euclidean = np.sqrt((mong_muon[0] - thuc_te[0]) ** 2 + (mong_muon[1] - thuc_te[1]) ** 2)
        sai_so.append(sai_so_euclidean)

        if sai_so_euclidean <= nguong:
            diem_chinh_xac += 1

    do_chinh_xac = (diem_chinh_xac / len(toa_do_mong_muon)) * 100

    return sai_so, do_chinh_xac

# Tính toán độ chính xác
nguong_sai_so = 10  # pixel
sai_so, do_chinh_xac = tinh_do_chinh_xac(desired_coords, actual_coords, nguong_sai_so)

print("=== KẾT QUẢ ĐÁNH GIÁ ĐỘ CHÍNH XÁC HỆ THỐNG ===")
print("\nSai số Euclidean từng cặp tọa độ:")
for i, sai_so_diem in enumerate(sai_so):
    print(f"Điểm {i+1}: {sai_so_diem:.2f} pixel")

print(f"\nĐộ chính xác với ngưỡng {nguong_sai_so} pixel: {do_chinh_xac:.2f}%")
print(f"Sai số trung bình: {np.mean(sai_so):.2f} pixel")
print(f"Sai số lớn nhất: {np.max(sai_so):.2f} pixel")
print(f"Sai số nhỏ nhất: {np.min(sai_so):.2f} pixel")