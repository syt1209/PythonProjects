from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#08d9d6"
RED = "#ff884b"
GREEN = "#30475e"
YELLOW = "#eaeaea"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=YELLOW)
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="20 minutes break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="5 minutes break", fg=PINK)
    else:
        count_down(work)
        timer_label.config(text="Focus and Work", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minute = math.floor(count / 60)
    second = int(count % 60)
    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks = "✓ " * (reps // 2)
        check_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=GREEN)

# canvas
canvas = Canvas(width=500, height=224, bg=GREEN, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(250, 112, image=tomato_png)
timer_text = canvas.create_text(250, 130, text="00:00", fill="beige", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN, fg=YELLOW)
timer_label.grid(column=1, row=0)
check_label = Label(bg=GREEN, fg=YELLOW, font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

# Button
start_button = Button(text="START", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="RESET", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
