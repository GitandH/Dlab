import tkinter as tk
import qrcode
from PIL import Image, ImageTk

# QR 코드 생성 함수
def generate_qr_code():
    data = entry.get()  # 입력된 데이터 가져오기

    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,  # QR 코드 버전
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 정정 레벨
        box_size=10,  # 각 박스 크기 (픽셀)
        border=4,  # 테두리 두께
    )
    qr.add_data(data)
    qr.make(fit=True)

    # QR 코드 이미지 생성
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # 이미지를 PhotoImage로 변환
    photo = ImageTk.PhotoImage(image=qr_image)

    # 이미지를 라벨에 표시
    qr_label.config(image=photo)
    qr_label.image = photo

    # 이미지를 파일로 저장
    qr_image.save("qrcode.png")

# tkinter 창 생성
root = tk.Tk()
root.title("QR 코드 생성기")

# 라벨과 입력 필드 생성
label = tk.Label(root, text="QR 코드로 만들 URL 또는 텍스트:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

# "생성" 버튼 생성
generate_button = tk.Button(root, text="QR 코드 생성 및 저장", command=generate_qr_code)
generate_button.pack(pady=10)

# QR 코드 이미지를 표시할 라벨 생성
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
