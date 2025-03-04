from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20

reps = 0
check_marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def on_reset():
    global reps, check_marks, timer
    reps = 0
    check_marks = ""

    if timer:
        window.after_cancel(timer)

    label.config(text="TIMER", fg=RED)
    canvas.itemconfig(countdown_text, text="00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def on_start():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 9:
        label.config(text="WELL DONE", fg=RED)
    elif reps % 8 == 0:  
        label.config(text="BREAK", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:   
        label.config(text="BREAK", fg=PINK)
        countdown(short_break_sec)
    else:
        label.config(text="WORK", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global check_marks, timer

    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(countdown_text, text=f"{minutes}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if reps % 2 != 0:
            check_marks += "✔"
            check_mark.config(text=check_marks)
        on_start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="TIMER", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1, pady=10)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
countdown_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 22, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=on_start, width=10)
start_button.grid(row=2, column=0)

check_mark = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(row=2, column=1)

reset_button = Button(text="Reset", command=on_reset, width=10)
reset_button.grid(row=2, column=2)

window.mainloop()
