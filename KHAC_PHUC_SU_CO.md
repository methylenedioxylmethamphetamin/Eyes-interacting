# Hướng Dẫn Khắc Phục Sự Cố

## Các Lỗi Thường Gặp

### 1. Lỗi "ModuleNotFoundError"
**Nguyên nhân:** Thiếu thư viện cần thiết

**Giải pháp:**
```bash
pip install -r requirements.txt
```

Hoặc cài đặt từng thư viện:
```bash
pip install mediapipe opencv-python pyautogui numpy pillow
```

### 2. Camera không hoạt động
**Nguyên nhân:** 
- Camera đang được sử dụng bởi ứng dụng khác
- Không có quyền truy cập camera
- Driver camera lỗi

**Giải pháp:**
- Đóng tất cả ứng dụng sử dụng camera (Zoom, Skype, etc.)
- Kiểm tra quyền truy cập camera trong cài đặt hệ thống
- Khởi động lại máy tính

### 3. Hệ thống không phản hồi chính xác
**Nguyên nhân:**
- Ánh sáng không đủ
- Ngồi quá xa/gần camera
- Kính mắt phản quang

**Giải pháp:**
- Đảm bảo có ánh sáng đủ, tránh ánh sáng chói
- Ngồi cách camera 50-70cm
- Tháo kính hoặc điều chỉnh góc để tránh phản quang
- Hiệu chỉnh độ nhạy trong code

### 4. Lỗi "Permission denied" trên macOS
**Nguyên nhân:** macOS chặn quyền điều khiển màn hình

**Giải pháp:**
1. Mở System Preferences > Security & Privacy
2. Chọn tab Privacy
3. Chọn Accessibility
4. Thêm Terminal hoặc Python vào danh sách cho phép

### 5. Con trỏ chuột di chuyển không mượt
**Nguyên nhân:** Tham số làm mượt chưa phù hợp

**Giải pháp:**
Chỉnh sửa trong file `preprocess.py`:
```python
# Tăng smoothing_factor để di chuyển mượt hơn (0.1-0.5)
self.smooth_move(target_x, target_y, self.last_x, self.last_y, smoothing_factor=0.3)
```

### 6. Nháy mắt không được nhận diện
**Nguyên nhân:** Ngưỡng phát hiện nháy mắt không phù hợp

**Giải pháp:**
Chỉnh sửa trong file `preprocess.py`:
```python
# Tăng ngưỡng nếu mắt to, giảm nếu mắt nhỏ
left_eye_closed = (landmarks[145].y - landmarks[159].y) < (0.03 * face_height)  # Tăng từ 0.02
```

## Tối Ưu Hóa Hiệu Suất

### 1. Giảm độ trễ
- Đóng các ứng dụng không cần thiết
- Sử dụng camera có độ phân giải thấp hơn nếu cần

### 2. Tăng độ chính xác
- Hiệu chỉnh tham số theo từng người dùng
- Thực hiện calibration trước khi sử dụng

### 3. Cải thiện trải nghiệm
- Thêm âm thanh phản hồi
- Hiển thị trạng thái hệ thống rõ ràng

## Liên Hệ Hỗ Trợ

Nếu vẫn gặp vấn đề, vui lòng:
1. Kiểm tra log lỗi trong terminal
2. Chụp ảnh màn hình lỗi
3. Mô tả chi tiết các bước đã thực hiện

## Cập Nhật Hệ Thống

Để cập nhật lên phiên bản mới:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
``` 