from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()
for q_data in question_data:
    q_text = q_data['question']
    q_answer = q_data['correct_answer']
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while not quiz.end_of_game():
    quiz.next_question()

print(f"Quiz completed. Your final score is {quiz.score}/{len(question_bank)}.")
