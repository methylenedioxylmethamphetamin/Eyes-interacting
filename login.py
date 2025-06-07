import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  
import subprocess

def on_go_button_click(event=None):
    user_name = name_entry.get()
    root.withdraw()
    subprocess.Popen(['python', 'main.py', user_name])

root = tk.Tk()
root.title("Ứng Dụng Theo Dõi Mắt")
root.geometry("1000x500")

background_image = Image.open("background.png")  
background_image = background_image.resize((1000, 500), Image.Resampling.LANCZOS)  
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

title_font = font.Font(family="Helvetica", size=20, weight="bold")
text_font = font.Font(family="Helvetica", size=10)
entry_font = font.Font(family="Helvetica", size=12)

title_label = tk.Label(root, text="Ứng Dụng Theo Dõi Mắt", bg='#1E2440', fg='#D4B0FF', font=title_font)
title_label.pack(pady=10)

description_text = ("Ứng dụng theo dõi mắt sử dụng công nghệ tiên tiến\n"
                    "để ghi lại và phân tích chuyển động mắt của người dùng.\n"
                    "Nó có thể nâng cao trải nghiệm người dùng trong nhiều\n"
                    "lĩnh vực như nghiên cứu thị trường, giáo dục và\n"
                    "chăm sóc sức khỏe.\n\n"
                    "Trong giáo dục, nó cung cấp cho các nhà giáo dục\n"
                    "công cụ để đánh giá sự tham gia của học sinh và\n"
                    "tối ưu hóa tài liệu học tập. Trong chăm sóc sức khỏe,\n"
                    "nó có thể hỗ trợ chẩn đoán và điều trị các rối loạn\n"
                    "thị giác và nhận thức bằng cách phân tích cách\n"
                    "bệnh nhân tương tác với môi trường.\n\n"
                    "Nhìn chung, công nghệ này không chỉ cải thiện khả năng\n"
                    "sử dụng và hiệu quả mà còn mở ra những con đường mới\n"
                    "cho nghiên cứu và đổi mới trong nhiều lĩnh vực.")

description_label = tk.Label(root, text=description_text, bg='#1E2440', fg='white', justify="left", font=text_font)
description_label.pack(pady=10)

form_frame = tk.Frame(root, bg='#1E2440')
form_frame.pack(pady=10)

name_label = tk.Label(form_frame, text="TÊN", bg='#1E2440', fg='white', font=text_font)
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, font=entry_font)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(form_frame, text="SỐ ĐIỆN THOẠI", bg='#1E2440', fg='white', font=text_font)
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
phone_entry = tk.Entry(form_frame, font=entry_font)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

go_button = tk.Button(root, text="BẮT ĐẦU", font=entry_font, bg="#3D5279", fg="white", width=10, command=on_go_button_click)
go_button.pack(pady=10)
root.bind('<Return>', on_go_button_click)
root.mainloop()

