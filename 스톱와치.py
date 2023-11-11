import tkinter as tk
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("스톱워치")

        self.running = False
        self.elapsed_time = timedelta(seconds=0)
        self.laps = []

        self.time_display = tk.Label(root, text="00:00:00.000", font=("Arial", 24))
        self.time_display.pack(pady=10)

        self.start_button = tk.Button(root, text="시작", command=self.start_stop)
        self.lap_button = tk.Button(root, text="랩", command=self.lap)
        self.reset_button = tk.Button(root, text="리셋", command=self.reset)

        self.start_button.pack()
        self.lap_button.pack()
        self.reset_button.pack()

        self.lap_display = tk.Listbox(root)
        self.lap_display.pack(pady=10)

        self.update_time()
        
    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.config(text="시작")
        else:
            self.running = True
            self.start_button.config(text="중지")
            self.start_time = datetime.now() - self.elapsed_time
            self.update_time()

    def lap(self):
        if self.running:
            lap_time = datetime.now() - self.start_time
            self.laps.append(lap_time)
            self.lap_display.insert(tk.END, str(lap_time))

    def reset(self):
        if not self.running:
            self.elapsed_time = timedelta(seconds=0)
            self.laps = []
            self.lap_display.delete(0, tk.END)
            self.update_time()

    def update_time(self):
        if self.running:
            self.elapsed_time = datetime.now() - self.start_time
        total_seconds = int(self.elapsed_time.total_seconds())
        milliseconds = int(self.elapsed_time.microseconds / 1000)
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        self.time_display.config(text=time_str)
        if self.running:
            self.root.after(10, self.update_time)  # 10 밀리초마다 업데이트

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
