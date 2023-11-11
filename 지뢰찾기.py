import tkinter as tk
import random
import pygame.mixer

pygame.mixer.init()

def button_clicked():
    pygame.mixer.music.load("hit-sound-effect-12445.mp3")  # 효과음 파일 경로 지정
    pygame.mixer.music.play()

pygame.mixer.music.load("summer.mp3")  # 배경 음악 파일 경로 지정
pygame.mixer.music.play(-1)

initial_time = 0
current_time = initial_time
timer_running = False

def update_timer():
    global current_time
    if timer_running:
        current_time += 1
        # timer_label.config(text=format_time(current_time))
    root.after(1000, update_timer)  # 1초마다 업데이트

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def start_timer():
    global timer_running
    timer_running = True

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global current_time, timer_running
    current_time = initial_time
    timer_running = False
    # timer_label.config(text=format_time(current_time))



# 게임 설정
WIDTH, HEIGHT = 40, 15
MINES = 45

# 지뢰 필드 초기화
field = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
revealed = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
mines = set()
game_over_flag = False  # 게임 오버 상태를 나타내는 플래그

# Tkinter 윈도우 초기화
root = tk.Tk()
root.title("지뢰찾기")


# 지뢰찾기 버튼 클릭 및 우클릭 이벤트 처리
def place_flag(event, x, y):
    if not game_over_flag and not revealed[y][x]:
        if event.num == 3:  # 마우스 오른쪽 버튼 클릭(3)
            if buttons[y][x].cget('text') == "":
                buttons[y][x].config(text="ʕ•͡-•ʔ", fg="black")
            elif buttons[y][x].cget('text') == 'ʕ•͡-•ʔ':#🚩
                buttons[y][x].config(text='')
            

# 버튼 그리기
buttons = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
for y in range(HEIGHT):
    for x in range(WIDTH):
        button = tk.Button(root, width=3, height=2, text="", command=lambda x=x, y=y: click(x, y))
        button.bind('<Button-3>', lambda e, x=x, y=y: place_flag(e, x, y))  # 우클릭 이벤트 바인딩
        button.grid(row=y, column=x)
        buttons[y][x] = button
    

# 버튼 클릭 이벤트 처리
# def click(x, y):
#     if game_over_flag or revealed[y][x]:
#         restart_button.grid_forget()
#         return
    

#     revealed[y][x] = True
#     button = buttons[y][x]

#     if (x, y) in mines:
#         button.config(text="지뢰", background="red")
#         game_over()
#     else:
#         adjacent_mines = sum(1 for dx in [-1, 0, 1] for dy in [-1, 0, 1]
#                              if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT and (x + dx, y + dy) in mines)
#         if adjacent_mines == 0:
#             button.config(text="", background="light gray")
#             for dx in [-1, 0, 1]:
#                 for dy in [-1, 0, 1]:
#                     if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT:
#                         click(x + dx, y + dy)
#         else:
#             button.config(text=str(adjacent_mines), background="light gray")
    
#     if check_win():
#         victory_screen()
# 버튼 클릭 이벤트 처리
def click(x, y):
    if game_over_flag or revealed[y][x]:
        restart_button.grid_forget()
        return

    revealed[y][x] = True
    button = buttons[y][x]

    if (x, y) in mines:
        button.config(text="지뢰", background="red")
        game_over()
    else:
        adjacent_mines = sum(1 for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                             if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT and (x + dx, y + dy) in mines)
        if adjacent_mines == 1:
            button.config(text="", background="light gray")
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT:
                        click(x + dx, y + dy)  # 재귀 호출로 빈 영역을 열기 위해 클릭 함수 호출
        else:
            button.config(text=str(adjacent_mines), background="light gray")

    if check_win():
        victory_screen()

def game_over():
    button_clicked()

    global game_over_flag

    # 게임 오버 라벨
    global game_over_label

    # 재시작 버튼
    global restart_button
    
    game_over_flag = True
    for y in range(HEIGHT):
        for x in range(WIDTH):
            buttons[y][x].config(state=tk.DISABLED)
    game_over_label = tk.Label(root, text="게임 오버", font=("Helvetica", 16))
    game_over_label.grid(row=HEIGHT + 1, columnspan=WIDTH)
    
    restart_button = tk.Button(root, text="다시 시작", command=restart_game)
    restart_button.grid(row=HEIGHT + 2, columnspan=WIDTH)
    
def restart_game():
    start_timer()
    pygame.mixer.music.load("a-long-way-166385.mp3")  # 배경 음악 파일 경로 지정
    pygame.mixer.music.play(-1)
    global game_over_flag
    game_over_flag = False
    for y in range(HEIGHT):
        for x in range(WIDTH):
            revealed[y][x] = False
            buttons[y][x].config(text="", background="SystemButtonFace", state=tk.NORMAL)

    game_over_label.grid_forget()
    restart_button.grid_forget()

    generate_mines()

def check_win():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) not in mines and not revealed[y][x]:
                return False
    return True



def victory_screen():
    if check_win():
        for y in range(HEIGHT):
            for x in range(WIDTH):
                buttons[y][x].config(state=tk.DISABLED)
        victory_label = tk.Label(root, text="승리!", font=("Helvetica", 16))
        victory_label.grid(row=HEIGHT + 1, columnspan=WIDTH)
        restart_button = tk.Button(root, text="다시 시작", command=restart_game)
        restart_button.grid(row=HEIGHT + 2, columnspan=WIDTH)

# 지뢰 생성 함수
def generate_mines():
    global mines
    mines = set()
    while len(mines) < MINES:
        x, y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
        if (x, y) not in mines:
            mines.add((x, y))

generate_mines()

update_timer()

root.mainloop()