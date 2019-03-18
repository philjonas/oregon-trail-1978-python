import random
import or78_helpers


def blizzard(this_vars):
    print("BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST")
    this_vars.is_blizzard = True
    this_vars.amount_spent_on_food -= 25
    this_vars.amount_spent_on_miscellaneous -= 10
    this_vars.amount_spent_on_bullets -= 300
    this_vars.total_mileage = this_vars.total_mileage-30-(40*random.random())
    if this_vars.amount_spent_on_clothing < 18 + (2*random.random()):
        or78_helpers.illness(this_vars)


def blue_mountain(this_vars):
    if this_vars.total_mileage < 1700:
        return

    if this_vars.has_cleared_blue_montains:
        return
    else:
        this_vars.has_cleared_blue_montains = True
        if random.random() < .7:
            blizzard(this_vars)


def south_pass(this_vars):
    if this_vars.has_cleared_south_pass:
        blue_mountain(this_vars)
    else:
        this_vars.has_cleared_south_pass = True
        if random.random() < .8:
            blizzard(this_vars)
        else:
            print("YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW")


def rugged_mountain(this_vars):
    print("RUGGED MOUNTAINS")
    if random.random() > .1:
        if random.random() > .11:
            print("THE GOING GETS SLOW")
            this_vars.total_mileage -= 45 - (random.random / .2)
            south_pass(this_vars)
        else:
            print("WAGON DAMAGED!—LOSE TIME AND SUPPLIES")
            this_vars.amount_spent_on_miscellaneous -= 5
            this_vars.amount_spent_on_bullets -= 200
            this_vars.total_mileage -= 20 - (20 * random.random())
            south_pass(this_vars)
    else:
        print("YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!")
        this_vars.total_mileage -= 60
        south_pass(this_vars)


def mountain(this_vars):
    if this_vars.total_mileage < this_vars.SOUTH_PASS_IN_MILES:
        return

    if random.random()*10 > 9-((this_vars.total_mileage/100-15) ^ 2+72)/((this_vars.total_mileage/100-15) ** 2+12):
        south_pass(this_vars)
    else:
        rugged_mountain(this_vars)
