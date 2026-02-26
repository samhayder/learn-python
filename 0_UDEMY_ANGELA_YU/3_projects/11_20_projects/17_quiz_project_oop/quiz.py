class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        if self.still_has_question():
            self.current_question = self.question_list[self.question_number]
            self.question_number+= 1
            
            user_answer = input(f"G.{self.question_number}: {self.current_question.question} (True/False)?: ")
            
            self.check_answer(user_answer=user_answer)
            
    def check_answer(self,user_answer):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            print("You are right.")
        else:
            print(f"Wrong answer.")
        
        print(f"Score: {self.score}/{self.question_number}\n")
        
    
    