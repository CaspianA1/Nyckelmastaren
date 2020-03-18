# inventory.py

import os
from maps import Position
from .formatting import Format
from ..Health_Attack.swords import all_swords
from ..Health_Attack.items import all_items
from ..Visuals.neo_animation_system import show_graphic


class InventoryCheck:
	frm = Format()
	pos_obj = Position()
	var_dir = os.getcwd() + "/Assets/Global_Vars/"

	def reset_inventory(self):  # TODO: maybe not needed
		with open(f"{self.var_dir}inventory_data.txt", "w") as inventory:
			return

	def print_inventory(self):
		inventory_list = []
		duplicates = {}
		duplicates_as_str = ""

		with open(f"{self.var_dir}inventory_data.txt", "r") as inventory:
			inventory_list += [item.capitalize().strip("\n") for item in inventory]
		with open(f"{self.var_dir}item_inventory_data.txt", "r") as item_inventory:
			inventory_list += [item.capitalize().strip("\n") for item in item_inventory]

		for item in inventory_list:
			if item not in duplicates.keys():
				duplicates[item] = 1
			else:
				duplicates[item] += 1

		blink_char = self.frm.blink("->", end = "", ret_char = True)
		for item, item_amt in duplicates.items():
			if item_amt > 1:
				duplicates_as_str += f"{blink_char} {item_amt}x {item}s\n"
			else:
				duplicates_as_str += f"{blink_char} {item_amt}x {item}\n"

		self.frm.printfast(duplicates_as_str)

	def max_sword(self, get_param=None):
		unsorted_sword_dict = {}
		sorted_sword_dict = {}

		with open(
			f"{self.var_dir}inventory_data.txt", "r"
		) as inventory_file:
			for item in inventory_file:
				item = item.strip("\n")
				unsorted_sword_dict[item] = 0

			for each_sword in all_swords:
				for item in unsorted_sword_dict.keys():
					if each_sword.name == item:
						unsorted_sword_dict[item] = each_sword.strength

			sorted_sword_dict = sorted(unsorted_sword_dict.items(), key=lambda t: t[1])
			max_sword_name = sorted_sword_dict[-1][0]
			max_sword_strength = sorted_sword_dict[-1][1]

			if get_param == "name":
				return max_sword_name

			elif get_param == "strength":
				return max_sword_strength

	def sword_check(self, mat):
		pos = self.pos_obj.global_pos("get")
		pos_x, pos_y = pos[0], pos[1]

		unmodified_inventory = []  # no new items yet
		inventory = []  # may have errors with repeats
		sans_inventory = []  # added item, with no repeats
		with open(
			f"{self.var_dir}inventory_data.txt", "r"
		) as inventory_file:
			for line in inventory_file:
				unmodified_inventory.append(line.strip())
				inventory.append(line.strip())

		for each_sword in all_swords:
			if each_sword.mapletter == mat[pos_x][pos_y]:
				inventory.append(each_sword.name)

		for item in inventory:
			if item not in sans_inventory:
				sans_inventory.append(item)

		for each_sword in all_swords:
			if each_sword.mapletter == mat[pos_x][pos_y]:
				global position_sword
				position_sword = each_sword

		if unmodified_inventory == sans_inventory:
			return
		else:
			self.frm.printfast(
				f"\nThere is a {position_sword.name} at your feet. Do you pick it up?\n",
			)
			while True:
				take_status = input("\x1b[5m->\x1b[25m ")
				take_status = self.frm.frm_str(take_status)

				if "y" in take_status or "k" in take_status:
					self.frm.printfast("\n" + position_sword.description + "\n")
					if position_sword.has_animation:
						show_graphic(position_sword.name)

					break

				elif take_status == "":
					continue
				elif "n" in take_status:
					self.frm.printfast(
						f"\nYou forgot about the {position_sword.name} and kept moving.\n"
					)
					break

				else:
					continue


			if "y" in take_status or "k" in take_status:
				with open(
					f"{self.var_dir}inventory_data.txt", "w"
				) as inventory_file:
					for item in sans_inventory:
						inventory_file.write(item + "\n")
					self.frm.printfast(
						f"\n{position_sword.name.capitalize()} added to inventory.\n"
					)
					return
