dates = ["MARCH 29",
         "APRIL 12 ",
         "APRIL 26 ",
         "MAY 10 ",
         "MAY 24 ",
         "JUNE 7 ",
         "JUNE 21 ",
         "JULY 5 ",
         "JULY 19 ",
         "AUGUST 2 ",
         "AUGUST 16 ",
         "AUGUST 31 ",
         "SEPTEMBER 13 ",
         "SEPTEMBER 27 ",
         "OCTOBER 11 ",
         "OCTOBER 25 ",
         "NOVEMBER 8 ",
         "NOVEMBER 22 ",
         "DECEMBER 6 ",
         "DECEMBER 20 "]

weekdays = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY",
            "THURSDAY", "FRIDAY"]


def print_date(turn_number):
    print("==================================================")
    print("{} {} 1847".format(weekdays[0], dates[turn_number]))
    print("==================================================")


def print_weekday(amount):
    return weekdays[amount % 7]


def print_final_date(D3):
    # mar 29 -> dec 20 1847 = 266 days
    weekday = print_weekday(D3)
    # dec 1 = 246 days
    if D3 > 246:
        return "{} DECEMBER {} 1847".format(weekday, D3 - 246)
    elif D3 > 216:
        return "{} NOVEMBER {} 1847".format(weekday, D3 - 216)
    elif D3 > 185:
        return "{} OCTOBER {} 1847".format(weekday, D3 - 185)
    elif D3 > 155:
        return "{} SEPTEMBER {} 1847".format(weekday, D3 - 155)
    elif D3 > 125:
        return "{} AUGUST {} 1847".format(weekday, D3 - 124)
    else:
        return "{} JULY {} 1847".format(weekday, D3 - 93)
