from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score_label = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=290, text='Question goes here',
                                                     font=FONT, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='End of Quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true(self):
        self.feedback(self.quiz.check_answer('true'))

    def false(self):
        self.feedback(self.quiz.check_answer('false'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)



