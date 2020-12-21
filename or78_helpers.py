import random
import time


def input_yes_no(message):
    reply = input(message)
    return True if 'y' in reply else False


def input_int(message):
    text_2_int = None
    while text_2_int == None:
        try:
            text_2_int = int(input(message))
        except:
            text_2_int = None
    return text_2_int


def shooting(shooting_level):
    words = ["bang", "blam", "pow", "wham"]
    word = random.choice(words)
    t0 = time.time()
    typed_word = input("TYPE {}: ".format(word))
    t1 = time.time()
    B1 = (t1-t0)-(shooting_level-1)
    if typed_word != word:
        return 9
    return max(B1, 0)


def illness(this_vars):
    RND = random.random()
    if 100*RND < 10+35*(this_vars.choice_of_eating-1):
        print("MILD ILLNESS---MEDICINE USED")
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_miscellaneous -= 2
    elif 100*RND < 100-(40/4**(this_vars.choice_of_eating-1)):
        print("BAD ILLNESS---MEDICINE USED")
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_miscellaneous -= 5
    else:
        print("SERIOUS ILLNESS")
        print("YOU MUST STOP FOR MEDICAL ATTENTION")
        this_vars.amount_spent_on_miscellaneous -= 10
        this_vars.has_illness = True
