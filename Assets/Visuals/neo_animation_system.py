# otf_animation.py

import os
import sys
import time
import random
from PIL import Image

FRAMES_POSTFIX_4 = ("00", "01", "02", "03")

FRAMES_POSTFIX_12 = (
"00", "01", "02", "03",
"04", "05", "06", "07",
"08", "09", "10", "11")

ENEMY_STYLE_POSTFIX = (
'Idle', 'Intro',
'Enemy Death', 'Strike Player', 'Player Strike')

class AnimationType:
    def __init__(self, prefix, style_postfixes = ENEMY_STYLE_POSTFIX, frame_num = None, is_enemy = True):
        self.prefix = prefix
        self.style_postfixes = style_postfixes
        self.frame_num = frame_num
        self.is_enemy = is_enemy

# shares parts of prefixes would be very effecient
draugr = AnimationType(prefix = "/Assets/Visuals/Animations/Draugr", frame_num = 12, is_enemy = True)
wizard = AnimationType(prefix = "/Assets/Visuals/Animations/Wizard",frame_num = 12, is_enemy = True)
goblin = AnimationType(prefix = "/Assets/Visuals/Animations/Goblin", frame_num = 12, is_enemy = True)
huldra = AnimationType(prefix = "/Assets/Visuals/Animations/Huldra", frame_num = 12, is_enemy = True)
troll = AnimationType(prefix = "/Assets/Visuals/Animations/Troll", frame_num = 12, is_enemy = True)
moloch = AnimationType(prefix = "/Assets/Visuals/Animations/Moloch", frame_num = 12, is_enemy = True)
ogre = AnimationType(prefix = "/Assets/Visuals/Animations/Ogre", frame_num = 12, is_enemy = True)
enemy_animations = {"draugr": draugr, "wizard": wizard, "goblin": goblin, "huldra": huldra, "troll": troll, "moloch": moloch, "ogre": ogre}

transition_1 = AnimationType(prefix = "/Assets/Visuals/Animations/Screen_Transition/Transition 1", style_postfixes = None, frame_num = 12, is_enemy = False)
transition_2 = AnimationType(prefix = "/Assets/Visuals/Animations/Screen_Transition/Transition 2", style_postfixes = None, frame_num = 4, is_enemy = False)
title_screen = AnimationType(prefix = "/Assets/Visuals/Animations/Title\\ Screen", style_postfixes = None, frame_num = 12, is_enemy = False)
intro_one = AnimationType(prefix =  "/Assets/Visuals/Animations/Intro_one", style_postfixes = None, frame_num = 12, is_enemy = False)
intro_two = AnimationType(prefix =  "/Assets/Visuals/Animations/Intro_two", style_postfixes = None, frame_num = 12, is_enemy = False)
intro_three = AnimationType(prefix = "/Assets/Visuals/Animations/Intro_three", style_postfixes = None, frame_num = 12, is_enemy = False)
intro_four = AnimationType(prefix = "/Assets/Visuals/Animations/Intro_four", style_postfixes = None, frame_num = 12, is_enemy = False)
intro_five = AnimationType(prefix = "/Assets/Visuals/Animations/Intro_five", style_postfixes = None, frame_num = 12, is_enemy = False)

rusty_sword = AnimationType(prefix = "/Assets/Visuals/Animations/Rusty_sword", style_postfixes = None, frame_num = 12, is_enemy = False)
gold_sword = AnimationType(prefix = "/Assets/Visuals/Animations/Gold_sword", style_postfixes = None, frame_num = 12, is_enemy = False)
diamond_sword = AnimationType(prefix = "/Assets/Visuals/Animations/Diamond_sword", style_postfixes = None, frame_num = 12, is_enemy = False)
plasma_sword = AnimationType(prefix = "/Assets/Visuals/Animations/Plasma_sword", style_postfixes = None, frame_num = 12, is_enemy = False)
bucky_ball = AnimationType(prefix = "/Assets/Visuals/Animations/Bucky_ball", style_postfixes = None, frame_num = 12, is_enemy = False)
bronze_key =  AnimationType(prefix = "/Assets/Visuals/Animations/Bronze_key", style_postfixes = None, frame_num = 12, is_enemy = False)
silver_key = AnimationType(prefix = "/Assets/Visuals/Animations/Silver_key", style_postfixes = None, frame_num = 12, is_enemy = False)
gold_key = AnimationType(prefix = "/Assets/Visuals/Animations/Gold_key", style_postfixes = None, frame_num = 12, is_enemy = False)

not_enemy_animations = {
"transition 1": transition_1, "transition 2": transition_2, "rusty sword": rusty_sword,
"gold sword": gold_sword, "diamond sword": diamond_sword, "plasma sword": plasma_sword,
"bucky ball": bucky_ball, "bronze key": bronze_key, "silver key": silver_key, "gold key": gold_key,
"title screen": title_screen, "intro one": intro_one, "intro two": intro_two, "intro three": intro_three,
"intro four": intro_four, "intro five": intro_five}

castle_lead_up = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/castle_lead_up.png", frame_num = 1, is_enemy = False)
gold_key_single = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/Gold key.png", frame_num = 1, is_enemy = False)
in_castle = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/in_castle.png", frame_num = 1, is_enemy = False)
in_field = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/in_field.png", frame_num = 1, is_enemy = False)
in_garden = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/in_garden.png", frame_num = 1, is_enemy = False)
in_plaza = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/in_plaza.png", frame_num = 1, is_enemy = False)
overall_map = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/overall_map.png", frame_num = 1, is_enemy = False)
old_window = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/old_window.png", frame_num = 1, is_enemy = False)
plasma_sword_single = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/Plasma Sword.png", frame_num = 1, is_enemy = False)
salazars_den = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/salazar's den.png", frame_num = 1, is_enemy = False)
window_look = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/window_look.png", frame_num = 1, is_enemy = False)
house_frame = AnimationType(prefix = "/Assets/Visuals/Miscellaneous/One_Frame/house_frame.png", frame_num = 1, is_enemy = False)
single_frames = {  # "castle lead up": castle_lead_up,
"gold key single": gold_key_single, "in castle": in_castle, "in field": in_field, "in garden": in_garden, "house frame": house_frame,
"in plaza": in_plaza, "overall map": overall_map,"old window": old_window, "plasma sword single": plasma_sword_single, "salazar's den": salazars_den, "window look": window_look}

all_graphics = (enemy_animations, not_enemy_animations, single_frames)


def get_screen_size():
    try:
        columns, rows = os.get_terminal_size(0)
        avg_size = (columns + rows) / 2
        if avg_size in range(86):
            return 85
        elif avg_size in range(87, 151):
            return 100
        else:
            return 120
    except OSError:
        return 85


erase = lambda: os.system("printf '\033c'")
correct_path = lambda bad_path: bad_path.replace(" ", "\\ ")

def show_frame(frame_path):
    # not using screen size for now
    img = Image.open(frame_path)
    width, height = img.size
    pixels = list(img.getdata())

    space_detector = 0
    for pixel_clump in pixels:
        avg_color = int(sum(pixel_clump) / len(pixel_clump))
        if avg_color == 0: avg_color = random.randint(100, 105)
        print(f"\033[48;5;{avg_color}m  \033[0m", end = "")
        if space_detector % width == 0: print()
        space_detector += 1


# number frames argument not needed (can be found from object)
def show_graphic(graphic_name, animation_style = "", multi_frame = True, wait_speed = "medium"):
    graphic_object = None
    for graphic_category in all_graphics:
        for each_graphic_name, each_graphic_obj in graphic_category.items():
            if each_graphic_name.lower() == graphic_name.lower():
                graphic_object = each_graphic_obj

    needed_postfix = None
    if graphic_object.frame_num == 4:
        needed_postfix = FRAMES_POSTFIX_4
    elif graphic_object.frame_num == 12:
        needed_postfix = FRAMES_POSTFIX_12

    speed = None
    if wait_speed == "slow":
        speed = 0.4
    elif wait_speed == "medium":
        speed = 0.2
    elif wait_speed == "fast":
        speed = 0.1

    movement_category = ""
    for each_postfix in ENEMY_STYLE_POSTFIX:
        if each_postfix.lower() == animation_style.lower():
            movement_category = each_postfix

    if graphic_name == "title screen":
        time.sleep(0.2)
        frame_path = f"{graphic_object.prefix}{movement_category}/"
        the_dir = f"Assets/Visuals/Animations/Title\\ Screen/"
        command = f"viu Assets/Visuals/Animations/Title\\ Screen/sprite_00.png"
        os.system(command)
        new_screen = input("")
        erase()
        command_2 = f"viu Assets/Visuals/Animations/Title\\ Screen/sprite_06.png"
        os.system(command_2)
        time.sleep(2)
        erase()
        return

    if "intro" in graphic_name:
        time.sleep(0.2)
        frame_path = f"{os.getcwd()}{graphic_object.prefix}/{movement_category}/"
        for index, frame_postfix in enumerate(FRAMES_POSTFIX_12):
            show_frame(f"{frame_path}sprite_{frame_postfix}.png")
            time.sleep(speed * 2) if index != 11 else time.sleep(0.8)
            erase()
        return


    if graphic_object.frame_num == 12:
        time.sleep(0.2)
        frame_path = f"{os.getcwd()}{graphic_object.prefix}/{movement_category}/"
        for index, frame_postfix in enumerate(FRAMES_POSTFIX_12):
            show_frame(f"{frame_path}sprite_{frame_postfix}.png")
            time.sleep(speed) if index != 11 else time.sleep(0.4)
            erase()
        return

    elif graphic_object.frame_num == 4:
        time.sleep(0.2)
        frame_path = f"{os.getcwd()}{graphic_object.prefix}{movement_category}/"
        frame_path = correct_path(frame_path)
        for index, frame_postfix in enumerate(FRAMES_POSTFIX_4):
            os.system(f"viu {frame_path}sprite_{frame_postfix}.png")
            time.sleep(0.8)
            time.sleep(speed) if index != 3 else time.sleep(0.6)
            erase()

    elif graphic_object.frame_num == 1:
        time.sleep(1)
        frame_path = f"{os.getcwd()}{graphic_object.prefix}"
        frame_path = correct_path(frame_path)
        os.system(f"viu {frame_path}")
        time.sleep(3)
        erase()


"""
if __name__ == "__main__":
    # this won't work here because it's running correctly from the relative directory of the adventure game.
    show_graphic(graphic_name = "draugr", animation_style = "enemy death", wait_speed = "fast")
"""
