from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    right_answer = question % 2 == 0 and 'yes' or 'no'
    return str(question), right_answer
