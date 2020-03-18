# reset_game.py

import os

to_erase = ("item_tracker.txt", "inventory_data.txt")
to_reset = {
"curr_pl_mat.txt": "home_hprmat",
"curr_pr_mat.txt": "home_hprmat",
# "first_game.txt": "Yes",
"item_inventory_data.txt": "burger\nmuscle-milk",
"map_size.txt": "1",
"money.txt": "100",
"player_stats.txt": "100\n10\n10\n50\n50\n50\n50",  # changed from 80 earlier, and 40 before that - then 50, now 100
"savedvariables.txt": "6\n7\nnullenemy"  # "9\n4\nnullenemy"
}

var_dir = os.getcwd() + "/Assets/Global_Vars/"

def write_file(file_name, to_write = None):
    with open(f"{var_dir}{file_name}", "w") as a_file:
        if to_write is None:
            return
        a_file.write(to_write)

def reset_stats():
    stats_as_str = to_reset["player_stats.txt"]
    write_file("player_stats.txt", stats_as_str)

def partial_reset():
    for erase_file_name in to_erase:
        write_file(erase_file_name)
    for reset_file_name, data in to_reset.items():
        write_file(reset_file_name, data)

def full_reset():
    partial_reset()
    with open(f"{var_dir}first_game.txt", "w") as fg_file:
        fg_file.write("Yes")
