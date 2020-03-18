# items.py

import os
import math
import time
from .stats import Stats
from ..Miscellaneous.formatting import Format
from maps import Position
from ..Miscellaneous.key_door_event import check_key_inventory
from ..Visuals.neo_animation_system import show_graphic
from ..Health_Attack.swords import all_swords

class Item:
	pos_obj = Position()
	frm = Format()
	var_dir = os.getcwd() + "/Assets/Global_Vars/"
	stats_obj = Stats()
	def __init__(
		self,
		name=None,
		price=None,
		mapletter=None,
		has_animation=False,
		heal_amount=None,
		heal_target=None,
		message=None,
	):
		self.name = name
		self.price = price
		self.mapletter = mapletter
		self.has_animation = has_animation
		self.heal_amount = heal_amount
		self.heal_target = heal_target
		self.message = message

	def get_all_items(self):
		player_items = []
		with open(f"{self.var_dir}item_inventory_data.txt", "r") as inventory_file:
			for item in inventory_file:
				player_items.append(item.strip("\n"))
		return player_items

	def compare_duplicate_data(self, item, pos_x, pos_y, map_name):
		prmat = self.pos_obj.get_mat("prmat")
		duplicate_data = []
		with open(f"{self.var_dir}item_tracker.txt", "r") as tracker_file:
			for line in tracker_file:
				line = line.strip()
				line = line.split()
				duplicate_data.append(line)

		for group in duplicate_data:

			if (group[0] == item.name
			and group[1] == str(pos_x)
			and group[2] == str(pos_y)
			and group[3] == map_name
			):
				return "Item already picked up"


		for item_group in all_items:
			if prmat[pos_x][pos_y] in [item.mapletter for item in item_group]:
				return "Item has not been picked up"

		return "There is not an item here"


	def record_duplicate_item(self, item, pos_x, pos_y, map_name):
		duplicate_data = []
		with open(f"{self.var_dir}item_tracker.txt", "r") as tracker_file:
			for line in tracker_file:
				line = line.strip()
				line = line.split()
				duplicate_data.append(line)
		new_duplicate = [item.name, pos_x, pos_y, map_name]
		duplicate_data.append(new_duplicate)

		with open(f"{self.var_dir}item_tracker.txt", "w") as tracker_file:
			for group in duplicate_data:
				add_str = ""
				for dp in group:
					add_str += str(dp) + " "
				tracker_file.write(add_str.rstrip())
				tracker_file.write("\n")


	def reset_inventory(self):
		with open(f"{self.var_dir}item_inventory_data.txt", "w"):
			return

	def add_to_inventory(self, item):
		inventory_data = []

		with open(f"{self.var_dir}item_inventory_data.txt", "r") as i_file:
			for line in i_file:
				inventory_data.append(line)

		inventory_data = [each_item.strip("\n") for each_item in inventory_data]
		inventory_data.append(item.name)

		with open(f"{self.var_dir}item_inventory_data.txt", "w") as i_file:
			for each_item in inventory_data:
				i_file.write(each_item + "\n")


	def max_items_check(self, item_name):
		# goal of function:
		# get item at current position
		# if there are three of that item in the inventory:
		# return false
		current_items = []
		duplicates = {}

		with open(f"{self.var_dir}/item_inventory_data.txt", "r") as i_file:
			current_items = i_file.read().rstrip().split("\n")

		for item in current_items:
			if item not in duplicates.keys():
				duplicates[item] = 1
			else:
				duplicates[item] += 1

		try:
			amt_of_item = duplicates[item_name]
			if amt_of_item >= 3:
				return True, "old"
			else:
				return False, "old"
		except KeyError:
			return False, "new"


	def use_item(self, item_request):
		inv_data = []
		with open(
			f"{self.var_dir}item_inventory_data.txt", "r"
		) as idata_file:
			for line in idata_file:
				inv_data.append(line)

		item = None
		inv_data = [each_item.strip() for each_item in inv_data]
		# strings of item names

		for each_food in all_foods:
			if each_food.name in item_request:
				item = each_food

		for each_drink in all_drinks:
			if each_drink.name in item_request:
				item = each_drink

		for each_key in all_keys:
			if each_key.name in item_request:
				self.frm.printfast("\nYou can only use the keys at Salazar's lair.\n")
				return

		if (item not in all_foods
		and item not in all_drinks
		and item not in all_keys):
			# self.frm.printfast("\nThat's not an item.\n")
			self.frm.printfast("\nSorry, that item isn't available.\n")
			return

		if item in all_keys:
			num_keys_left = 3 - check_key_inventory(ret_num_keys = True, all_keys = all_keys)
			if num_keys_left != 0:
				self.frm.printfast(f"\nYou may only use your {item.name} once you have found all of the keys.\n")
				self.frm.printfast("\nUsing these three keys, you will gain entrance to the great wizard Salazar's lair.\n")
				return

		if item.name not in inv_data:
			self.frm.printfast(f"\nYou don't have any {item.name}s left.\n")
			return

		for _ in range(0, item.heal_amount, 4):
			self.frm.audio("print_blip_3.wav", sound_effect = True)
			time.sleep(0.05)

		else:
			for each_ht in item.heal_target:
				current_heal_amt = self.stats_obj.global_stats("get", each_ht)
				if each_ht == "hp": self.stats_obj.global_stats("set", hp = current_heal_amt + item.heal_amount)
				elif each_ht == "hunger": self.stats_obj.global_stats("set", hunger = current_heal_amt - item.heal_amount)
				elif each_ht == "dehydration": self.stats_obj.global_stats("set", dehydration = current_heal_amt - item.heal_amount)
				elif each_ht == "phys strength": self.stats_obj.global_stats("set", phys_strength = current_heal_amt + item.heal_amount)
				elif each_ht == "mental strength": self.stats_obj.global_stats("set", mental_strength = current_heal_amt + item.heal_amount)
				elif each_ht == "psychic powers": self.stats_obj.global_stats("set", psychic_powers = current_heal_amt + item.heal_amount)
				elif each_ht == "intelligence": self.stats_obj.global_stats("set", intelligence = current_heal_amt + item.heal_amount)

		self.frm.printfast(f"\n{item.message}\n")

		inventory_data = []
		with open(
			f"{self.var_dir}item_inventory_data.txt", "r"
		) as idata_file:
			for line in idata_file:
				inventory_data.append(line)

		for index, each_item in enumerate(inventory_data):
			inventory_data[index] = each_item.strip("\n")

		for each_item in inventory_data:
			if each_item == item.name:
				inventory_data.remove(item.name)

		with open(
			f"{self.var_dir}item_inventory_data.txt", "w"
		) as idata_file:
			for item in inventory_data:
				idata_file.write(item + "\n")


	def check_for_item(self, mat):
		# print("In check for item")
		pos = self.pos_obj.global_pos("get")
		pos_x, pos_y = pos[0], pos[1]
		map_name = ""
		with open(f"{self.var_dir}curr_pr_mat.txt", "r") as stored_mat_file:
			map_name = stored_mat_file.read()

		item = None
		for each_food in all_foods:
			if mat[pos_x][pos_y] == each_food.mapletter:
				item = each_food

		for each_drink in all_drinks:

			if mat[pos_x][pos_y] == each_drink.mapletter:
				item = each_drink

		for each_key in all_keys:
			if mat[pos_x][pos_y] == each_key.mapletter:
				item = each_key

		if item is None: return

		pickup_status = self.compare_duplicate_data(item, pos_x, pos_y, map_name)
		if pickup_status == "Item already picked up":
			return
		elif pickup_status == "Item has not been picked up":

			pass
		elif pickup_status == "There is not an item here":
			return

		if (mat[pos_x][pos_y] == item.mapletter):
			duplicate_data = self.max_items_check(item.name)

			if duplicate_data[1] == "new":
				self.frm.printfast("\nThere's a new type of item on the ground!\n")
				self.frm.printfast(f"\nIt's a {item.name}. Do you pick it up?\n")
			elif duplicate_data[1] == "old":
				if duplicate_data[0] is False:
					self.frm.printfast(f"\nThere's a {item.name} on the ground.\n")
					self.frm.printfast("\nDo you pick it up?\n")
				elif duplicate_data[0] is True:
					self.frm.printfast(f"\nYou found a {item.name}!\n")
					self.frm.printfast(f"\nBut your inventory can't fit any more {item.name}s.\n")
					return

			while True:
				take_status = input("\x1b[5m->\x1b[25m ")
				take_status = self.frm.frm_str(take_status)

				if "y" in take_status or "k" in take_status:
					self.add_to_inventory(item)
					self.record_duplicate_item(item, pos_x, pos_y, map_name)
					self.frm.printfast(f"\nYou added the {item.name} to your inventory.\n")
					self.frm.audio("item_pick_up.wav", sound_effect = True)

					if item.has_animation:
						corrected_item_name = item.name.replace("-", " ")
						show_graphic(corrected_item_name)

					if item.name in [key.name for key in all_keys]:
						keys_left = 3 - check_key_inventory(ret_num_keys = True, all_keys = all_keys)
						plural = "key" if keys_left == 1 else "keys"
						self.frm.printfast(f"\nYou have {keys_left} {plural} left to find.\n")

					break

				elif "n" in take_status:
					self.frm.printfast(f"\nYou left the {item.name} alone and kept moving.\n")
					break


class Food(Item):
	def __init__(self, name, price, mapletter, has_animation, heal_amount, heal_target, message):
		super().__init__(name, price, mapletter, has_animation, heal_amount, heal_target, message)

parmesan_cheese = Food(
	name="parmesan-cheese",
	price=2,
	mapletter="pch",
	has_animation=False,
	heal_amount=20,
	heal_target=("hp", "hunger"),
	message="The parmesan cheese increased your HP."
)

burger = Food(
	name="burger",
	price=3,
	mapletter="bu",
	has_animation=False,
	heal_amount=25,
	heal_target=("hp", "hunger"),
	message="The burger is delicious, and it helped your HP."
)

lasagna = Food(
	name="lasagna",
	price=4,
	mapletter="la",
	has_animation=False,
	heal_amount=30,
	heal_target=("hp", "hunger"),
	message="The lasagna tastes amazing, and it helped your HP."
)

chicken = Food(
	name="chicken",
	price=5,
	mapletter="ch",
	has_animation=False,
	heal_amount=35,
	heal_target=("hp", "hunger"),
	message="This tasty chicken helped your HP."
)

class Drink(Item):
	def __init__(self, name, price, mapletter, has_animation, heal_amount, heal_target, message):
		super().__init__(name, price, mapletter, has_animation, heal_amount, heal_target, message)

soda = Drink(
	name="soda",
	price=2,
	mapletter="so",
	has_animation=False,
	heal_amount=-10,
	heal_target=("hp"),
	message="The soda was unhealthy for your HP. Don't drink it!",
)
muscle_milk = Drink(
	name="muscle-milk",
	price=3,
	mapletter="mm",
	has_animation=False,
	heal_amount=20,
	heal_target=("hp", "phys strength", "hunger", "dehydration"),
	message="The muscle milk made you stronger.",
)
coffee = Drink(
	name="coffee",
	price=4,
	mapletter="cf",
	has_animation=False,
	heal_amount=15,
	heal_target=("hp", "mental strength", "dehydration"),
	message="The coffee made you more focused.",
)

whey_milk = Drink(
		name="whey-and-milk",
		price=5,
		mapletter="wh",
		has_animation=False,
		heal_amount=35,
		heal_target=("hp", "phys strength", "hunger", "dehydration"),
		message="This protein-rich whey helped your strength.",
)


class Key(Item):
	def __init__(self, name, price, mapletter, has_animation, heal_amount, heal_target, message):
		super().__init__(name, price, mapletter, has_animation, heal_amount, heal_target, message)


bronze_key = Key(
	name="bronze-key",
	price=None,
	mapletter="bk",
	has_animation=True,
	heal_amount=None,
	heal_target=None,
	message="You found the bronze key! You'll use it later...",
)
silver_key = Key(
	name="silver-key",
	price=None,
	mapletter="sk",
	has_animation=True,
	heal_amount=None,
	heal_target=None,
	message="You found the silver key! This will be important later...",
)
gold_key = Key(
	name="gold-key",
	price=None,
	mapletter="gk",
	has_animation=True,
	heal_amount=None,
	heal_target=None,
	message="You found the golden key! This will be very important later...",
)


all_foods = (parmesan_cheese, burger, lasagna, chicken)
all_drinks = (soda, muscle_milk, coffee, whey_milk)
all_keys = (bronze_key, silver_key, gold_key)
all_items = (all_foods, all_drinks, all_keys)
