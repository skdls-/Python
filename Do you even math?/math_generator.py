import random
import math
from operator import add, sub, mul
from orm import *


def operation_to_string(op):
    if op == add:
        return "+"
    elif op == sub:
        return "-"
    elif op == mul:
        return "*"


def create_math_problem():
    ops = (add, sub, mul)
    op = random.choice(ops)
    num1, num2 = random.randint(1, 10), random.randint(1, 10)
    answer = op(num1, num2)
    print ("The problem is: ")
    print (num1, operation_to_string(op), num2)
    return answer


def math_generator():
    ops = (add, sub, mul)
    right_guesses_in_a_row = 0

    cond = True
    while cond:
        answer = create_math_problem()
        expectation = input("What is your answer? ")
        expectation = int(expectation)
        if expectation == answer:
            right_guesses_in_a_row += 1
        else:
            cond = False
    else:
        print ("Game over! Your score is: ", right_guesses_in_a_row ** 2)
        return right_guesses_in_a_row ** 2


def start_game():
    curr_player = login()
    this_score = math_generator()
    if this_score > curr_player.max_score:
        curr_player.max_score = this_score
        session.commit()
    session.commit()

def print_top_10():
    position = 1
    top = session.query(Player).order_by(desc(Player.max_score))
    for player in top[:10]:
        print (position, " --- ", player)
        position += 1

start_game()
print_top_10()



