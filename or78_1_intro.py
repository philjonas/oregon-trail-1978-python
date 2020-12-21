import or78_helpers


def need_intro():
    message = '''THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM
    INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847.
    YOUR FAMILY OF FIVE WILL COVER THE 2040 MILE OREGON TRAIL
    IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE.

    YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST
    PAID $200 FOR A WAGON .
    YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE
        FOLLOWING ITEMS:

        OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM
        THE MORE YOU SPEND, THE FASTER YOU'LL GO
        BECAUSE YOU'LL HAVE BETTER ANIMALS

        FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE
        IS OF GETTING SICK

        AMMUNITION - 81 BUYS A BELT OF 50 BULLETS
        YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS
        AND BANDITS, AND FOR HUNTING FOOD

        CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD
        WEATHER YOU WILL ENCOUNTER WHEN CROSSING THE MOUNTAINS

        MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND
        OTHER THINGS YOU WILL NEED FOR SICKNESS
        AND EMERGENCY REPAIRS

    YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -
    OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG
    THE WAY WHEN YOU RUN LOW. H0WEVER, ITEMS COST MORE AT
    THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET
    MORE FOOD.
    WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,
    YOU WILL BE TOLD TO TYPE IN A WORD (ONE THAT SOUNDS LIKE A
    GUN SHOT). THE FASTER YOU TYPE IN THAT WORD AND HIT THE
    "RETURN" KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR GUN.

    AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS
    EXCEPT BULLETS
    WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A "$" "."
    GOOD LUCK!!!
    '''

    reply = or78_helpers.input_yes_no("DO YOU NEED INSTRUCTIONS  (y/n)")
    if reply:
        print(message)


def marksman_level():
    message = '''HOW GOOD A SHOT ARE YOU WITH YOUR RIFLE?
        (1) ACE MARKSMAN,  (2) GOOD SHOT,  (3) FAIR TO MIDDLIN'
        (4) NEED MORE PRACTICE,  (5) SHAKY KNEES
    ENTER ONE OF THE ABOVE -- THE BETTER YOU CLAIM YOU ARE, THE
    FASTER YOU'LL HAVE TO BE WITH YOUR GUN TO BE SUCCESSFUL.'''
    amount = or78_helpers.input_int(message)
    return min(amount, 5)


def oxen():
    message = "HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM ?"
    amount = 0
    while amount < 200 or amount > 300:
        amount = or78_helpers.input_int(message)
        if amount < 200:
            print("NOT ENOUGH")
        elif amount > 300:
            print("TOO MUCH")
    return amount


def general_expenses(var):
    message = "HOW MUCH DO YOU WANT TO SPEND ON {}? ".format(var)
    amount = -1
    while amount < 0:
        amount = or78_helpers.input_int(message)
        if amount < 0:
            print("IMPOSSIBLE")
    return amount


def init(this_vars):
    # ***INSTRUCTIONS***
    need_intro()
    this_vars.shooting_level = marksman_level()
    # *** INITIAL PURCHASES***
    while this_vars.cash_total < 0:
        this_vars.amount_spent_on_animals = oxen()
        this_vars.amount_spent_on_food = general_expenses("FOOD")
        this_vars.amount_spent_on_bullets = general_expenses("AMMUNITION")
        this_vars.amount_spent_on_clothing = general_expenses("CLOTHING")
        this_vars.amount_spent_on_miscellaneous = general_expenses(
            "MISCELLANEOUS SUPPLIES")
        this_vars.cash_total = 700 - this_vars.amount_spent_on_animals - this_vars.amount_spent_on_food - \
            this_vars.amount_spent_on_bullets - this_vars.amount_spent_on_clothing - \
            this_vars.amount_spent_on_miscellaneous
        if this_vars.cash_total < 0:
            print("YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN.")

    print("AFTER ALL YOUR PURCHASES, YOU NOW HAVE {} DOLLARS LEFT".format(
        this_vars.cash_total))
