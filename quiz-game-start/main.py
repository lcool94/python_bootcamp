from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

list_question = []
for item in question_data:
    list_question.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(list_question)

while quiz.still_has_question():
    quiz.next_question()
print('Complete.')
print(f"Your score is: {quiz.score}/{quiz.question_number}")