# TODO: asking the question
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz



class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        # Retrieve the item at the curren question_number from the question_list
        current_question = self.questions_list[self.question_number]

        # Use the input function to show the user the Question text and ask for the user's answer
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")

        # Increment the question_number by 1
        self.question_number += 1

        self.check_answer(user_answer=user_answer, correct_answer=current_question.answer)


    def still_has_questions(self):
        # If the number of self.question_number is less than the length of the question list
        # return True, else return False
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        # If user answer is the same as the answer in the current question
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"That's wrong.")
        print(f"Correct answer is: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}\n")