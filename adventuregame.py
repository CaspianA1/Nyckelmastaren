# coding=utf-8
#!/usr/bin/env/python3

# creators: caspian ahlberg, agam winograd,
# christopher ahlberg, stack overflow
# adventure game

import os
import sys
import time
import random
import simpleaudio as sa
from threading import Thread

from Assets.Miscellaneous.formatting import Format
from Assets.Miscellaneous.inventory import InventoryCheck
from Assets.Health_Attack.stats import Stats
from Assets.Battle_System.battle_request import Battle_Request
from Assets.Health_Attack.items import Item
from maps import Position
from Assets.Health_Attack.merchants import Merchant
from Assets.Audio.audio_control import main_audio_loop
from Assets.Health_Attack.status_screen import print_status_screen
from Assets.Health_Attack.items import all_keys
from Assets.Miscellaneous.key_door_event import check_key_inventory, pass_door
from Assets.Visuals.neo_animation_system import show_graphic
from Assets.Miscellaneous.reset_game import full_reset
from Assets.Miscellaneous.neo_2_settings import settings
from Assets.Miscellaneous.bed_check import bed_check
from Assets.Miscellaneous.window_event import window_event
from Assets.Miscellaneous.opening_sequence import opening_sequence

frm = Format()
pos_obj = Position()
ick = InventoryCheck()
stats_obj = Stats()
itm = Item()
merch = Merchant()
request_obj = Battle_Request()
var_dir = os.getcwd() + "/Assets/Global_Vars/"
wall_tuple = ("#", "s", "BW", "W", "A", "P", "O", "wa", "lp", "dp")


def wordsofencouragement():
    outcome = random.randint(1, 5)
    if outcome == 0:
        frm.printfast("\nYou can do it!\n")
    elif outcome == 1:
        frm.printfast("\nGo get 'em, champ!\n")
    elif outcome == 2:
        frm.printfast("\nSlay those monsters!\n")
    elif outcome == 3:
        frm.printfast("\nBelieve in yourself!\n")
    elif outcome == 4:
        frm.printfast("\nYou are a superstar!\n")
    elif outcome == 5:
        frm.printfast("\nIt's all going to be okay!\n")
    else:
        frm.printfast("\nEncouragement error\n")


def locdescription0(mat):
    pos = pos_obj.global_pos("get")
    pos_x, pos_y = pos[0], pos[1]
    if mat[pos_x][pos_y] == "h":
        frm.printfast(
            "\nYou're standing in a dark, misty, hallway made of cobblestone brick.\n"
        )
    elif mat[pos_x][pos_y] == "h2":
        frm.printfast("\nThere's a skylight shining through a cracked window.\n")

    else:
        frm.printfast("\nStop dazing around. You have things to do!\n")


def write_var(var, file):
    var = str(var)
    with open(f"{var_dir}{file}", "w") as size_file:
        size_file.write(var)


def user_input1(input1):
    global var_dir, wall_tuple
    input1 = frm.frm_str(input1)
    pos = pos_obj.global_pos("get")
    pos_x, pos_y = pos[0], pos[1]
    curr_enemy = pos[2]

    prmat = pos_obj.get_mat("prmat")

    num_rows, num_cols = pos_obj.get_rows_cols()

    if input1 == "words of encouragement":
        wordsofencouragement()

    elif input1 == "look around":
        locdescription0(prmat[pos_x][pos_y])

    elif input1 in ("go north", "north", "w"):

        if pos_y >= 0 and prmat[pos_x - 1][pos_y] not in wall_tuple:
            pos_x -= 1
            pos_obj.global_pos("set", pos_x=pos_x, pos_y=pos_y, currentenemy=curr_enemy)
            frm.printmap(prmat)
            frm.printfast("\nYou're going North.\n")
            ick.sword_check(prmat)
            itm.check_for_item(prmat)
            merch.check_for_merchant(prmat)
            request_obj.enemy_at_loc(prmat)
            pass_door(all_keys)
            bed_check()
            window_event()
            pos_obj.map_change()
        else:
            frm.printmap(prmat)
            frm.printfast("\nYou can't go North.\n")
    elif input1 in ("go east", "east", "d"):
        if pos_y < (num_cols - 1) and prmat[pos_x][pos_y + 1] not in wall_tuple:
            pos_y += 1
            pos_obj.global_pos("set", pos_x=pos_x, pos_y=pos_y, currentenemy=curr_enemy)
            frm.printmap(prmat)
            frm.printfast("\nYou're going East.\n")
            ick.sword_check(prmat)
            itm.check_for_item(prmat)
            merch.check_for_merchant(prmat)
            request_obj.enemy_at_loc(prmat)
            pass_door(all_keys)
            bed_check()
            window_event()
            pos_obj.map_change()
        else:
            frm.printmap(prmat)
            frm.printfast("\nYou can't go East.\n")
    elif input1 in ("go south", "south", "s"):
        if pos_x < (num_rows - 1) and prmat[pos_x + 1][pos_y] not in wall_tuple:
            pos_x += 1
            pos_obj.global_pos("set", pos_x=pos_x, pos_y=pos_y, currentenemy=curr_enemy)
            frm.printmap(prmat)
            frm.printfast("\nYou're going South.\n")
            ick.sword_check(prmat)
            itm.check_for_item(prmat)
            merch.check_for_merchant(prmat)
            request_obj.enemy_at_loc(prmat)
            pass_door(all_keys)
            bed_check()
            window_event()
            pos_obj.map_change()
        else:
            frm.printmap(prmat)
            frm.printfast("\nYou can't go South.\n")
    elif input1 in ("go west", "west", "a"):
        if pos_y > 0 and prmat[pos_x][pos_y - 1] not in wall_tuple:
            pos_y -= 1
            pos_obj.global_pos("set", pos_x=pos_x, pos_y=pos_y, currentenemy=curr_enemy)
            frm.printmap(prmat)
            frm.printfast("\nYou're going West.\n")
            ick.sword_check(prmat)
            itm.check_for_item(prmat)
            merch.check_for_merchant(prmat)
            request_obj.enemy_at_loc(prmat)
            pass_door(all_keys)
            bed_check()
            window_event()
            pos_obj.map_change()
        else:
            frm.printmap(prmat)
            frm.printfast("\nYou can't go West.\n")

    elif "item" in input1 or "use" in input1:
        with open(f"{var_dir}item_inventory_data.txt", "r") as inventory_file:
            if inventory_file.read().strip() == "":
                frm.printfast("\nYour inventory is empty. Look around, and you might find something!\n")
                return
            else:
                ick.print_inventory()
                frm.printfast("\nWhich item do you want to use?\n")
                item_request = input("\x1b[5m->\x1b[25m ")
                item_request = frm.frm_str(item_request)
                itm.use_item(item_request)
    elif "inventory" in input1:
        ick.print_inventory()
    elif "location" in input1:
        with open(f"{var_dir}curr_pr_mat.txt", "r") as prmat_file:
            prmat_name = prmat_file.read().strip()
            if "general" in input1:
                show_graphic("overall map")
            if prmat_name in ("prmat0", "prmat1", "prmat2"):
                show_graphic("in castle")
            elif prmat_name == "hprmat05":
                show_graphic("in garden")
            elif prmat_name == "hprmat075":
                show_graphic("in field")
            elif prmat_name == "hprmat_plaza":
                show_graphic("in plaza")
            elif prmat_name == "home_hprmat":
                show_graphic("house frame")

    elif "settings" in input1 or "options" in input1:
        settings()

    elif "help" in input1 or "command" in input1:
        LIST_COMMANDS = [
        "north / w", "east / d", "south / s",
        "west / a", "words of encouragement",
        "item / use", "inventory", "location",
        "settings / options", "help"
        ]
        frm.printfast("\nHere are the available commands:\n")
        for command in LIST_COMMANDS:
            print(f"-> {command}")

    elif input1 == "":
        frm.printmap(prmat)
    else:
        frm.printmap(prmat)
        frm.printfast("\nYou're entering a wrongful command, shame on you\n")  # \n


try:
    input = raw_input
except NameError:
    pass

os.system("printf '\033c'")

is_new_game = open(f"{var_dir}first_game.txt", "r").read()
if (len(sys.argv) > 1 and sys.argv[1] == "new") or is_new_game == "Yes":
        full_reset()
        open(f"{var_dir}first_game.txt", "w").close()
        print_speed = input("Which printing mode do you want? Teletype/Instant: ")
        print_speed = frm.frm_str(print_speed)
        if "teletype" in print_speed: write_var(0.04, "print_speed.txt")
        elif "instant" in print_speed: write_var(0, "print_speed.txt")
        else: frm.printfast("\nThat printing mode is unavailable.\n")
        map_size = input("What map size do you want? 1/2/3: ")
        if "1" in map_size: write_var(1, "map_size.txt")
        elif "2" in map_size: write_var(2, "map_size.txt")
        elif "3" in map_size: write_var(3, "map_size.txt")
        else: frm.printfast("\nThat size is unavailable.\n")
        frm.audio("dream fractal.wav")
        opening_sequence()
else:
    frm.audio("8-Bit 1.wav")
    open(f"{var_dir}first_game.txt", "w").close()
    open(f"{var_dir}audio_stop_check.txt", "w").write("abc")
    os.system("printf '\033c'")
    show_graphic("title screen")
    sa.stop_all()


def main_game_loop():
    while True:
        stats_obj.conditioncheck()

        all_stats = stats_obj.global_stats("get", "all")
        keys_left = 3 - check_key_inventory(ret_num_keys = True, all_keys = all_keys)
        max_sword_name = ""
        if open(f"{var_dir}inventory_data.txt").read().strip() == "":
            max_sword_name = "No sword"
        else:
            max_sword_name = ick.max_sword("name")

        print_status_screen(all_stats, keys_left, max_sword_name)

        hp_fluct = random.choice((1, -1))
        stats_obj.global_stats("set",
        hp = all_stats[0] + hp_fluct,
        hunger = all_stats[1] + hp_fluct,
        dehydration = all_stats[2] + hp_fluct,
        phys_strength = all_stats[3] + hp_fluct,
        intelligence = all_stats[6] + hp_fluct)

        first_input = input("\x1b[5m>\x1b[25m ")
        os.system("printf '\033c'")
        user_input1(first_input)


audio_thread = Thread(target = main_audio_loop)
game_thread = Thread(target = main_game_loop)
game_thread.start()
audio_thread.start()
