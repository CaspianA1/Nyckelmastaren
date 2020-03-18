# neo_battlesystem.py

import os
import time
import random
from maps import Position
from ..Visuals.neo_animation_system import show_graphic
from ..Health_Attack.stats import Stats
from ..Health_Attack.enemies import Enemy, all_enemies
from ..Health_Attack.defenses import all_defenses
from ..Health_Attack.attacks import all_attacks
from ..Miscellaneous.formatting import Format
from ..Miscellaneous.inventory import InventoryCheck
from ..Miscellaneous.reset_game import partial_reset
from ..Miscellaneous.ending_screen import ending_screen
from ..Audio.audio_control import stop_audio


class BattleSystem:
    troll, goblin, ogre, huldra, draugr, moloch, wizard = all_enemies
    attack_str = "\nSlash Chest - Stab Heart\nKick Knee - Bash Head\n"
    defense_str = "\nChest Block - Duck\nQuick Dodge - Run Away\n"
    var_dir = os.getcwd() + "/Assets/Global_Vars/"
    pos_obj = Position()
    stats_obj = Stats()
    frm = Format()
    ick = InventoryCheck()

    def __init__(self):
        with open(f"{self.var_dir}current_enemy_health.txt", "w"):
            return

    def check_enemy_death(self):
        with open(f"{self.var_dir}current_enemy_health.txt", "r") as enemy_health_file:
            enemy_health = int(float(enemy_health_file.read().strip()))
        if enemy_health <= 0:
            return True
        else:
            return False


    def check_player_death(self):
        current_hp = self.stats_obj.global_stats("get", "hp")
        if current_hp <= 0:
            return True
        else:
            return False

    def subtract_enemy_health(self, amount):
        previous_health = 0
        new_health = 0
        with open(f"{self.var_dir}current_enemy_health.txt", "r") as enemy_health_file:
            previous_health = float(enemy_health_file.read().strip())
            new_health = previous_health - amount
        with open(f"{self.var_dir}current_enemy_health.txt", "w") as enemy_health_file:
            enemy_health_file.write(str(new_health))

    def subtract_player_health(self, amount):
        # amount = abs(amount)
        previous_hp = self.stats_obj.global_stats("get", "hp")
        current_hp = (previous_hp - amount)
        self.stats_obj.global_stats("set", hp = current_hp)

    def player_move(self, enemy_obj, sword_power):
        currentenemy = enemy_obj
        self.frm.printfast("\nHere are your attacks:\n")
        self.frm.printfast(self.attack_str)
        self.frm.printfast("\nChoose an attack:\n")

        while True:
            attack_choice = input("\x1b[5m->\x1b[25m ")
            attack_choice = self.frm.frm_str(attack_choice)

            for each_attack in all_attacks:
                if each_attack.name == attack_choice:
                    self.frm.audio("hit_noise.wav", sound_effect = True)
                    self.frm.printfast("\n" + each_attack.battle_phrase.format(currentenemy.name) + "\n")

                    player_stats = self.stats_obj.global_stats("get", "all")
                    phys_strength = player_stats[3]
                    mental_strength = player_stats[4]
                    psychic_powers = player_stats[5]
                    reduced_enemy_health = 0.2 * (
                        sword_power + phys_strength + psychic_powers
                    )
                    return reduced_enemy_health

                else:
                    continue

    def enemy_move(self, enemy_obj):
        currentenemy = enemy_obj

        self.frm.printfast("\nHere are your defenses:\n")
        self.frm.printfast(self.defense_str)

        attack_messages = (currentenemy.attack_message, currentenemy.attack_message_2)

        defense_num = random.randint(0, 100)

        if defense_num < currentenemy.defense_chance:
            self.frm.printfast("\nChoose a defense:\n")
            while True:
                defense_choice = input("\x1b[5m->\x1b[25m ")
                defense_choice = self.frm.frm_str(defense_choice)

                for each_defense in all_defenses:
                    if each_defense.name == defense_choice:
                        self.frm.audio("hit_noise.wav", sound_effect = True)
                        player_stats = self.stats_obj.global_stats("get", "all")
                        phys_strength = player_stats[3]
                        mental_strength = player_stats[4]
                        player_subtr_amt = 0


                        if each_defense.name == "quick dodge":
                            self.frm.printfast("\n" + random.choice(attack_messages) + "\n")
                            self.frm.printfast("\n" + each_defense.battle_phrase.format(currentenemy.name) + "\n")
                        elif each_defense.name == "run away":
                            self.frm.printfast( "\n" + random.choice(attack_messages) + "\n")
                            self.frm.printfast("\nDon't trick yourself! You can't run away from a battle.\n")
                            player_subtr_amt = currentenemy.strength - 0.25 * (
                                 mental_strength + each_defense.absorb
                            )
                        else:
                            self.frm.printfast("\n" + random.choice(attack_messages) + "\n")
                            self.frm.printfast("\n" + each_defense.battle_phrase.format(currentenemy.name) + "\n")
                            player_subtr_amt = currentenemy.strength - 0.25 * (mental_strength + each_defense.absorb)

                        return player_subtr_amt

                    else:
                        continue
        else:
            self.frm.printfast(f"\nThe {currentenemy.name} was fast, and attacked first!\n")
            self.frm.printfast("\n" + random.choice(attack_messages) + "\n")
            player_stats = self.stats_obj.global_stats("get", "all")
            phys_strength = player_stats[3]
            mental_strength = player_stats[4]
            player_subtr_amt = currentenemy.strength - (0.25 * mental_strength)
            return player_subtr_amt



    def main(self, mat, who_goes_first, enemy_obj):
        currentenemy = enemy_obj

        with open(f"{self.var_dir}current_enemy_health.txt", "w") as enemy_health_file:
            enemy_health_file.write(str(currentenemy.hp))

        self.frm.printfast(f"\n{currentenemy.description}\n")
        max_sword_name = self.ick.max_sword("name")
        max_sword_strength = self.ick.max_sword("strength")
        self.frm.printfast(
            f"\nYou bear a {max_sword_name} with a power level of {max_sword_strength}.\n"
        )
        show_graphic(currentenemy.name, "intro")

        if who_goes_first == "player":

            while (
                self.check_player_death() is False and self.check_enemy_death() is False
            ):

                hit_power_to_enemy = self.player_move(currentenemy, max_sword_strength)
                self.subtract_enemy_health(hit_power_to_enemy)
                time.sleep(0.5)
                show_graphic(currentenemy.name, "player strike")

                hit_power_to_player = self.enemy_move(currentenemy)
                self.subtract_player_health(hit_power_to_player)
                time.sleep(0.5)
                show_graphic(currentenemy.name, "strike player")

        else:

            while (
                self.check_player_death() is False and self.check_enemy_death() is False
            ):

                hit_power_to_player = self.enemy_move(currentenemy)
                self.subtract_player_health(hit_power_to_player)
                show_graphic(currentenemy.name, "strike player")

                hit_power_to_enemy = self.player_move(currentenemy, max_sword_strength)
                self.subtract_enemy_health(hit_power_to_enemy)
                show_graphic(currentenemy.name, "player strike")

        if currentenemy.name == "wizard":
            stop_audio()
            rand_track = random.choice(("8-Bit 27.wav", "8-Bit 28.wav"))
            self.frm.audio(rand_track)
            partial_reset()
            ending_screen()
            os._exit(0)

        if self.check_enemy_death() is True:
            self.frm.printfast(f"\nYou slayed the {currentenemy.name}!")  # slaid
            time.sleep(0.5)
            show_graphic(currentenemy.name, "enemy death")
            player_stats = self.stats_obj.global_stats("get", "all")
            ksi = currentenemy.kill_stats_incr
            self.stats_obj.global_stats(
                "set",
                hp=player_stats[0] + ksi["hp"],
                phys_strength=player_stats[3] + ksi["phys strength"],
                mental_strength=player_stats[4] + ksi["mental strength"],
                psychic_powers=player_stats[5] + ksi["psychic powers"],
                intelligence=player_stats[6] + ksi["intelligence"],
                )

            for ability in ksi:
                self.frm.printfast(
                    f"\nYour {ability} increased by {ksi[ability]}.\n"
                    )

        elif self.check_player_death() is True:
            self.frm.printfast(
                f"\nThe {currentenemy.name} brought you to your death.\n"
            )
            self.frm.printfast("\nBetter luck next time?\n")
            self.frm.audio("death_noise.wav", sound_effect = True)
            partial_reset()
            os._exit(0)
