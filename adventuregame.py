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


if __name__ == "__main__":
    audio_thread = Thread(target = main_audio_loop)
    game_thread = Thread(target = main_game_loop)
    game_thread.start()
    audio_thread.start()

    # audio_thread.start(); game_thread.start()


# Fix: battlesystem - almost done - now done
# battle system audio - done
# pick up burger items - done
# eventual lack of audio on 3rd floor - done
# Fix: going east on 3rd floor - getter for num_rows and num_cols for certain floors - done
# Add: ability to use items from inventory - done
# Fix/Assert that it is fixed: The map generator, specifically its random item function - done
# Implement: The newer hprmat075 map - done
# Add: The new bitrate 8-Bit 3 track - done
# Convert: Adam's pixel art into ASCII art - did not do
# Remove: The older hprmat075 from maps_data.py - done
# Fix: The trait of removal of an item, after it has been used - done
# Implement: The merchants system - done
# Add: The 3 keys, and the ability to use them from the inventory - STILL NEED TO DO - not needed now
# Add: A duplicate item checker (note: this functionality seems to already be the case for swords) - done
# Fix: the colorscheme for the maps - figure out what the actual colors will be for the floor - done
# Put in: merchants on the map. Also, make sure that the merchants are working - do today - done
# Fix: The max hp message, which happens too often (it should stop, as the hp should be put to 99 after the message) - still need to do - do next - done
# Add: The special Salazar area, and battle - STILL NEED TO DO ***
# Fix: printing inventory, so it looks nicer - done
# Just added (sorta by accident): an inventory size limit - done
# Add: a checker that logs the position and if the item has been picked up, and then checks there again next time - done
# Add: sound effects to regular events, like picking up an item - done
# Fix: negative money issue, with having negative money at certain points after buying with very little money - done
# Add: a feature that says that the player's inventory is empty if it is when requesting to use an item - excluding the swords - done
# Add: plaza map - done
# Fix: hero stats info printing - done
# Add: A title screen, and an option for fighting styles at the beginning *** - will not do fighting styles - can do title screen
# Make: The game an executable with pyinstaller ***
# Added just recently/Made: A small GUI application for selecting different options - done
# Add: A fire intro to the beginning of the game *** - adam is doing
# Add: Animations for all of the key items, and for all of the swords - and next, put them in practically and make sure that they work - done
# Fix: continual low hunger or dehydration messages - they don't show up, which is a bug - fix not needed
# Add: A feature that will do a random chance when attack request is called - so, half the time, attacks will happen *** - done
# Add: A little status screen at the bottom - including health, and items - it should look really nice - done
# Add: when a non-matching input is inputted, just print the mat another time *** - done
# Fix: os error bug with huldra in fight - done
# Add: A large map (for visual purposes), (like from pokemon), that blinks with where you are (big picture) when "location" is inputted - done (but it doesn't work very well) - maybe turn it into a matrix *** - done
# Idea: A flask app, like a website that can run the game - maybe don't do
# Add: A way to scale up the maps - done
# Add: A secret wall, in which you can find the bucky ball *** - done
# Just fixed: A max sword error - done
# Fix/Add: The item count for the inventory *** - done
# Add: the reset game function for where it can be needed (enemies, death in general) - done
# Fix: The messy var_dir code in lots of places - in the process of doing - done
# Add: global var constant objects to the top of every class - done
# Fix: The sorta-broken prmat2, and the audio bindings for it
# Fix: The visual system, and put in place of the old one - done
# Enable: Key use functionality - did not do
# Add: an enemy to the narrow entranceway of the hprmat-plaza - done
# Fix: spelling error, with "one keys left to find" - it should be changed to: "one key left to find" - do next - done
# Fix: the maximum amount of items that you can have in your inventory (it is not working right now)
# Just fixed: error with selecting non-exisiting item - done
# "which item do you want to use" - a spelling error - fix - not an error - done
# coffee is not an item - bug - not really a bug - done
# Fix: error - slaid - slayed - done
# Add: fast printing option - done
# Fix: too fast of a wait after printing single-frame graphics - done
# Add: a stairs sound, like a shuffling sound when you're going up stairs - and the transition too
# Add: a boundary, requiring you to first use the keys when entering - done
# Add (last, but boring): A better interaction layout for the homea
# Add/Remove: The "use key" option - done
# Assert: That after having found all of the keys, that you can enter Salazar's den - done

# FINAL TO DO:

# Title screen animation - from Adam
# Title screen splash screen - I can draw it
# Between-floor splash screens - done
# Ending - done

# Attack probability, when you're at an enemy position - I can do it - done
# Non-matching input, or whitespace results in a printed game screen - I can do that one - done
# Inventory item count - I can write that feature - done
# "1 keys left to find" on information screen - done
# Maximum three per item in inventory - testing right now - done
# Settings - done
# Title screen spelling + 2 new 8-bit songs + big animation
# Clean up house - making it smaller would be a good idea - done
# Isolate project, and remove unneccesary files from final result
# Executable game file - I can do
# Submit to Github
