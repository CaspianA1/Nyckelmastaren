# window_event.py

import random
from maps import Position
from .formatting import Format
from ..Visuals.neo_animation_system import show_graphic

pos_obj = Position()
frm = Format()

def window_event():
    pos = pos_obj.global_pos("get")
    prmat = pos_obj.get_mat("prmat")
    pos_x, pos_y, _ = pos
    if prmat[pos_x][pos_y] == "wi":
        frm.printfast("\nYou see a window and look outside.\n")
        window_graphic = random.choice(("old window", "window look"))
        show_graphic(window_graphic)
        frm.printfast("\nIt's beautiful. (Except for Salazar, of course...)\n")
    # show window then
    # you look outside.
    # show window
    # it's beautiful. (except for salazar. (?))

    # change the color of the window, and shift it more to the right
    # and also, make it two pixels wide
