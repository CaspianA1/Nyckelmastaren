# merchants.py

from ..Miscellaneous.formatting import Format
from ..Health_Attack.items import Item
from ..Health_Attack.items import all_foods, all_drinks, all_items
from ..Health_Attack.money_manager import MoneyManager
from maps import Position


class Merchant:
	frm = Format()
	itm = Item()
	pos_obj = Position()
	manager = MoneyManager()
	parmesan_cheese, burger, lasagna, chicken = all_foods
	soda, muscle_milk, coffee, whey_milk = all_drinks

	def __init__(self, name=None, item_tuple=None, mapletter=None, message_1=None, message_2=None, message_3=None):
		self.name = name
		self.item_tuple = item_tuple
		self.mapletter = mapletter
		self.message_1 = message_1
		self.message_2 = message_2
		self.message_3 = message_3

	def check_for_merchant(self, mat):
		pos = self.pos_obj.global_pos("get")
		pos_x, pos_y = pos[0], pos[1]

		for each_merchant in all_merchants:
			if mat[pos_x][pos_y] == each_merchant.mapletter:
				if self.manager.bankruptcy_check() is False:
					self.item_query(each_merchant)
				else:
					self.frm.printfast(f"\nA {each_merchant.name} wants to sell to you, but you don't have any money.\n")
					self.frm.printfast("\nYou shouldn't have used it up so quickly!\n")

	def item_query(self, merchant_obj):
		self.frm.printfast("\n" + merchant_obj.message_1 + "\n")

		for each_item in merchant_obj.item_tuple:
			self.frm.printfast("\n- " + each_item.name.capitalize())

		self.frm.printfast("\n\nWhich item do you want?\n")
		self.frm.printfast("\nRemember, nothing is an option too.\n")
		while True:
			buy_item = input("\x1b[5m-> \x1b[25m")
			buy_item = self.frm.frm_str(buy_item)

			for each_item in merchant_obj.item_tuple:
				if each_item.name in buy_item:
					self.itm.add_to_inventory(each_item)
					self.manager.subtract_money(each_item.price)
					self.manager.print_money()
					self.frm.printfast("\n" + merchant_obj.message_2 + "\n")
					return
				elif "no" in buy_item:
					self.frm.printfast("\n" + merchant_obj.message_3 + "\n")
					return
				else:
					continue


gubbe = Merchant(
"gubbe",
(Merchant.soda, Merchant.muscle_milk, Merchant.coffee),
 "gu",
 "I am Gubbe. I have some good stuff if you want some:",
 "Thank you for buying my stuff!",
 "Why didn't you buy anything?"
 )

nisse = Merchant(
"nisse",
(Merchant.parmesan_cheese, Merchant.burger, Merchant.lasagna),
"ni",
"I am Nisse. Are you hungry? Look no further:",
"You are a generous young person! Thank you.",
"Please, buy something next time..."
)


tomte = Merchant(
"tomte",
(Merchant.parmesan_cheese, Merchant.lasagna, Merchant.whey_milk),
"to",
"I am Tomte! What would you like to buy?",
"I hope you like your food!",
"I guess I'll see you next time then..."
)

all_merchants = (gubbe, nisse, tomte)
