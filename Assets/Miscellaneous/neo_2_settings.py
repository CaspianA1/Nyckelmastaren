# neo_2_settings.py

import curses, os
from ..Miscellaneous.reset_game import partial_reset, full_reset
from ..Miscellaneous.formatting import Format


menu = [
"Return to game",
"Printing - Teletype",
"Printing - Instant",
"Screen size - Small",
"Screen size - Medium",
"Screen size - Large",
"Reset - Partial",
"Reset - Full",
"Exit Game"
]

frm = Format()

def write_data(file_name, data):
    var_dir = os.getcwd() + "/Assets/Global_Vars/"
    with open(f"{var_dir}{file_name}", "w") as file_obj:
        file_obj.write(str(data))

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()


def print_center(stdscr, text):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()


def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)

    # (i added this) tan background color
    # curses.init_pair(0, curses.COLOR_WHITE, curses.COLOR_WHITE)
    # stdscr.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)

    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)

    # specify the current selected row
    current_row = 0

    # print the menu
    print_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            option = menu[current_row]
            
            if option == "Return to game":
                curses.endwin()
                break
            elif option == "Printing - Teletype":
                curses.endwin()
                write_data("print_speed.txt", 0.04)
                break
            elif option == "Printing - Instant":
                curses.endwin()
                write_data("print_speed.txt", 0)
                break
            elif option == "Screen size - Small":
                curses.endwin()
                write_data("map_size.txt", 1)
                break
            elif option == "Screen size - Medium":
                curses.endwin()
                write_data("map_size.txt", 2)
                break
            elif option == "Screen size - Large":
                curses.endwin()
                write_data("map_size.txt", 3)
                break
            elif option == "Reset - Partial":
                curses.endwin()
                partial_reset()
                break
            elif option == "Reset - Full":
                curses.endwin()
                full_reset()
                break
            elif option == "Exit Game":
                curses.endwin()
                os.system("printf '\033c'")
                frm.printslow("\nShutting down. .  .\n\n")
                os._exit(0)

            # print_center(stdscr, "You selected '{}'".format(menu[current_row]))
            # stdscr.getch()
            # if user selected last row, exit the program
            if current_row == len(menu)-1:
                break

        print_menu(stdscr, current_row)

def settings():
    curses.wrapper(main)
