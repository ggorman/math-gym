# Import the random module
import random

# Import SymPy
from sympy import Rational


# Define some functions that we need below to build up the exercises
def get_random_fraction(a=1, b=10):
    numerator = random.randint(a, b)
    denominator = random.randint(a, b)

    if denominator == 1:
        num = "%d" % numerator
    elif denominator == numerator:
        num = "1"
    else:
        num = "%d/%d" % (numerator, denominator)

    return num, Rational(numerator, denominator)


def get_random_question(a=1, b=10):
    num1, num1_sym = get_random_fraction(a=a, b=b)
    num2, num2_sym = get_random_fraction(a=a, b=b)

    questions = [("%s + %s" % (num1, num2), num1_sym+num2_sym),
                 ("%s - %s" % (num1, num2), num1_sym-num2_sym),
                 ("%s * %s" % (num1, num2), num1_sym*num2_sym),
                 ("%s / %s" % (num1, num2), num1_sym/num2_sym)]

    return random.choice(questions)


def check_answer(expression, answer):
    try:
        n, d = answer.split('/')
    except ValueError:
        n, d = answer, 1

    answer = Rational(int(n), int(d))

    return answer == expression


def quiz_adding_fractions(a=1, b=10, num=10):
    score = 0
    for i in range(num):
        # Get two random fractions
        num1, num1_sym = get_random_fraction()
        num2, num2_sym = get_random_fraction()

        question = "q%d: %s + %s: " % (i, num1, num2)
        answer = input(question)

        if check_answer(num1_sym+num2_sym, answer):
            print("Correct.")
            score += 1
        else:
            print("Incorrect. Correct answer is ", num1_sym+num2_sym,
                  ". Remember to check where you went wrong before moving on.")

    print("score = %d out of %d" % (score, num))
    if score == num:
        print("You aced it. Move onto next level.")
    else:
        print("Practice makes perfect. Try again.")


def quiz_fraction_mania(a=1, b=10, num=10):
    score = 0
    for i in range(num):
        question_str, question_sym = get_random_question()

        question = "q%d: %s: " % (i, question_str)

        answer = input(question)

        if check_answer(question_sym, answer):
            print("Correct.")
            score += 1
        else:
            print("Wrong. Correct answer is ", question_sym,
                  ".Remember to check where you went wrong before moving on.")

    print("score = %d out of %d" % (score, num))
    if score == num:
        print("You aced it. Move onto next level.")
    else:
        print("Practice makes perfect. Try again.")
