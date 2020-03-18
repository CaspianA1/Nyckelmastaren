# key_door_event.py


import os
from maps import Position
from ..Miscellaneous.formatting import Format

pos_obj = Position()
var_dir = os.getcwd() + "/Assets/Global_Vars"
frm = Format()

def check_for_key():  # TODO: method maybe not used
    pos = pos_obj.global_pos("get")
    pos_x, pos_y = pos[0], pos[1]
    prmat = pos_obj.global_map("prmat")

    for each_key in all_keys:
        if prmat[pos_x][pos_y] == each_key.mapletter:
            frm.printfast(each_key.message)


def check_key_inventory(ret_num_keys, all_keys):
    inventory_data = ""
    key_counter = 0
    with open(f"{var_dir}/item_inventory_data.txt", "r") as inventory_file:
        inventory_data = inventory_file.read()

    for each_key in all_keys:
        # print("each key outer: " + each_key.name)
        if each_key.name in inventory_data:
            # print("each key name: " + each_key.name)
            key_counter += 1
            # print("key counter has increased.")

    if ret_num_keys is True:
        return key_counter

    if key_counter == 3:
        return True
    else:
        return False
        # if key_counter > 3:
            # print("Key counter error in key_door_event.py.")  # I will remove this soon.
        # else:


def check_door_bl():
    pos = pos_obj.global_pos("get")
    pos_x, pos_y = pos[0], pos[1]
    prmat = pos_obj.get_mat("prmat")

    if prmat[pos_x][pos_y] == "bl":  # blockade
         # pass_door()
         return True

def pass_door(all_keys):
    door_message = "\nThis is Salazar's den. If you beat him, you will take his place as the rightful king of this land.\nIf you lose, he will rule this land forever.\n"
    key_message_false = "\nBut, you need the three keys to enter. Come back when you've found them.\n"
    key_message_true = "\nYou have collected the three keys. So, you may enter.\n"
    # door_message = "\nIn front of you is Salazar's home.\nHe has been waiting to slay you, the last member of the royal family.\nThis is your time to win.\n"

    door_status = check_door_bl()
    key_status = check_key_inventory(False, all_keys)


    if door_status is True:
        frm.printfast(door_message)
        if key_status is False:
            frm.printfast(key_message_false)
            pos = pos_obj.global_pos("get")
            pos_x = pos[0] + 1
            pos_obj.global_pos("set", pos_x = pos_x)
            return
        elif key_status is True:
            frm.printfast(key_message_true)
