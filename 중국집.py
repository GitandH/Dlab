import tkinter as tk

class ChineseRestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("중국집 리더기")

        self.menu = {
            "짜장면": {"가격": 5000, "수량": 10, "이미지": r"C:\Users\SAMSUNG\Documents\새 폴더\짜장.png"},
            "짬뽕": {"가격": 6000, "수량": 15, "이미지": r"C:\Users\SAMSUNG\Documents\새 폴더\짬뽕.png"},
            "볶음밥": {"가격": 7000, "수량": 12, "이미지": r"C:\Users\SAMSUNG\Documents\새 폴더\볶음밥.png"},
            "탕수육": {"가격": 12000, "수량": 5, "이미지": r"C:\Users\SAMSUNG\Documents\새 폴더\탕수육.png"},
        }

        self.orders = {}
        self.balance = 0

        self.create_menu()
        self.create_order_frame()

    def create_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(side=tk.LEFT, padx=10)

        label = tk.Label(menu_frame, text="메뉴")
        label.pack()

        self.menu_labels = {}

        for item, details in self.menu.items():
            item_label = tk.Label(menu_frame, text=f"{item}: {details['가격']}원 (수량: {details['수량']})")
            item_label.pack()
            self.menu_labels[item] = item_label

            # 이미지를 표시
            img = tk.PhotoImage(file=details["이미지"])
            item_image_label = tk.Label(menu_frame, image=img)
            item_image_label.image = img
            item_image_label.pack()

            order_button = tk.Button(menu_frame, text="주문", command=lambda i=item: self.add_to_order(i))
            order_button.pack()

    def create_order_frame(self):
        order_frame = tk.Frame(self.root)
        order_frame.pack(side=tk.LEFT, padx=10)

        self.order_label = tk.Label(order_frame, text="주문 내역")
        self.order_label.pack()

        self.order_text = tk.Text(order_frame, height=10, width=30)
        self.order_text.pack()

        total_button = tk.Button(order_frame, text="총액 계산", command=self.calculate_total)
        total_button.pack()

        self.balance_label = tk.Label(order_frame, text="원래 금액")
        self.balance_label.pack()

        self.balance_entry = tk.Entry(order_frame)
        self.balance_entry.pack()

    def add_to_order(self, item):
        if item in self.menu and self.menu[item]['수량'] > 0:
            if item in self.orders:
                self.orders[item] += 1
            else:
                self.orders[item] = 1
            self.menu[item]['수량'] -= 1
            self.update_order_text()
            self.update_menu_labels()
        else:
            self.order_text.insert(tk.END, f"\n{item}은(는) 품절입니다.")

    def update_order_text(self):
        self.order_text.delete(1.0, tk.END)
        for item, quantity in self.orders.items():
            self.order_text.insert(tk.END, f"{item} x{quantity}\n")

    def update_menu_labels(self):
        for item, label in self.menu_labels.items():
            label.config(text=f"{item}: {self.menu[item]['가격']}원 (수량: {self.menu[item]['수량']})")

    def calculate_total(self):
        total = sum(self.menu[item]['가격'] * quantity for item, quantity in self.orders.items())
        self.order_text.insert(tk.END, f"\n총 금액: {total}원")

        try:
            balance = float(self.balance_entry.get())
            if total > balance:
                self.order_text.insert(tk.END, "\n잔액이 부족합니다.")
            else:
                self.order_text.insert(tk.END, f"\n주문이 완료되었습니다. 잔액: {balance - total}원")
        except ValueError:
            self.order_text.insert(tk.END, "\n올바른 잔액을 입력하세요.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChineseRestaurantApp(root)
    root.mainloop()
