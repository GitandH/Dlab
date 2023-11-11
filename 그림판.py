'''import tkinter as tk
import random

class NumberBaseballGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Baseball Game")

        self.secret_number = self.generate_secret_number()
        self.attempts = 0
        self.max_attempts = 5

        self.label = tk.Label(master, text="3자리 수를 입력하세요:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="입력", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def generate_secret_number(self):
        return ''.join(random.sample('0123456789', 3))

    def check_guess(self):
        guess = self.entry.get()
        
        if not guess.isdigit() or len(guess) != 3:
            self.result_label.config(text="똑바로 하자.")
            return
        
        self.attempts += 1
        bulls, cows = self.calculate_bulls_and_cows(guess)

        if bulls == 3:
            self.result_label.config(text=f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
            self.submit_button.config(state=tk.DISABLED)
        else:
            self.result_label.config(text=f"bulls: {bulls}, Cows: {cows}, Attempts: {self.attempts}/{self.max_attempts}")

        if self.attempts >= self.max_attempts:
            self.result_label.config(text=f"Game over! The secret number was {self.secret_number}.")
            self.submit_button.config(state=tk.DISABLED)

    def calculate_bulls_and_cows(self, guess):
        bulls = sum(1 for i in range(3) if guess[i] == self.secret_number[i])
        common_digits = set(self.secret_number) & set(guess)
        cows = len(common_digits) - bulls
        return bulls, cows

def main():
    root = tk.Tk()
    game = NumberBaseballGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
'''
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("그림판")

        self.pen_color = "black"
        self.brush_size = 2

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()

        self.color_label = ttk.Label(root, text="펜 색상:")
        self.color_label.pack()

        self.color_picker = ttk.Combobox(root, values=["black", "red", "green", "blue"])
        self.color_picker.pack()
        self.color_picker.set("black")
        self.color_picker.bind("<<ComboboxSelected>>", self.change_pen_color)

        self.brush_size_label = ttk.Label(root, text="브러쉬 크기:")
        self.brush_size_label.pack()

        self.brush_size_slider = ttk.Scale(root, from_=1, to=10, orient="horizontal", length=200, command=self.change_brush_size)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.pack()

        self.clear_button = ttk.Button(root, text="캔버스 지우기", command=self.clear_canvas)
        self.clear_button.pack()

        self.save_button = ttk.Button(root, text="저장", command=self.save_canvas)
        self.save_button.pack()

        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)

    def start_paint(self, event):
        self.old_x, self.old_y = event.x, event.y

    def paint(self, event):
        new_x, new_y = event.x, event.y
        self.canvas.create_line(
            self.old_x,
            self.old_y,
            new_x,
            new_y,
            fill=self.pen_color,
            width=self.brush_size,
            capstyle=tk.ROUND,
            smooth=tk.TRUE,
        )
        self.old_x, self.old_y = new_x, new_y

    def change_pen_color(self, event):
        self.pen_color = self.color_picker.get()

    def change_brush_size(self, event):
        self.brush_size = int(self.brush_size_slider.get())

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG 파일", "*.png")])
        if file_path:
            try:
                self.canvas.postscript(file=file_path, colormode='color')
            except Exception as e:
                tk.messagebox.showerror("오류", f"오류가 발생했습니다: {str(e)}")

def main():
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
