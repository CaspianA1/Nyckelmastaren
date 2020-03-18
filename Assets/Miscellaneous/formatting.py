# formatting.py

import os
import sys
import random
import time
import copy
# from copy import deepcopy
import simpleaudio as sa

class Format:
    cwd = os.getcwd()
    var_dir = cwd + "/Assets/Global_Vars/"
    audio_dir = cwd + "/Assets/Audio/WAV_New/"
    audio_dir_sf = audio_dir + "Sound Effects/"

    def frm_str(self, string):
        string = string.lower().strip()
        return string

    def clear_screen(self):
        """
        clear the screen in the command shell
        works on windows (nt, xp, Vista) or Linux
        """
        os.system(["clear", "cls"][os.name == "nt"])

    def erase_screen(self):
        os.system("printf '\033c'")

    def dots(self):
        time.sleep(0.1)
        print("..........")
        time.sleep(0.1)
        print("..........")
        time.sleep(0.1)
        print("..........")
        time.sleep(0.1)

    def printslow(self, string):
        for letter in string:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.1)

    def printfast(self, string, override_speed = False, wait = False):
        if override_speed is False:
            print_speed = float(open(f"{self.var_dir}print_speed.txt", "r").read())
        else:
            print_speed = override_speed
        for letter in string:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(print_speed)
        if wait is True:
            time.sleep(0.5)

    def printsuperfast(self, string):
        for letter in string:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.03)

    def printcrazy(self, string):
        for letter in string:
            sys.stdout.write(letter)
            sys.stdout.flush()
            randnum = random.random() / 6
            time.sleep(randnum)

    def fastblink(self, string):
        for letter in string:
            end = ""
            letter += end
            self.printfast(f"\x1b[5m{letter}\x1b[25m")
            sys.stdout.flush()

    def blink(self, string, end="\n", ret_char = False):  # no arguments yet, doesn't work
        if ret_char is False:
            self.printfast(f"\x1b[5m{string}\x1b[25m" + end)
        else:
            return f"\x1b[5m{string}\x1b[25m" + end

    def sc_use(self, repeat):
        def spinning_cursor():
            while True:
                for cursor in "|/-\\":
                    yield cursor

        spinner = spinning_cursor()
        for _ in range(repeat):
            sys.stdout.write(next(spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")

    def red(self, string, arg=None):
        if arg is None:
            self.printfast("\u001b[31m" + string + "\u001b[30m")
        elif arg == 1:
            self.printslow("\u001b[31m" + string + "\u001b[30m")
        elif arg == 2:
            self.printsuperfast("\u001b[31m" + string + "\u001b[30m")
        elif arg == 3:
            self.printcrazy("\u001b[31m" + string + "\u001b[30m")
        else:
            return "\u001b[31m" + string + "\u001b[30m"

    def green(self, string, arg=None):
        if arg is None:
            self.printfast("\u001b[32m" + string + "\u001b[30m")
        elif arg == 1:
            self.printslow("\u001b[32m" + string + "\u001b[30m")
        elif arg == 2:
            self.printsuperfast("\u001b[32m" + string + "\u001b[30m")
        elif arg == 3:
            self.printcrazy("\u001b[32m" + string + "\u001b[30m")
        else:
            return "\u001b[31m" + string + "\u001b[30m"

    def blue(self, string, arg=None):
        if arg is None:
            self.printfast("\u001b[34m" + string + "\u001b[30m")
        elif arg == 1:
            self.printslow("\u001b[34m" + string + "\u001b[30m")
        elif arg == 2:
            self.printsuperfast("\u001b[34m" + string + "\u001b[30m")
        elif arg == 3:
            self.printcrazy("\u001b[34m" + string + "\u001b[30m")
        else:
            return "\u001b[31m" + string + "\u001b[30m"

    def cyan(self, string, arg=None):
        if arg is None:
            self.printfast("\u001b[36m" + string + "\u001b[30m")
        elif arg == 1:
            self.printslow("\u001b[36m" + string + "\u001b[30m")
        elif arg == 2:
            self.printsuperfast("\u001b[36m" + string + "\u001b[30m")
        elif arg == 3:
            self.printcrazy("\u001b[36m" + string + "\u001b[30m")
        else:
            return "\u001b[31m" + string + "\u001b[30m"

    def yellow(self, string, arg=None):
        if arg is None:
            self.printfast("\u001b[33m" + string + "\u001b[30m")
        elif arg == 1:
            self.printslow("\u001b[33m" + string + "\u001b[30m")
        elif arg == 2:
            self.printsuperfast("\u001b[33m" + string + "\u001b[30m")
        elif arg == 3:
            self.printcrazy("\u001b[33m" + string + "\u001b[30m")
        else:
            return "\u001b[31m" + string + "\u001b[30m"

    def scale_map(self, mat, scale):
        new_mat_across = []
        new_mat_down = []
        sublist = []
        for row in range(0, len(mat)):
            for value in mat[row]:
                for _ in range(scale):
                    sublist.append(value)
            new_mat_across.append(sublist)
            sublist = []
        for row in range(0, len(new_mat_across)):
            for _ in range(scale):
                new_mat_down.append(new_mat_across[row])

        return new_mat_down

    def printmap(self, map):
        # write code that only prints part of the map at a time - like a scrolling map.
        # or maybe additionally - try to write some code that makes movement more fluid when navigating around the map.
        from maps import Position  # this is needed here because up there results in an incorrect relative import
        pos_obj = Position()
        pos = pos_obj.global_pos("get")
        pos_x, pos_y = pos[0], pos[1]
        prmat_name = ""
        with open(f"{self.cwd}/Assets/Global_Vars/curr_pr_mat.txt", "r") as prmat_file:
            prmat_name = prmat_file.read().strip()
        # print different things depending on the prmat
        pmat = copy.deepcopy(map)
        pmat[pos_x][pos_y] = "X"

        with open(f"{self.cwd}/Assets/Global_Vars/map_size.txt", "r") as size_file:
            map_size = int(size_file.read().strip())
            if map_size == 2: pmat = self.scale_map(pmat, 2)
            elif map_size == 3: pmat = self.scale_map(pmat, 3)

        for row in pmat:
            for i in range(0, len(row)):
                curr_char = row[i]

                if prmat_name == "prmat0":
                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "usta0_1" or curr_char == "acr0_0.5":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    else:
                        print(" ", end="")

                elif prmat_name == "hprmat_plaza":
                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "h0":
                        print("\033[48;5;160m" + " " + "\033[0m", end="")  # red, for ground
                    elif curr_char == "W":
                        print("\033[48;5;99m" + " " + "\033[0m", end="")   # ocean-ish blue , for wall
                    elif curr_char == "O":
                        color = random.randint(95, 96)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")   # similar-ish blue , plaza outside
                    elif curr_char == "P":
                        color = random.choice((32, 33))
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")  # another blue, for plaza center
                    elif curr_char == "#":
                        print("\033[48;5;11m" + " " + "\033[0m", end="")  # yellow, for a corner block
                    elif curr_char == "acrplaza_0.75":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    elif curr_char == "gk":
                        color = random.randint(221, 223)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")  # golden-y color
                    elif curr_char == "dr":
                        print("\033[48;5;160m" + " " + "\033[0m", end="")

                elif prmat_name == "home_hprmat":
                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "be":
                        print("\033[48;5;196m" + " " + "\033[0m", end="")
                    elif curr_char == "r":
                        print("\033[48;5;95m" + " " + "\033[0m", end="")
                    elif curr_char == "bu":
                        print("\033[48;5;52m" + " " + "\033[0m", end="")
                    elif curr_char == "ch":
                        print("\033[48;5;231m" + " " + "\033[0m", end="")
                    elif curr_char == "gr":
                        print("\033[48;5;34m" + " " + "\033[0m", end="")
                    elif curr_char == "m":
                        color = random.randint(40, 45)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")
                    elif curr_char == "W":
                        print("\033[48;5;180m" + " " + "\033[0m", end="")
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "h0.25":
                        print("\033[48;5;234m" + " " + "\033[0m", end="")
                    elif curr_char == "En":
                        print("\033[48;5;202m" + " " + "\033[0m", end="")
                    elif curr_char == "acrhome_0.75":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    elif curr_char == "wi":
                        color = random.choice((51, 86, 87))
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")
                    # else:
                        # print(f"CHAR: {curr_char}")

                elif prmat_name == "hprmat075":
                    if curr_char == "sk":
                        color = random.choice((15, 253))
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")
                    elif curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "h0.75t":
                        print("\033[48;5;208m" + " " + "\033[0m", end="")
                    elif curr_char == "h0.75b":
                        color = random.randint(62, 63)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")
                    elif curr_char == "gu":
                        print("\033[48;5;196m" + " " + "\033[0m", end="")
                    elif curr_char == "ni":
                        print("\033[48;5;160m" + " " + "\033[0m", end="")
                    elif curr_char == "to":
                        print("\033[48;5;124m" + " " + "\033[0m", end="")
                    elif (
                        curr_char == "r"
                        # maybe remove some of these
                        or curr_char == "g"
                        or curr_char == "d"
                        or curr_char == "p"
                        or curr_char == "t"
                        or curr_char == "go"
                        or curr_char == "o"
                        or curr_char == "hu"
                        or curr_char == "dr"
                        or curr_char == "m"
                        or curr_char == "w"
                        or curr_char == "bu"
                        or curr_char == "do"
                        ):
                        color = random.randint(208, 209)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")
                    else:
                        # this includes foods, and stairs
                        print("\033[48;5;208m" + " " + "\033[0m", end="")

                elif prmat_name == "hprmat05":
                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "s":
                        color = random.choice((46, 46, 46, 46, 46, 46, 47))
                        print(f"\u001b[{color}m" + " " + "\u001b[0m", end="")
                    elif curr_char == "T":
                        color = random.choice((42, 42, 42, 42, 42, 42, 43))
                        print(f"\u001b[{color};1m" + " " + "\u001b[0m", end="")
                    elif curr_char == "R":
                        print("\u001b[43;1m" + " " + "\u001b[0m", end="")
                    elif curr_char == "h0.5":
                        print(" ", end="")
                    elif curr_char == "gu":
                        print("\033[48;5;196m" + " " + "\033[0m", end="")
                    elif curr_char == "acr0.5_0":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    elif curr_char == "acr0.5_0.75":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")

                elif prmat_name == "prmat1":
                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "h2":
                        print("\033[48;5;37m" + " " + "\033[0m", end="")
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "usta1_2":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    elif curr_char == "dsta1_0":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    elif curr_char == "bk":
                        color = random.randint(166, 168)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")  # a rusty color

                elif prmat_name == "prmat2":

                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "h3":
                        print("\033[48;5;7m" + " " + "\033[0m", end="")  # gray
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "dsta2_1" or curr_char == "acr2_bb":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")
                    elif curr_char == "lp": # light purple
                        print("\033[48;5;128m" + " " + "\033[0m", end="")  # light purple
                    elif curr_char == "tr":  # golden  # triangle, not troll
                        print("\033[48;5;208m" + " " + "\033[0m", end="")  # golden
                    elif curr_char == "dp":
                        print("\033[48;5;91m" + " " + "\033[0m", end="")  # a darker purple
                    elif curr_char == "wa":
                        print("\033[48;5;62m" + " " + "\033[0m", end="")  # blue-purple
                    elif curr_char == "w":
                        color = random.randint(92, 93)
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")  # another purple color
                    elif curr_char == "p":
                        # this is the plasma sword
                        color = random.randint(91, 93)  # 93
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")  # same purple color as the wall
                    elif curr_char == "bl":
                        print("\033[48;5;8m" + " " + "\033[0m", end="")  # darker gray
                    elif curr_char == "ch":
                        color = random.randint(166, 167)  # 166
                        print(f"\033[48;5;{color}m" + " " + "\033[0m", end="")
                    elif curr_char == "m":
                        print("\033[48;5;7m" + " " + "\033[0m", end="")
                    # else:
                        # print(curr_char, end="")  # remove later

                elif prmat_name == "prmat_bbfl":
                    if curr_char == "X":
                        print("\033[31m" + "X" + "\033[0m", end="")
                    elif curr_char == "#":
                        print("\033[7m \033[m", end="")
                    elif curr_char == "bbf":  # bucky ball floor
                        print("\033[48;5;202m" + " " + "\033[0m", end="")
                    elif curr_char == "bb":
                        print("\033[48;5;139m" + " " + "\033[0m", end="")  # a color that works
                    elif curr_char == "acrbb_2":
                        print("\033[48;5;210m" + " " + "\033[0m", end="")

            print()

    def audio(self, audiofile, sound_effect=False, arg=None):
        wave_obj = None

        if sound_effect is False:
            wave_obj = sa.WaveObject.from_wave_file(
                f"{self.audio_dir}{audiofile}"
                )
        else:
            wave_obj = sa.WaveObject.from_wave_file(
                f"{self.audio_dir_sf}{audiofile}"
                )
        play_obj = wave_obj.play()
        if arg is not None:
            return play_obj, wave_obj
