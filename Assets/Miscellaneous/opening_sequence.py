# opening_sequence.py

import os
from ..Visuals.neo_animation_system import show_graphic
from .formatting import Format

frm = Format()

def std_msg(*msgs, override_speed = 0.04):
        for msg in msgs:
            frm.printfast(f"\n{msg}\n", override_speed = override_speed)

def opening_sequence():
    frm.erase_screen()
    show_graphic("intro one")
    std_msg("It is raining.", "You have been sleeping for a very long time.")
    frm.sc_use(30)
    std_msg("A long time ago, your father's kingdom was a happy place.", "An abundance of peace coarsed through the veins of the people.")
    frm.sc_use(30)
    std_msg("One day, a very evil man entered this kingdom. His name was Salazar.")
    show_graphic("intro two")
    std_msg("Your father's land was ransacked by him and his comrades.")
    show_graphic("intro three")
    std_msg("He killed your family, the royal family, in the process.", "You are the only one left.")
    frm.sc_use(30)
    std_msg("He has also taken over the castle that you lived in as a young boy.")
    std_msg("To avenge your family, you decide to slay the wizard Salazar.", "But, you may need to discover a few things first...")
    show_graphic("intro four")
    std_msg("Before locking himself in your father's castle, Salazar scattered three keys across the land, sealing the door to his evil lair.")
    std_msg("And legends speak of a legendary sword capable of slaying any evil force...")
    frm.sc_use(30)
    show_graphic("intro five")

    move_on = input("\nDo you move on? Y/N: ")
    if "n" in move_on: std_msg("Coward."); os._exit(0)
