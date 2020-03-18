# battle_request.py

# from .battle_loops import Battle_Loops
from .neo_battlesystem import BattleSystem
from maps import Position
import random
import time
import os
from ..Health_Attack.enemies import all_enemies
from ..Health_Attack.swords import all_swords  # recently added
from ..Miscellaneous.formatting import Format


class Battle_Request:
    battle_obj = BattleSystem()
    pos_obj = Position()
    # prmat = pos_obj.global_map("get", which_get="prmat")
    prmat = pos_obj.get_mat("prmat")
    frm = Format()

    def __init__(self, counter=3, time_delta=0, total_time_delta=0):
        self.counter = counter
        self.time_delta = time_delta
        self.total_time_delta = total_time_delta

    def success_message(self, enemy_obj):
        self.frm.printfast("\nYou initiated the battle!\n")
        self.battle_obj.main(self.prmat, "player", enemy_obj)

    def failure_message_1(self, enemy_obj):
        self.frm.printfast(f"\nSorry. The {enemy_obj.name} initiated the battle!\n")
        self.battle_obj.main(self.prmat, "enemy", enemy_obj)

    def failure_message_2(self, enemy_obj):
        self.frm.printfast(f"\nToo indecisive! The {enemy_obj.name} initiated the battle.\n")
        self.battle_obj.main(self.prmat, "enemy", enemy_obj)

    def failure_message_3(self, enemy_obj):
        self.frm.printfast(f"\nToo slow. The {enemy_obj.name} initiated the battle!\n")
        self.battle_obj.main(self.prmat, "enemy", enemy_obj)

    def failure_message_4(self, enemy_obj):
        self.frm.printfast(f"\nThat's not an attack. The {enemy_obj.name} initiated the battle!\n")
        self.battle_obj.main(self.prmat, "enemy", enemy_obj)

    def main(self, enemy_wait, enemy_obj):
        cwd = os.getcwd()
        with open(f"{cwd}/Assets/Global_Vars/inventory_data.txt", "r") as sword_file:
            sword_file_data = sword_file.read().strip().strip("\n")

            if sword_file_data == "":
                self.frm.printfast(
                    "\nIt wants to fight you, but you don't have a sword.\n"
                )
                self.frm.printfast("\nCome back later when you've found one!\n")
                return

            # print("sword file data: " + sword_file_data)

            """
            for sword in all_swords:
                print("each sword name: " + sword.name)
                if sword.name not in sword_file.read().strip():
                    self.frm.printfast(
                        "\nIt wants to fight you, but you don't have a sword.\n"
                    )
                    self.frm.printfast("\nCome back later when you've found one!\n")
                    return
            """

        ew = enemy_wait
        self.frm.printfast("\nDo you want to attack?\n")
        attack_status = ""
        while self.counter > 0:
            self.counter -= 1

            time_0 = time.time()
            attack_status = input("\x1b[5m->\x1b[25m ")
            attack_status = attack_status.lower().strip()

            time_1 = time.time()

            self.time_delta = time_1 - time_0

            if attack_status == "":
                if self.total_time_delta >= ew or self.time_delta >= ew:
                    self.total_time_delta += self.time_delta
                    break
                else:
                    self.total_time_delta += self.time_delta
                    continue

            elif self.total_time_delta >= ew and attack_status == "":
                self.total_time_delta += self.time_delta
                break

            elif (
                "y" in attack_status or "k" in attack_status
            ) and self.total_time_delta <= ew:
                self.total_time_delta += self.time_delta
                break

            elif "n" in attack_status:
                self.total_time_delta += self.time_delta
                break

            else:
                if self.total_time_delta <= ew:
                    continue
                else:
                    self.total_time_delta += self.time_delta

        self.total_time_delta += self.time_delta

        if self.total_time_delta <= ew and (
            "y" in attack_status or "k" in attack_status
        ):
            self.success_message(enemy_obj)

        elif "n" in attack_status:
            self.failure_message_1(enemy_obj)

        elif attack_status.strip() == "":
            self.failure_message_2(enemy_obj)

        elif self.counter == 1 or self.total_time_delta >= ew:
            self.failure_message_3(enemy_obj)

        else:
            self.failure_message_4(enemy_obj)

    def calculate_init_attack(self, enemy_obj):
        if enemy_obj.name in ("nullenemy", "goblin", "wizard"):
            return True
        else:
            attack_num = enemy_obj.will_init * random.uniform(0.7, 1.1)
            return True if attack_num > 0.4 else False


    def enemy_at_loc(self, mat):
        cwd = os.getcwd()

        pos_obj = Position()
        pos_x, pos_y, currentenemy_name = pos_obj.global_pos("get")

        # print(mat[pos_x][pos_y])

        for poss_enemy in all_enemies:
            if (
                poss_enemy.mapletter == mat[pos_x][pos_y]
                and poss_enemy.name != "nullenemy"
            ):
                will_attack = self.calculate_init_attack(poss_enemy)
                if will_attack is False:
                    break
                pos_obj.global_pos(
                    "set", pos_x=pos_x, pos_y=pos_y, currentenemy=poss_enemy.name
                )
                self.frm.printfast(f"\nYou see a {poss_enemy.name}!\n")
                self.main(3, poss_enemy)


if __name__ == "__main__":
    bat_obj = Battle_Request()
    bat_obj.main(3)
