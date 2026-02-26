from question_model import QuestionModel
from data import question_data
from quiz import QuizBrain
import html

question_list = []

for item in question_data:
    get_question = html.unescape(item["question"])
    get_answer = item['correct_answer']
    new_question_model = QuestionModel(question=get_question, answer=get_answer)
    question_list.append(new_question_model)


quiz = QuizBrain(question_list)

while quiz.still_has_question:
    quiz.next_question()
    
print("Goodby! Finished the quiz.")
print(f"Your Current Score: {quiz.score}")



