class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {question.text} "
                            f"(True or False)?\n").lower()
        correct_answer = question.answer.lower()
        self.question_number += 1
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You are right!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}\n")

    def end_of_game(self):
        return self.question_number >= len(self.question_list)
