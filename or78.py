from or78_vars import GameGlobals
import or78_1_intro
import or78_2_date
import or78_3_loop
import or78_4_riders
import or78_5_events
import or78_6_mountain
import or78_7_endings

'''
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
'''


def game():
    g_vars = GameGlobals()

    or78_1_intro.init(g_vars)

    while g_vars.total_mileage < g_vars.GOAL_IN_MILES:
        or78_2_date.print_date(g_vars.current_date)

        or78_3_loop.begin(g_vars)
        if g_vars.dead:
            or78_7_endings.death(g_vars)
            break

        or78_3_loop.choices(g_vars)
        if g_vars.dead:
            or78_7_endings.death(g_vars)
            break
        else:
            or78_3_loop.toggle_fort_presence(g_vars)

        or78_3_loop.eating(g_vars)

        or78_4_riders.riders(g_vars)
        if g_vars.dead:
            or78_7_endings.death(g_vars)
            break

        or78_5_events.events(g_vars)
        if g_vars.dead:
            or78_7_endings.death(g_vars)
            break

        or78_6_mountain.mountain(g_vars)
        if g_vars.dead:
            or78_7_endings.death(g_vars)
            break

        g_vars.increment_turn()

        if g_vars.no_turns_left(or78_2_date.dates):
            g_vars.print_too_long()
            break

    if not g_vars.dead:
        or78_7_endings.final_turn(g_vars)

    print('END')


if __name__ == "__main__":
    game()
