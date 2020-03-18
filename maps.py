# maps.py

import os, time, random
from Assets.Miscellaneous.formatting import Format
from Assets.Global_Vars.maps_data import (
	h_prmat_dict,
	h_plmat_dict,
	v_prmat_dict,
	v_prmat_tuple_rev,
	v_plmat_dict,
)
from Assets.Visuals.neo_animation_system import show_graphic

# num_rows = 10
# num_cols = 10

# ADD HORIZONTAL MAPS

# ADD A GRAVEYARD AT THE BEGINNING ENTERING THE CASTLE

# ADD THE MAIN CHARACTER LEAVING THEIR HOME FIRST

class Position:
	var_dir = os.getcwd() + "/Assets/Global_Vars/"
	frm = Format()
	def get_rows_cols(self):
		which_prmat = ""
		with open(f"{self.var_dir}curr_pr_mat.txt", "r") as prmat_file:
			which_prmat = prmat_file.read().strip()

		if which_prmat == "prmat0":
			return (10, 10)
		elif which_prmat == "home_hprmat":
			# return (49, 19)
			# return (19, 50)
			# return (19, 50)
			# 49 wide, 19 down (counting from zero)
			return (10, 25)
		elif which_prmat == "hprmat_plaza":
			return (16, 40)
		elif which_prmat == "hprmat05":
			return (25, 30)
		elif which_prmat == "hprmat075":
			# return (14, 77)  # this one
			# return (15, 77)
			# return (77, 14)
			return (13, 76)
		elif which_prmat == "prmat1":
			return (10, 10)
		elif which_prmat == "prmat2":
			# return (14, 14)
			# return (15, 40)
			# return (9, 13)
			 #return (13, 10)
			 # return (10, 13)
			return (13, 42)
		elif which_prmat == "prmat3":  # doesn't exist yet
			pass
		elif which_prmat == "prmat_bbfl":
			return (4, 5)

	def global_pos(self, mode, **input_vars):
		var_file = self.var_dir + "savedvariables.txt"

		if mode == "get":
			return_list = []
			with open(var_file, "r") as var_file_data:
				for line in var_file_data.readlines():
					return_list.append(line.strip("\n"))

			for index, var in enumerate(return_list):
				if index in (0, 1):
					return_list[index] = int(var)
			return return_list

		elif mode == "set":
			current_vars = self.global_pos("get")
			for var_key, var_value in input_vars.items():
				if var_key == "pos_x":
					current_vars[0] = var_value
				elif var_key == "pos_y":
					current_vars[1] = var_value
				elif var_key == "currentenemy":
					current_vars[2] = var_value

			writable_vars = "".join(str(var) + "\n" for var in current_vars)
			writable_vars = writable_vars[0:-1]

			with open(var_file, "w") as var_file_data:
				var_file_data.write(writable_vars)


	def get_mat(self, prmat_name):
		if prmat_name == "prmat":
			cm = open(f"{self.var_dir}curr_pr_mat.txt", "r")
			curr_mat_name = cm.readline().strip()
			for real_mat_name in v_prmat_dict.keys():
				if curr_mat_name == real_mat_name:
					cm.close()
					return v_prmat_dict[real_mat_name]
			for real_mat_name in h_prmat_dict.keys():
				if curr_mat_name == real_mat_name:
					cm.close()
					return h_prmat_dict[real_mat_name]
		elif prmat_name == "plmat":
			cm = open(f"{self.var_dir}curr_pl_mat.txt", "r")
			curr_mat_name = cm.readline().strip()
			for real_mat_name in v_plmat_dict.keys():
				if curr_mat_name == real_mat_name:
					return v_plmat_dict[real_mat_name]

			for real_mat_name in h_plmat_dict.keys():
				if curr_mat_name == real_mat_name:
					return h_plmat_dict[real_mat_name]
		else:
			return "Specify a mode for the type of matrix to get in global_map, in maps.py."


	def map_change(self):
		prmat = self.get_mat("prmat")
		pos = self.global_pos("get")
		pos_x, pos_y = pos[0], pos[1]

		for stairwell in all_stairs:
			if prmat[pos_x][pos_y] == stairwell.mapletter:
				self.floor_change_prompt(stairwell)


	def floor_change_prompt(self, stairwell):
		if stairwell.is_vertical:
			if stairwell.is_going_up:
				self.frm.printfast("\nYou face a set of cobblestone steps.\n")
				self.frm.printfast("Ascend stairs?\n")
			else:
				self.frm.printfast(f"\nA dark spiral leads down to floor {stairwell.conn_floor_num}.\n")
				self.frm.printfast("Descend stairs?\n")
		else:
			# print("path detected")
			self.frm.printfast(stairwell.messages[0] + "\n")
			self.frm.printfast("Open the door?\n")

		while True:
			travel_prompt = input("\x1b[5m->\x1b[25m ")
			travel_prompt = self.frm.frm_str(travel_prompt)

			if "y" in travel_prompt or "k" in travel_prompt:
				with open(f"{self.var_dir}curr_pr_mat.txt", "w") as prmat_file:
					prmat_file.write(stairwell.connected_prmat)
				with open(f"{self.var_dir}curr_pl_mat.txt", "w") as plmat_file:
					plmat_file.write(stairwell.connected_plmat)

				if stairwell.new_x is not None:
					self.global_pos("set", pos_x = stairwell.new_x)
				if stairwell.new_y is not None:
					self.global_pos("set", pos_y = stairwell.new_y)

				if stairwell.is_vertical:
					if stairwell.is_going_up:
						self.frm.printfast("\nYou moved to the next floor.\n")
					else:
						self.frm.printfast("\nYou went down a floor.\n")
				else:
					self.frm.printfast(stairwell.messages[1] + "\n")
					if stairwell.connected_prmat == "home_hprmat":
						time.sleep(0.5)
						show_graphic("house frame")
						break
				time.sleep(1)
				rand_graphic = random.choice(("transition 1", "transition 2"))
				show_graphic(rand_graphic)
				break

			elif "n" in travel_prompt:
				if stairwell.is_vertical:
					self.frm.printfast("\nYou decided to stay on this floor.\n")
				else:
					self.frm.printfast(stairwell.messages[2] + "\n")
				break

			else:
				continue

class Stairs:
	def __init__(self,
		mapletter,
		is_vertical,
		is_going_up,
		conn_floor_num,
		connected_prmat,
		connected_plmat,
		messages = (None),
		new_x = None,
		new_y = None
		):

		self.mapletter = mapletter
		self.is_vertical = is_vertical
		self.is_going_up = is_going_up
		self.conn_floor_num = conn_floor_num
		self.connected_prmat = connected_prmat
		self.connected_plmat = connected_plmat
		self.messages = messages
		self.new_x = new_x
		self.new_y = new_y


usta0_1 = Stairs(
	mapletter = "usta0_1",
	is_vertical = True,
	is_going_up = True,
	conn_floor_num = 1,
	connected_prmat = "prmat1",
	connected_plmat = "plmat1",
	messages = (None),
	new_x = None,  # 9, 13
	new_y = None
	)

usta1_2 = Stairs(
	mapletter = "usta1_2",
	is_vertical = True,
	is_going_up = True,
	conn_floor_num = 2,
	connected_prmat = "prmat2",
	connected_plmat = "plmat2",
	messages = (None),
	new_x = 11,#9
	new_y = 13  # I think. Not super sure
	)

dsta1_0 = Stairs(
	mapletter = "dsta1_0",
	is_vertical = True,
	is_going_up = False,
	conn_floor_num = 0,
	connected_prmat = "prmat0",
	connected_plmat = "plmat0",
	messages = (None),
	new_x = None,
	new_y = None
	)

dsta2_1 = Stairs(
	mapletter = "dsta2_1",
	is_vertical = True,
	is_going_up = False,
	conn_floor_num = 1,
	connected_prmat = "prmat1",
	connected_plmat = "plmat1",
	messages = (None),
	new_x = 3,
	new_y = 1
	)

##########

acr0_05 = Stairs(
	mapletter = "acr0_0.5",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "hprmat05",
	connected_plmat = "hplmat05",
	messages = (
	"\nA door leads outside. It's cold.",
	"\nYou went outside.\n",
	"\nYou stayed inside.\n"),
	new_x = 1,
	new_y = 16

)

acr05_0 = Stairs(
	mapletter = "acr0.5_0",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "prmat0",
	connected_plmat = "plmat0",
	messages = (
	"\nYou face a tall wooden door.\nUpon entering, you will explore a mighty castle.",
	"\nYou entered the spiring citadel. Keep your sword close in there.\n",
	"\nYou stayed outside in the blistering hail.\n"
	),
	new_x = 8,
	new_y = 5
	# this is shifted a bit on purpose.
)

acr05_075 = Stairs(
	mapletter = "acr0.5_0.75",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "hprmat075",
	connected_plmat = "hplmat075",
	messages = (
	"\nYou see the field that you started in.\nIt's like a big maze.",
	"\nYou went into the big field. Don't get lost in there!\n",
	"\nYou stayed in the garden.\n",
	),
	new_x = 0,
	new_y = 36

)

acr075_05 = Stairs(
	mapletter = "acr0.75_0.5",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "hprmat05",
	connected_plmat = "hplmat05",
	messages = (
	"\nLooking far north, you see a garden.\n",
	"\nYou went to explore the garden.\n",
	"\nYou stayed in the field.\n",
	),
	new_x = 13,
	new_y = 0

)

acr075_home = Stairs(
	mapletter = "acr0.75_home",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "home_hprmat",
	connected_plmat = "home_hplmat",
	messages = (
	"\nYou have returned to where began your journey.\n",
	"\nYou returned to your humble abode.\n",
	"\nYou stayed in the field outside your home.\n"),
	new_x = 5,
	new_y = 20
	# new_x = 9,
	# new_y = 49


)

acrhome_075 = Stairs(
	mapletter = "acrhome_0.75",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "hprmat075",
	connected_plmat = "hplmat075",
	messages = (
	"\nOutside your small hut, a world lies unexplored.\nDangerous foes, including the dark wizard,\nare waiting for you.\n",
	"\nA realm of beasts awaits you.\nDid you remember your rusty sword? Check by entering 'see inventory'!\n",
	"\nYou stayed safe in your house. Remember, your ancestors are depending on you...\n"
	),
	# the following two numbers are incorrect.  # actually, maybe not.
	new_x = 12,
	new_y = 5
)

acr075_plaza = Stairs(
	mapletter = "acr0.75_plaza",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "hprmat_plaza",
	connected_plmat = "hplmat_plaza",
	messages = ("\nYou remember ancient stories of a sacred key lying here.\nUsing this key and others, you may enter Salazar's den.\n",
	"\nYou ventured into the ancient plaza.\n",
	"\nYou stayed in the tall, grassy field.\n"),
	new_x = 8,
	new_y = 0
)

acrplaza_075 = Stairs(
	mapletter = "acrplaza_0.75",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "hprmat075",
	connected_plmat = "hplmat075",
	messages = ("\nFar, far away you see the tall grassy field that you had left before.\n",
	"\nYou found your way back to the field.\n",
	"\nYou stayed in the abandoned plaza.\n"),
	new_x = 11,
	new_y = 54
)

acr2_bb = Stairs(
	mapletter = "acr2_bb",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "prmat_bbfl",
	connected_plmat = "plmat_bbfl",
	messages = ("\nThe room of the mighty bucky ball has been discovered!\nThe bucky ball is thousands of times stronger than the wimpy plasma sword.\n",
	"\nYou went to get the forgotten relic, Buckminsterfullerene!\n",
	"\nCome on, don't you want the strongest item in the game?\n"),
	new_x = 2,
	new_y = 2

)

acrbb_2 = Stairs(
	mapletter = "acrbb_2",
	is_vertical = False,
	is_going_up = False,
	conn_floor_num = None,
	connected_prmat = "prmat2",
	connected_plmat = "prmat2",
	messages = ("\nYou are now ready to face the challenge of Salazar. Good luck!\n",
	"\nYou went on to slay the wizard, once and for all!\n",
	"\nYou stayed in the bucky-ball's lair.\n"),
	new_x = 5,
	new_y = 0


)


# add the home map

all_stairs = (
usta0_1, usta1_2, dsta1_0, dsta2_1,
acr0_05, acr05_0, acr05_075, acr075_05,
acr075_home, acrhome_075, acr075_plaza, acrplaza_075, acr2_bb, acrbb_2)


"""
# - empty wall
h - hallway

r - rusty sword
g - gold sword
d - diamond sword
p - plasma sword

t - troll
go - goblin
o - ogre
hu - huldra
dr - draugr
m - moloch
w - wizard
"""

terrain = ["#", "hallway"]

"""
cmat characters:
# - empty wall
h - hallway

r - rusty sword
g - gold sword
d - diamond sword
p - plasma sword

t - troll
go - goblin
o - ogre
hu - huldra
dr - draugr
m - moloch
w - wizard
"""
