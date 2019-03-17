class GameGlobals:
    def __init__(self):
        self.DEAD = False
        # ***IDENTIFICATION OF VARIABLES IN THE PROGRAM***
        # A = AMOUNT SPENT ON ANIMALS
        self.A = 0
        # B = AMOUNT SPENT ON AMMUNITION
        self.B = 0
        # C = AMOUNT SPENT ON CLOTHING
        self.C = 0
        # C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
        self.C1 = False
        # C$ = YES/NO RESPONSE TO QUESTIONS
        self.CS = None
        # D1 = COUNTER IN GENERATING EVENTS
        self.D1 = None
        # D3 = TURN NUMBER FOR SETTING DATE
        self.D3 = 0
        # D9 = CHOICE OF SHOOTING EXPERTISE LEVEL
        self.D9 = None
        # E = CHOICE OF EATING
        self.E = None
        # F = AMOUNT SPENT ON FOOD
        self.F = 0
        # F1 = FLAG FOR CLEARING SOUTH PASS
        self.F1 = False
        # F2 = FLAG FOR CLEARING BLUE MOUNTAINS
        self.F2 = False
        # K8 = FLAG FOR INJURY
        self.K8 = False
        # L1 = FLAG FOR BLIZZARD
        self.L1 = False
        # M =TOTAL MILEAGE WHOLE TRIP
        self.M = 0
        # M1 = AMOUNT SPENT ON MISCELLANEOUS SUPPLIES
        self.M1 = 0
        # M2 = TOTAL MILEAGE UP THROUGH PREVIOUS TURN
        self.M2 = 0
        # R1 = RANDOM NUMBER IN CHOOSING EVENTS
        self.R1 = None
        # S4 = FLAG FOR ILLNESS
        self.S4 = False
        # S5 = ""HOSTILITY OF RIDERS"" FACTOR
        self.S5 = False
        # T = CASH LEFT OVER AFTER INITIAL PURCHASES
        self.T = -1
        # X = CHOICE OF ACTION FOR EACH TURN
        self.X = None
        # X1 = FLAG FOR FORT OPTION
        self.X1 = False

    def print_inventory(self):
        self.F = max(int(self.F), 0)
        self.B = max(int(self.B), 0)
        self.C = max(int(self.C), 0)
        self.M1 = max(int(self.M1), 0)
        print("=================================================")
        print("FOOD: ", self.F)
        print("BULLETS: ", self.B)
        print("CLOTHING:", self.C)
        print("MISC. SUPP.", self.M1)
        print("CASH", self.T)
        print("=================================================")

    def increment_turn(self):
        self.D3 += 1

    def print_too_long(self):
        print("YOU HAVE BEEN ON THE TRAIL TOO LONG ------")
        print("YOUR FAMILY DIES IN THE FIRST BLIZZARD OF WINTER")
        self.DEAD = True

    def no_turns_left(self, arr):
        return self.D3 >= len(arr)
