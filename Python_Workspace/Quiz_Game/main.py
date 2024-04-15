from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:

    q = Question(data["question"], data["correct_answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)


#
# loop = False
# while not loop:
# if quiz.still_has_question() == False:
# loop = True
# else:
# quiz.next_question()

# --- die While Schleife läuft so lange bis das Objekt False ist
while quiz.still_has_question():
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
