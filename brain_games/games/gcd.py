from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1, number2 = randint(1, 30), randint(1, 30)
    right_answer = gcd(number1, number2)
    return f'{number1} {number2}', str(right_answer)