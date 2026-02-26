from data import questions_data
from question_model import Question
from quiz import Quiz
from ui import QuizInterface
import html


questions_bank = []

for item in questions_data:
    question = html.unescape(item['question'])
    answer = item['correct_answer']
    new_question = Question(question=question, answer=answer)
    questions_bank.append(new_question)
    

quiz = Quiz(questions_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()
    
print("You have complete the quiz.")
print(f"Your current score: {quiz.score}/{quiz.question_number}")