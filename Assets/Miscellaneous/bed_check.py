# bed_check.py

import time
from maps import Position
from .formatting import Format
from ..Health_Attack.stats import Stats
pos_obj = Position()
frm = Format()
stats_obj = Stats()

def bed_check():
    pos = pos_obj.global_pos("get")
    prmat = pos_obj.get_mat("prmat")
    pos_x, pos_y, _ = pos
    if prmat[pos_x][pos_y] == "be":
        frm.printfast("\nYou're on your bed. Do you want to take a nap?\n")
        while True:
            nap_status = input("\x1b[5m->\x1b[25m ")
            if "y" in nap_status or "k" in nap_status:
                frm.printslow("\nZZzz...\n")
                all_stats = stats_obj.global_stats("get", "all")
                hp, phys_strength, mental_strength = all_stats[0], all_stats[3], all_stats[4]
                stats_obj.global_stats("set", hp = hp + 5, phys_strength = phys_strength + 5, mental_strength = mental_strength + 5)
                time.sleep(5)
                frm.audio("heal_sound.wav", sound_effect = True)
                frm.printslow("\nYou had a nice long nap.\n")
                # frm.printfast("\nYou feel much healthier now.\n")
                frm.printfast("\nYou feel much better now.\n")
                break

            elif "n" in nap_status:
                frm.printfast("\nYou thought you were too tough to take a nap.\n")
                break


# check out plaza later.
# add more randomized colors.
