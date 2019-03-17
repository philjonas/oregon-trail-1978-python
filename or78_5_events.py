import random
import or78_helpers


def cold_weather(this_vars):
    enough_clothes = this_vars.C > 22 + (4 * random.random())
    c_message = "" if enough_clothes else "DON'T "
    message = "COLD WEATHER---BRRRRRRR!---YOU {}HAVE ENOUGH CLOTHING TO KEEP YOU WARM".format(
        c_message)
    print(message)
    if not enough_clothes:
        this_vars.C1 = True
        this_vars.DEAD = True


def heavy_rains(this_vars):
    print("HEAVY RAINS---TIME AND SUPPLIES LOST")
    this_vars.F -= 10
    this_vars.B -= 500
    this_vars.M1 -= 15
    this_vars.M -= (10 * random.random()) - 5


def got_shot(this_vars):
    print("YOU GOT SHOT IN THE LEG AND THEY TOOK ONE OF YOUR OXEN")
    print("BETTER HAVE A DOC LOOK AT YOUR WOUND")
    this_vars.K8 = True
    this_vars.M1 -= 5
    this_vars.A -= 20


##### events array #####
def weather(this_vars):
    if this_vars.M > 950:
        cold_weather(this_vars)
    else:
        heavy_rains(this_vars)


def wagon_break_down(this_vars):
    print("WAGON BREAKS DOWN--LOSE TIME AND SUPPLIES FIXING IT")
    this_vars.M -= 15 - (5 * random.random())
    this_vars.M1 -= 8


def ox_injuries(this_vars):
    print("OX INJURES LEG--SLOWS YOU DOWN REST OF TRIP")
    this_vars.M -= 25
    this_vars.A -= 20


def arm_broke(this_vars):
    print("BAD LUCK--YOUR DAUGHTER BROKE HER ARM")
    print("YOU HAD TO STOP AND USE SUPPLIES TO MAKE A SLING")
    this_vars.M -= 5 - (4 * random.random())
    this_vars.M1 -= 2 - (3 * random.random())


def ox_wander(this_vars):
    print("OX WANDERS OFF--SPEND TIME LOOKING FOR IT")
    this_vars.M -= 17


def helpful_indians(this_vars):
    print("HELPFUL INDIANS SHOW YOU WERE TO FIND MORE FOOD")
    this_vars.F += 14


def lost_son(this_vars):
    print("YOUR SON GETS LOST---SPEND HALF THE DAY LOOKING FOR HIM")
    this_vars.M -= 10


def unsafe_water(this_vars):
    print("UNSAFE WATER--LOSE TIME LOOKING FOR CLEAN SPRING")
    this_vars.M -= (10*random.random()) - 2


def wagon_fire(this_vars):
    print("THERE WAS A FIRE IN YOUR WAGON--FOOD AND SUPPLIES DAMAGE!")
    this_vars.F -= 40
    this_vars.B -= 400
    this_vars.M1 -= (8*random.random()) - 3
    this_vars.M -= 15


def heavy_fog(this_vars):
    print("LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST")
    this_vars.M -= 10 - (5*random.random())


def snake_poison(this_vars):
    print("YOU KILLED A POISONOUS SNAKE AFTER IT BIT YOU")
    this_vars.B -= 10
    this_vars.M1 -= 5
    if this_vars.M1 < 0:
        print("YOU DIE OF SNAKEBITE SINCE YOU HAVE NO MEDICINE")
        this_vars.DEAD = True


def wagon_swamped(this_vars):
    print("WAGON GETS SWAMPED FORDING RIVER--LOSE FOOD AND CLOTHES")
    this_vars.F -= 30
    this_vars.C -= 20
    this_vars.M -= 20 - (20*random.random())


def hail_storm(this_vars):
    print("HAIL STORM---SUPPLIES DAMAGED")
    this_vars.M -= 5 - (10*random.random())
    this_vars.B -= 200
    this_vars.M1 -= 4 - (3*random.random())


def eating(this_vars):
    RND = random.random()
    if this_vars.E == 1:
        or78_helpers.illness(this_vars)
    elif this_vars.E == 3:
        if RND < .5:
            or78_helpers.illness(this_vars)
    else:
        if RND < .25:
            or78_helpers.illness(this_vars)


def animals_attack(this_vars):
    print("WILD ANIMALS ATTACK!")
    response_time = or78_helpers.shooting(this_vars.D9)
    if this_vars.B <= 38:
        print("YOU WERE TOO LOW ON BULLETS--")
        print("THE WOLVES OVERPOWERED YOU")
        this_vars.K8 = True
        this_vars.DEAD = True
        return

    if response_time <= 2:
        print("NICE SHOOTIN' PARDNER---THEY DIDN'T GET MUCH")
    else:
        print("SLOW ON THE DRAW---THEY GOT AT YOUR FOOD AND CLOTHES")
        this_vars.B -= (20 * response_time)
        this_vars.C -= (4 * response_time)
        this_vars.F -= (8 * response_time)


def bandits_attack(this_vars):
    print("BANDITS ATTACK")
    response_time = or78_helpers.shooting(this_vars.D9)
    this_vars.B -= (20 * response_time)

    if this_vars.B < 0:
        print("YOU RAN OUT OF BULLETS---THEY GET LOTS OF CASH")
        this_vars.T /= 3
        got_shot(this_vars)
    else:
        if response_time > 1:
            got_shot(this_vars)
        else:
            print("QUICKEST DRAW OUTSIDE OF DODGE CITY!!!")
            print("YOU GOT 'EM!")


##### events array #####

events_list = [weather, wagon_break_down, ox_injuries, arm_broke,
               ox_wander, helpful_indians, lost_son, unsafe_water,
               wagon_fire, heavy_fog, snake_poison, wagon_swamped,
               hail_storm, eating, animals_attack, bandits_attack]


def events(this_vars):
    ev = random.choice(events_list)
    ev(this_vars)
