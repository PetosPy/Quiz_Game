from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from tkinter import Tk
from ui import QuizInterface

# Hippopotomonstrosesquippedaliophobia

question_bank = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

# while quiz.still_has_questions():
#     quiz.next_question()


print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")











window.mainloop()
