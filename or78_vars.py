class GameGlobals:
    def __init__(self):
        self.dead = False
        self.GOAL_IN_MILES = 2040
        self.SOUTH_PASS_IN_MILES = 950

        # ***IDENTIFICATION OF VARIABLES IN THE PROGRAM***
        # A = AMOUNT SPENT ON ANIMALS
        self.amount_spent_on_animals = 0
        # B = AMOUNT SPENT ON AMMUNITION
        self.amount_spent_on_bullets = 0
        # C = AMOUNT SPENT ON CLOTHING
        self.amount_spent_on_clothing = 0
        # C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
        self.is_sufficient_clothing = False
        # D3 = TURN NUMBER FOR SETTING DATE
        self.current_date = 0
        # D9 = CHOICE OF SHOOTING EXPERTISE LEVEL
        self.shooting_level = 5
        # E = CHOICE OF EATING
        self.choice_of_eating = 1
        # F = AMOUNT SPENT ON FOOD
        self.amount_spent_on_food = 0
        # F1 = FLAG FOR CLEARING SOUTH PASS
        self.has_cleared_south_pass = False
        # F2 = FLAG FOR CLEARING BLUE MOUNTAINS
        self.has_cleared_blue_montains = False
        # F9 = FRACTION OF 2 WEEKS TRAVELED ON FINAL TURN
        self.fraction_of_2_weeks = 0
        # K8 = FLAG FOR INJURY
        self.is_injured = False
        # L1 = FLAG FOR BLIZZARD
        self.is_blizzard = False
        # M =TOTAL MILEAGE WHOLE TRIP
        self.total_mileage = 0
        # M1 = AMOUNT SPENT ON MISCELLANEOUS SUPPLIES
        self.amount_spent_on_miscellaneous = 0
        # M2 = TOTAL MILEAGE UP THROUGH PREVIOUS TURN
        self.total_mileage_previous_turn = 0
        # S4 = FLAG FOR ILLNESS
        self.has_illness = False
        # S5 = ""HOSTILITY OF RIDERS"" FACTOR
        self.hostility_of_riders = False
        # T = CASH LEFT OVER AFTER INITIAL PURCHASES
        self.cash_total = -1
        # X1 = FLAG FOR FORT OPTION
        self.has_fort = False

    def print_inventory(self):
        self.amount_spent_on_food = max(int(self.amount_spent_on_food), 0)
        self.amount_spent_on_bullets = max(
            int(self.amount_spent_on_bullets), 0)
        self.amount_spent_on_clothing = max(
            int(self.amount_spent_on_clothing), 0)
        self.amount_spent_on_miscellaneous = max(
            int(self.amount_spent_on_miscellaneous), 0)
        print("=================================================")
        print("FOOD: ", self.amount_spent_on_food)
        print("BULLETS: ", self.amount_spent_on_bullets)
        print("CLOTHING:", self.amount_spent_on_clothing)
        print("MISC. SUPPLIES: ", self.amount_spent_on_miscellaneous)
        print("CASH : $", self.cash_total)
        print("=================================================")

    def increment_turn(self):
        self.current_date += 1

    def print_too_long(self):
        print("YOU HAVE BEEN ON THE TRAIL TOO LONG ------")
        print("YOUR FAMILY DIES IN THE FIRST BLIZZARD OF WINTER")
        self.dead = True

    def no_turns_left(self, arr):
        return self.current_date >= len(arr)
