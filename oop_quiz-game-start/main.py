from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


##question_count = len(question_data)
##question_list = 0
##score = 0
##
##while question_count < question_list:
##    current_question = question_data[question_list]
##    question = current_question["text"]
##    answer = current_question["answer"]
##    question_list +=1
##    user_answer = input(f"Q{question_list}: {question}, (True/False)?: ")
##    if user_answer.lower() == answer.lower():
##        score +=1
##        print("You got it right!")
##        print(f"The correct answer was: {answer}")
##        print(f"Your current score is: {score}/{question_list}")
##    else:
##        print("That`s wrong!")
##        print(f"The correct answer was: {answer}")
##        print(f"Your current score is: {score}/{question_list}")
##
##



        




    
question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text , answer)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


    

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
