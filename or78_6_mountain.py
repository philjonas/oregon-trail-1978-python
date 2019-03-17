import random
import or78_helpers


def blizzard(this_vars):
    print("BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST")
    this_vars.L1 = True
    this_vars.F -= 25
    this_vars.M1 -= 10
    this_vars.B -= 300
    this_vars.M = this_vars.M-30-(40*random.random())
    if this_vars.C < 18 + (2*random.random()):
        or78_helpers.illness(this_vars)


def blue_mountain(this_vars):
    if this_vars.M < 1700:
        return

    if this_vars.F2:
        return
    else:
        this_vars.F2 = True
        if random.random() < .7:
            blizzard(this_vars)


def south_pass(this_vars):
    if this_vars.F1:
        blue_mountain(this_vars)
    else:
        this_vars.F1 = True
        if random.random() < .8:
            blizzard(this_vars)
        else:
            print("YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW")


def rugged_mountain(this_vars):
    print("RUGGED MOUNTAINS")
    if random.random() > .1:
        if random.random() > .11:
            print("THE GOING GETS SLOW")
            this_vars.M -= 45 - (random.random / .2)
            south_pass(this_vars)
        else:
            print("WAGON DAMAGED!—LOSE TIME AND SUPPLIES")
            this_vars.M1 -= 5
            this_vars.B -= 200
            this_vars.M -= 20 - (20 * random.random())
            south_pass(this_vars)
    else:
        print("YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!")
        this_vars.M -= 60
        south_pass(this_vars)


def mountain(this_vars):
    if this_vars.M < 950:
        return

    if random.random()*10 > 9-((this_vars.M/100-15) ^ 2+72)/((this_vars.M/100-15) ** 2+12):
        south_pass(this_vars)
    else:
        rugged_mountain(this_vars)
