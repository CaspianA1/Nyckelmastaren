# picked_up_items.py

import os

var_dir = os.getcwd() + "/Assets/Global_Vars"


def check_for_duplicate(self, mat):
	current_items = list(open(f"{var_dir}/item_inventory_data.txt").read().strip()).close()

	repeat_items = {}

	for item in current_items:
		repeat_items[item] = 0

	for each_item in current_items:
		for inner_item in current_items:
			if each_item == inner_item:
				repeats[each_item] += 1

	for item_key, item_value in repeats.items():
		repeats[item_key] = math.sqrt(item_value)

	for item_key, item_value in current_items.values():
		if item_value > 3:
			print(f"Wait! You don't have enough space for another {item_key}.")
			print(f"You left the {item_key} on the ground and kept moving.")
			current_items.remove(item_key)

	with open("f{var_dir}/item_inventory_data.txt", "w") as item_file_data:
		for item in current_items:
			item_file_data.write(item)
