#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script khởi chạy hệ thống theo dõi mắt
Kiểm tra các thư viện cần thiết và chạy ứng dụng
"""

import sys
import subprocess
import importlib.util

def kiem_tra_thu_vien():
    """Kiểm tra các thư viện cần thiết"""
    thu_vien_can_thiet = [
        'cv2',
        'mediapipe', 
        'pyautogui',
        'numpy',
        'PIL',
        'tkinter'
    ]
    
    thu_vien_thieu = []
    
    for thu_vien in thu_vien_can_thiet:
        if importlib.util.find_spec(thu_vien) is None:
            thu_vien_thieu.append(thu_vien)
    
    return thu_vien_thieu

def cai_dat_thu_vien(thu_vien_thieu):
    """Cài đặt các thư viện thiếu"""
    if not thu_vien_thieu:
        return True
    
    print("Đang cài đặt các thư viện thiếu...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Cài đặt thành công!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Lỗi khi cài đặt thư viện!")
        return False

def main():
    print("🔍 Đang kiểm tra hệ thống...")
    
    # Kiểm tra Python version
    if sys.version_info < (3, 9):
        print("❌ Cần Python 3.9 trở lên!")
        print(f"Phiên bản hiện tại: {sys.version}")
        return
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    
    # Kiểm tra thư viện
    thu_vien_thieu = kiem_tra_thu_vien()
    
    if thu_vien_thieu:
        print(f"❌ Thiếu các thư viện: {', '.join(thu_vien_thieu)}")
        print("🔧 Đang cài đặt...")
        
        if not cai_dat_thu_vien(thu_vien_thieu):
            print("❌ Không thể cài đặt thư viện. Vui lòng chạy:")
            print("pip install -r requirements.txt")
            return
    else:
        print("✅ Tất cả thư viện đã sẵn sàng!")
    
    print("\n🚀 Khởi chạy ứng dụng theo dõi mắt...")
    print("📝 Lưu ý:")
    print("   - Đảm bảo camera hoạt động")
    print("   - Ngồi cách camera 50-70cm")
    print("   - Có đủ ánh sáng")
    print("   - Nhấn Esc để thoát\n")
    
    try:
        subprocess.run([sys.executable, 'login.py'])
    except KeyboardInterrupt:
        print("\n👋 Tạm biệt!")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    main() 