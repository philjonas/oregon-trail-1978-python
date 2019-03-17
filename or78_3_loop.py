import or78_helpers
import random


def begin(this_vars):
    if this_vars.F < 13:
        print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!")
    this_vars.T = int(this_vars.T)
    this_vars.M = int(this_vars.M)
    this_vars.M2 = this_vars.M
    if this_vars.S4 or this_vars.K8:
        this_vars.T -= 20
        if this_vars.T < 0:
            this_vars.DEAD = True
        else:
            print("DOCTOR'S BILL IS $20")
            this_vars.K8 = this_vars.S4 = False
    else:
        print("TOTAL MILEAGE IS {}".format(this_vars.M))
    this_vars.print_inventory()


def spend(value, purse):
    if value > purse:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        print("YOU MISS YOUR CHANCE TO SPEND ON THAT ITEM")
        return purse, value, False
    return purse - value, value, True


def fort(this_vars):
    print("ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING: ")
    this_vars.T, P, is_purchase = spend(
        or78_helpers.input_int('FOOD'), this_vars.T)
    if is_purchase and P > 0:
        this_vars.F += (this_vars.F+2)/(3*P)
    this_vars.T, P, is_purchase = spend(
        or78_helpers.input_int('AMMUNITION'), this_vars.T)
    if is_purchase and P > 0:
        this_vars.B += int((this_vars.B+2)/(3*P*50))
    this_vars.T, P, is_purchase = spend(
        or78_helpers.input_int('CLOTHING'), this_vars.T)
    if is_purchase and P > 0:
        this_vars.C += (this_vars.C+2)/(3*P)
    this_vars.T, P, is_purchase = spend(
        or78_helpers.input_int('MISCELLANEOUS SUPPLIES'), this_vars.T)
    if is_purchase and P > 0:
        this_vars.M1 += (this_vars.M1+2)/(3*P)
    this_vars.M -= 45
    continue_on(this_vars)


def hunt(this_vars):
    if this_vars.B <= 39:
        print("TOUGH---YOU NEED M0RE BULLETS TO GO HUNTING")
        choices(this_vars)
    else:
        this_vars.M -= 45
        RND = random.random()
        response_time = or78_helpers.shooting(this_vars.D9)
        if response_time <= 1:
            print("RIGHT BETWEEN THE EYES---YOU OOT A BIG ONE!!!!")
            print("FULL BELLIES TONIGHT!")
            this_vars.F = (this_vars.F+52)+(RND*6)
            this_vars.B = (this_vars.B-10)-(RND*4)
        elif 100*RND < 13*response_time:
            print("YOU MISSED---AND YOUR DINNER GOT AWAY.....")
        else:
            print("NICE SHOT--RIGHT ON TARGET--GOOD EATIN' TONIGHT!!")
            this_vars.F = (this_vars.F+48)-(2*response_time)
            this_vars.B = (this_vars.B-10)-(3*response_time)
        continue_on(this_vars)


def continue_on(this_vars):
    if this_vars.F < 13:
        this_vars.DEAD = True


def choices(this_vars):
    choice = 0
    choices_1 = []
    if this_vars.X1:
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
    this_vars.X1 = not this_vars.X1


def eating(this_vars):
    this_vars.E = 0
    while this_vars.E < 1 or this_vars.E > 3:
        this_vars.E = or78_helpers.input_int(
            "DO YOU WANT TO EAT (1) POORLY, (2) MODERATELY OR (3) WELL")
    eaten = (this_vars.F-8)-(5*this_vars.E)
    if eaten < 0:
        print("YOU CAN'T EAT THAT WELL")
    else:
        this_vars.F = eaten
        this_vars.M += (this_vars.M+200+(this_vars.A-220)) / (5+(10*random.random()))
        this_vars.L1 = this_vars.C1 = False


if __name__ == '__main__':
    pass
