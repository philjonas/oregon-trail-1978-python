import random
import or78_helpers


def outcome(this_vars):
    if this_vars.hostility_of_riders:
        print("RIDERS WERE HOSTILE--CHECK FOR LOSSES")
        if this_vars.amount_spent_on_bullets < 0:
            print("YOU RAN OUT OF BULLETS AND GOT MASSACRED BY THE RIDERS")
            this_vars.dead = True
    else:
        print("RIDERS WERE FRIENDLY, BUT CHECK FOR POSSIBLE LOSSES")


def shooting_outcome(response_time, this_vars):
    if response_time <= 1:
        print("NICE SHOOTING---YOU DROVE THEM OFF")
        outcome(this_vars)
    elif response_time <= 4:
        print("KINDA SLOW WITH YOUR COLT .45")
        outcome(this_vars)
    else:
        this_vars.is_injured = True
        print("YOU HAVE TO SEE OL' DOC BLANCHARD")
        outcome(this_vars)


def attack_riders(this_vars):
    response_time = or78_helpers.shooting(this_vars.shooting_level)
    this_vars.amount_spent_on_bullets = this_vars.amount_spent_on_bullets - \
        (response_time*40)-80
    shooting_outcome(response_time, this_vars)


def run_from_riders(this_vars):
    this_vars.total_mileage += 20
    this_vars.amount_spent_on_miscellaneous -= 15
    this_vars.amount_spent_on_bullets -= 150
    this_vars.amount_spent_on_animals -= 40
    outcome(this_vars)


def continue_anyway(this_vars):
    if random.random() > .8:
        print("THEY DID NOT ATTACK")
    else:
        this_vars.amount_spent_on_bullets -= 150
        this_vars.amount_spent_on_miscellaneous -= 15
        outcome(this_vars)


def circle_wagons(this_vars):
    response_time = or78_helpers.shooting(this_vars.shooting_level)
    this_vars.amount_spent_on_bullets = this_vars.amount_spent_on_bullets - \
        (response_time*30)-80
    this_vars.total_mileage -= 25
    shooting_outcome(response_time, this_vars)


def non_hostile_choices(choice, this_vars):
    if choice == 2:
        this_vars.total_mileage -= 5
        this_vars.amount_spent_on_bullets -= 100
        outcome(this_vars)
    elif choice == 3:
        pass
        outcome(this_vars)
    elif choice == 4:
        this_vars.total_mileage -= 20
        outcome(this_vars)
    else:
        this_vars.total_mileage += 15
        this_vars.amount_spent_on_animals -= 10
        outcome(this_vars)


def riders(this_vars):
    if random.random()*10 > ((this_vars.total_mileage/100-4)**2+72)/((this_vars.total_mileage/100-4)**2+12)-1:
        return
    this_vars.hostility_of_riders = random.random() < .8
    S5_message = "" if this_vars.hostility_of_riders else "DON'T "
    message = "RIDERS AHEAD.   THEY {}LOOK HOSTILE".format(S5_message)
    print(message)
    if random.random() <= .2:
        this_vars.hostility_of_riders = not this_vars.hostility_of_riders
    choice = 0
    while choice < 1 or choice > 4:
        print("TACTICS")
        choice = or78_helpers.input_int(
            "(1) RUN  (2) ATTACK  (3) CONTINUE  (4) CIRCLE WAGONS? ")
    if this_vars.hostility_of_riders:
        if choice == 2:
            attack_riders(this_vars)
        elif choice == 3:
            continue_anyway(this_vars)
        elif choice == 4:
            circle_wagons(this_vars)
        else:
            run_from_riders(this_vars)
    else:
        non_hostile_choices(choice, this_vars)
