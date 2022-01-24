import signal
import sys
from or78_vars import GameGlobals
from or78_1_intro import init
from or78_2_date import print_date, dates
from or78_3_loop import begin, choices, toggle_fort_presence, eating
from or78_4_riders import riders
from or78_5_events import events
from or78_6_mountain import mountain
from or78_7_endings import death, final_turn

"""
 The program that follows is a reconstruction
 of the Oregon Trail game written for HP time-shared
 BASIC by Don Rawitsch and Bill Heinemann and Paul Dillenberger
 in 1971. Its source is an updated version published in the
 July-August 1978 issue of Creative Computing.


 PROGRAM NAME - 0REGON        VERSION:01/01/78
 ORIGINAL PROGRAMMING BY BILL HEINEMANN - 1971
 SUPPORT RESEARCH AND MATERIALS BY DON RAVITSCH
 MINNESOTA EDUCATIONAL COMPUTING CONSORTIUM STAFF
 CDC CYBER 70/73-26 BASIC 3-1
 DOCUMENTATION BOOKLET 'OREGON' AVAILABLE FROM
    MECC SUPPORT SERVICES
    2520 BROADWAY DRIVE
    ST. PAUL, MN  55113
"""
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

def game():
    g_vars = GameGlobals()

    init(g_vars)

    while g_vars.total_mileage < g_vars.GOAL_IN_MILES:
        signal.signal(signal.SIGINT, signal_handler)
        print_date(g_vars.current_date)

        begin(g_vars)
        if g_vars.dead:
            death(g_vars)
            break

        choices(g_vars)
        if g_vars.dead:
            death(g_vars)
            break
        else:
            toggle_fort_presence(g_vars)

        eating(g_vars)

        riders(g_vars)
        if g_vars.dead:
            death(g_vars)
            break

        events(g_vars)
        if g_vars.dead:
            death(g_vars)
            break

        mountain(g_vars)
        if g_vars.dead:
            death(g_vars)
            break

        g_vars.increment_turn()

        if g_vars.no_turns_left(dates):
            g_vars.print_too_long()
            break

    if not g_vars.dead:
        final_turn(g_vars)

    print("END")


if __name__ == "__main__":
    game()
