import os
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import sys
import pyautogui
from preprocess import TrackingFace

user_name = sys.argv[1] if len(sys.argv) > 1 else "Người dùng"

root = tk.Tk()
root.title("Giao Diện Camera - Theo Dõi Mắt")
root.geometry("1000x700")
root.configure(bg='#1E2440')

tracking_active = False
tracking_face = None

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

camera_frame = tk.Label(root, bg="black")
camera_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

side_frame = tk.Frame(root, bg='#1E2440')
side_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

user_icon = tk.Label(side_frame, text="👤", font=("Helvetica", 32), bg='#1E2440', fg='white')
user_icon.pack(pady=10)
user_name_label = tk.Label(side_frame, text=f"Xin chào, {user_name}", font=("Helvetica", 12), bg='#1E2440', fg='white')
user_name_label.pack(pady=10)

# Thêm hướng dẫn sử dụng
instruction_label = tk.Label(side_frame, text="HƯỚNG DẪN:", font=("Helvetica", 10, "bold"), bg='#1E2440', fg='#D4B0FF')
instruction_label.pack(pady=(20, 5))

instructions = [
    "• Nháy mắt trái: Click trái",
    "• Nháy mắt phải: Click phải", 
    "• Nháy 2 lần: Double click",
    "• Nhìn lên/xuống trái: Cuộn",
    "• Nhắm 2 mắt 5s: Thoát",
    "• Phím Esc: Thoát ngay"
]

for instruction in instructions:
    inst_label = tk.Label(side_frame, text=instruction, font=("Helvetica", 8), bg='#1E2440', fg='white', anchor='w')
    inst_label.pack(pady=1, fill='x')

# Nút cuộn thủ công
manual_label = tk.Label(side_frame, text="CUỘN THỦ CÔNG:", font=("Helvetica", 10, "bold"), bg='#1E2440', fg='#D4B0FF')
manual_label.pack(pady=(20, 5))

up_button = tk.Button(side_frame, text="⬆ CUỘN LÊN", font=("Helvetica", 10), bg='#3D5279', fg='white', width=12,
                      command=lambda: pyautogui.scroll(10))
up_button.pack(pady=5)

down_button = tk.Button(side_frame, text="⬇ CUỘN XUỐNG", font=("Helvetica", 10), bg='#3D5279', fg='white', width=12,
                        command=lambda: pyautogui.scroll(-10))
down_button.pack(pady=5)

# Nút thoát
exit_button = tk.Button(side_frame, text="THOÁT", font=("Helvetica", 10, "bold"), bg='#8B0000', fg='white', width=12,
                        command=lambda: stop_program())
exit_button.pack(pady=(20, 5))

cap = cv2.VideoCapture(0)

def stop_program(event=None):
    print("Đang dừng chương trình...")
    global cap
    cap.release()
    cv2.destroyAllWindows()
    root.quit()

root.bind('<Escape>', stop_program)

def update_camera():
    global tracking_face
    ret, frame = cap.read()
    if ret:
        camera_w = camera_frame.winfo_width()
        camera_h = camera_frame.winfo_height()
        frame = cv2.resize(frame, (camera_w, camera_h))

        if tracking_active:
            if tracking_face is None:
                tracking_face = TrackingFace()
            frame = tracking_face.process_frame(frame)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        camera_frame.imgtk = imgtk
        camera_frame.configure(image=imgtk)

    camera_frame.after(10, update_camera)

tracking_active = True
update_camera()

root.mainloop()

cap.release()
cv2.destroyAllWindows()
