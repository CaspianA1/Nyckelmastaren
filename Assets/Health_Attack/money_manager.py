# money_manager.py

import os
from ..Miscellaneous.formatting import Format


class MoneyManager:
	cwd = os.getcwd()
	frm = Format()
	def print_money(self):
		with open(f"{self.cwd}/Assets/Global_Vars/money.txt", "r") as money_file:
			amt_money = int(money_file.read())
			self.frm.printfast(f"\nYou have {amt_money} coins left.\n")


	def subtract_money(self, subtr_amt):
		current_amount = 0
		with open(f"{self.cwd}/Assets/Global_Vars/money.txt", "r") as money_file:
			current_amount = int(money_file.read())

		new_amount = current_amount - subtr_amt
		if new_amount <= 0:
			new_amount += abs(new_amount)

		with open(f"{self.cwd}/Assets/Global_Vars/money.txt", "w") as money_file:
			money_file.write(str(new_amount))

			# add a zero-money checker.

	def bankruptcy_check(self):
		with open(f"{self.cwd}/Assets/Global_Vars/money.txt", "r") as money_file:
			current_amount = int(money_file.read())
			if current_amount <= 0:
				return True
			else:
				return False
