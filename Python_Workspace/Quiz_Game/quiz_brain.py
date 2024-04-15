
class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list =  q_list
        self.score = 0
    def next_question(self):
         self.question_number += 1
         question_obj = self.question_list[self.question_number]
         quiz_question = input(f"Q.{self.question_number}: {question_obj.text} (True/False)?: ")
         self.check_answer(quiz_question,question_obj.answer)


    def still_has_question(self):
        #------- Effizienter dadurch dass direkt dann der False und True wert gegeben wird ------
        return self.question_number < len(self.question_list)-1


        #------ So kann man es machen -------
        #lenQu = len(self.question_list)
        #if self.question_number < lenQu-1:
            #return True
        #else:
            #return False
        

        #for i in range (len(self.question_list)):
            #self.question_number = i
            #question_obj = self.question_list[i]
            #quiz_question = input(f"Q.{i+1}: {question_obj.text} (True/False)?: ")

    def check_answer(self,answer, correct_answer):
        
        #lower() um sicher zu sein, dass alles klein geschrieben wird im System
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print(f"The correct answer is {correct_answer}")
            print(f"Your current score: {self.score}/{self.question_number} \n")
        elif answer.lower() != "true" and answer.lower() != "false":  
            print("INVALID INPUT!")
            print(f"Your current score: {self.score}/{self.question_number} \n")        
        else:
            print("That's wrong.")
            print(f"The correct answer is {correct_answer}")
            print(f"Your current score: {self.score}/{self.question_number} \n")
        




