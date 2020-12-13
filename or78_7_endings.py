import or78_2_date
import or78_helpers


def final_turn(this_vars):
    this_vars.fraction_of_2_weeks = (this_vars.GOAL_IN_MILES-this_vars.total_mileage_previous_turn) / \
        (this_vars.total_mileage-this_vars.total_mileage_previous_turn)
    this_vars.amount_spent_on_food = this_vars.amount_spent_on_food + \
        (1-this_vars.fraction_of_2_weeks)*(8+5*this_vars.choice_of_eating)
    print("YOU FINALLY ARRIVED AT OREGON CITY")
    print("AFTER g_vars.GOAL_IN_MILES LONG MILES---HOORAY !!!!!")
    print("A REAL PIONEER!")
    F9 = int(this_vars.fraction_of_2_weeks*14)
    days = this_vars.current_date*14+F9
    # base_week = or78_2_date.print_date(this_vars.current_date)
    last_date = or78_2_date.print_final_date(days)
    print(last_date)
    this_vars.print_inventory()
    print("PRESIDENT JAMES K. POLK SENDS YOU HIS")
    print("HEARTIEST CONGRATULATIONS")
    print("AND WISHES YOU A PROSPEROUS LIFE AHEAD")
    print("AT YOUR NEW HOME")


def death(this_vars):
    if this_vars.amount_spent_on_food < 12:
        print("YOU RAN OUT OF FOOD AND STARVED TO DEATH")
    elif this_vars.is_sufficient_clothing:
        print("YOU DIED OF PNEUMONIA")
    elif this_vars.cash_total < 0:
        print("YOU CAN'T AFFORD A DOCTOR")
        print("YOU DIED OF PNEUMONIA")
    elif this_vars.amount_spent_on_miscellaneous < 0:
        print("YOU RAN OUT OF MEDICAL SUPPLIES")
    elif this_vars.is_injured:
        print("YOU DIED OF INJURIES")
    print("DUE TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW FORMALITIES WE MUST GO THROUGH")
    minister = or78_helpers.input_yes_no("WOULD YOU LIKE A MINISTER?")
    funeral = or78_helpers.input_yes_no("WOULD YOU LIKE A FANCY FUNERAL?")
    kin = or78_helpers.input_yes_no(
        "WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?")
    if kin:
        print("THAT WILL BE $4.50 FOR THE TELEGRAPH CHARGE.")
    else:
        print("BUT YOUR AUNT SADIE IN ST. LOUIS IS REALLY WORRIED ABOUT YOU")
    print("WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU")
    print("DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON")
    print("BETTER LUCK NEXT TIME")
    print("SINCERELY")
    print("THE OREGON CITY CHAMBER OF COMMERCE")
