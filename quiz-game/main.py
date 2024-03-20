from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def create_question_bank():
    question_bank = []
    for question in question_data:
        question_bank.append(Question(text=question["text"], answer=question["answer"]))
    return question_bank


def start_quiz(questions):
    quiz = QuizBrain(questions)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You've completed the quiz.")
    print(f"Your final score is: {quiz.score} / {quiz.question_number}")


def main():
    questions = create_question_bank()
    start_quiz(questions)


if __name__ == "__main__":
    main()  # This is the entry point of the program.
