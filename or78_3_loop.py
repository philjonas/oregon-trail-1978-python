import or78_helpers
import random


def begin(this_vars):
    if this_vars.amount_spent_on_food < 13:
        print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!")
    this_vars.cash_total = int(this_vars.cash_total)
    this_vars.total_mileage = int(this_vars.total_mileage)
    this_vars.total_mileage_previous_turn = this_vars.total_mileage
    if this_vars.has_illness or this_vars.is_injured:
        this_vars.cash_total -= 20
        if this_vars.cash_total < 0:
            this_vars.dead = True
        else:
            print("DOCTOR'S BILL IS $20")
            this_vars.is_injured = this_vars.has_illness = False
    else:
        print("TOTAL MILEAGE IS {}".format(this_vars.total_mileage))
    this_vars.print_inventory()


def spend(value, purse):
    if value > purse:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        print("YOU MISS YOUR CHANCE TO SPEND ON THAT ITEM")
        return purse, value, False
    return purse - value, value, True


def fort(this_vars):
    print("ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING: ")
    this_vars.cash_total, P, is_purchase = spend(
        or78_helpers.input_int('FOOD'), this_vars.cash_total)
    if is_purchase and P > 0:
        this_vars.amount_spent_on_food += (
            this_vars.amount_spent_on_food+2)/(3*P)
    this_vars.cash_total, P, is_purchase = spend(
        or78_helpers.input_int('AMMUNITION'), this_vars.cash_total)
    if is_purchase and P > 0:
        this_vars.amount_spent_on_bullets += int(
            (this_vars.amount_spent_on_bullets+2)/(3*P*50))
    this_vars.cash_total, P, is_purchase = spend(
        or78_helpers.input_int('CLOTHING'), this_vars.cash_total)
    if is_purchase and P > 0:
        this_vars.amount_spent_on_clothing += (
            this_vars.amount_spent_on_clothing+2)/(3*P)
    this_vars.cash_total, P, is_purchase = spend(
        or78_helpers.input_int('MISCELLANEOUS SUPPLIES'), this_vars.cash_total)
    if is_purchase and P > 0:
        this_vars.amount_spent_on_miscellaneous += (
            this_vars.amount_spent_on_miscellaneous+2)/(3*P)
    this_vars.total_mileage -= 45
    continue_on(this_vars)


def hunt(this_vars):
    if this_vars.amount_spent_on_bullets <= 39:
        print("TOUGH---YOU NEED M0RE BULLETS TO GO HUNTING")
        choices(this_vars)
    else:
        this_vars.total_mileage -= 45
        RND = random.random()
        response_time = or78_helpers.shooting(this_vars.shooting_level)
        if response_time <= 1:
            print("RIGHT BETWEEN THE EYES---YOU OOT A BIG ONE!!!!")
            print("FULL BELLIES TONIGHT!")
            this_vars.amount_spent_on_food = (
                this_vars.amount_spent_on_food+52)+(RND*6)
            this_vars.amount_spent_on_bullets = (
                this_vars.amount_spent_on_bullets-10)-(RND*4)
        elif 100*RND < 13*response_time:
            print("YOU MISSED---AND YOUR DINNER GOT AWAY.....")
        else:
            print("NICE SHOT--RIGHT ON TARGET--GOOD EATIN' TONIGHT!!")
            this_vars.amount_spent_on_food = (
                this_vars.amount_spent_on_food+48)-(2*response_time)
            this_vars.amount_spent_on_bullets = (
                this_vars.amount_spent_on_bullets-10)-(3*response_time)
        continue_on(this_vars)


def continue_on(this_vars):
    if this_vars.amount_spent_on_food < 13:
        this_vars.dead = True


def choices(this_vars):
    choice = 0
    choices_1 = []
    if this_vars.has_fort:
        while choice < 1 or choice > 3:
            choice = or78_helpers.input_int(
                "DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, OR (3) CONTINUE? ")
        choices_1 = [fort, hunt, continue_on]
    else:
        while choice < 1 or choice > 2:
            choice = or78_helpers.input_int(
                "DO YOU WANT TO (1) HUNT, OR (2) CONTINUE? ")
        choices_1 = [hunt, continue_on]
    choices_1[choice-1](this_vars)


def toggle_fort_presence(this_vars):
    this_vars.has_fort = not this_vars.has_fort


def eating(this_vars):
    this_vars.choice_of_eating = 0
    while this_vars.choice_of_eating < 1 or this_vars.choice_of_eating > 3:
        this_vars.choice_of_eating = or78_helpers.input_int(
            "DO YOU WANT TO EAT (1) POORLY, (2) MODERATELY OR (3) WELL")
    eaten = (this_vars.amount_spent_on_food-8)-(5*this_vars.choice_of_eating)
    if eaten < 0:
        print("YOU CAN'T EAT THAT WELL")
    else:
        this_vars.amount_spent_on_food = eaten
        this_vars.total_mileage += (this_vars.total_mileage+200+(
            this_vars.amount_spent_on_animals-220)) / (5+(10*random.random()))
        this_vars.is_blizzard = this_vars.is_sufficient_clothing = False
