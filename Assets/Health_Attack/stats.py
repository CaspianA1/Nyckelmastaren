# stats.py

import os
from ..Miscellaneous.formatting import Format
from maps import Position
from ..Miscellaneous.reset_game import partial_reset

class Stats:
    pos_obj = Position()
    frm = Format()
    var_dir = os.getcwd() + "/Assets/Global_Vars/"

    def global_stats(
        self,
        mode,
        spec_get=None,
        hp=None,
        hunger=None,
        dehydration=None,
        phys_strength=None,
        mental_strength=None,
        psychic_powers=None,
        intelligence=None,
    ):
        if mode == "set":
            stats_data = []
            user_input = [
                hp,
                hunger,
                dehydration,
                phys_strength,
                mental_strength,
                psychic_powers,
                intelligence,
            ]

            with open(f"{self.var_dir}player_stats.txt", "r") as ps_file_r:
                for line in ps_file_r:
                    line = float(line.rstrip("\n"))
                    stats_data.append(line)

            for argument in user_input:
                if argument is not None:
                    argument_index = user_input.index(argument)
                    stats_data[argument_index] = argument

            with open(f"{self.var_dir}player_stats.txt", "w") as ps_file_w:
                for argument in stats_data:
                    ps_file_w.write(str(argument) + "\n")

        elif mode == "get":
            stats_data = []

            with open(f"{self.var_dir}player_stats.txt", "r") as ps_file_r:
                for line in ps_file_r:
                    line = float(line.rstrip("\n"))
                    stats_data.append(line)

            if spec_get == "all":
                return stats_data

            elif spec_get == "hp":
                return stats_data[0]

            elif spec_get == "hunger":
                return stats_data[1]

            elif spec_get == "dehydration":
                return stats_data[2]

            elif spec_get == "phys strength":
                return stats_data[3]

            elif spec_get == "mental strength":
                return stats_data[4]

            elif spec_get == "psychic powers":
                return stats_data[5]

            elif spec_get == "intelligence":
                return stats_data[6]

            else:
                return "Invalid spec_get request for global_stats in stats.py"

        # elif mode == "reset":
            # reset_stats()

    def conditioncheck(self):

        hero_stats = self.global_stats("get", "all")
        hp = hero_stats[0]
        hunger = hero_stats[1]
        dehydration = hero_stats[2]
        phys_strength = hero_stats[3]
        mental_strength = hero_stats[4]
        psychic_powers = hero_stats[5]
        intelligence = hero_stats[6]

        condition_dict_1 = {
            "hp": hp,
            "physical strength": phys_strength,
            "mental strength": mental_strength,
            "psychic powers": psychic_powers,
            "intelligence": intelligence,
        }

        condition_dict_2 = {"hunger": hunger, "dehydration": dehydration}

        for condition_name in condition_dict_1.keys():
            if condition_dict_1[condition_name] >= 200:
                self.frm.printfast(f"\nYour {condition_name} is maxed out.\n\n")
                if condition_name == "hp": self.global_stats("set", hp = 190)
                elif condition_name == "physical strength": self.global_stats("set", phys_strength = 190)
                elif condition_name == "mental strength": self.global_stats("set", mental_strength = 190)
                elif condition_name == "psychic powers": self.global_stats("set", psychic_powers = 190)
                elif condition_name == "intelligence": self.global_stats("set", intelligence = 190)

            elif condition_dict_1[condition_name] <= 0:
                self.frm.printfast(f"\nYou died because of your {condition_name}.\n\n")
                partial_reset()
                os._exit(0)

            # TODO maybe problem with an int and a float
            elif condition_dict_1[condition_name] <= 20:
                self.frm.printfast(f"\nDanger! Your {condition_name} is critical.\n")

        for condition_name in condition_dict_2.keys():
            if condition_dict_2[condition_name] >= 200:
                self.frm.printfast(f"\nYou died because of your {condition_name}.\n")
                reset_game()
                os._exit(0)

            elif condition_dict_2[condition_name] <= 0:
                self.frm.printfast(f"\nYour {condition_name} troubles are gone.\n")
                if condition_name == "hunger":
                    self.global_stats("set", hunger = 10)
                elif condition_name == "dehydration":
                    self.global_stats("set", dehydration = 10)


            elif condition_dict_2[condition_name] < 200 <= 160:
                self.frm.printfast(f"\nDanger! Your {condition_name} level is critical.\n")
