class CashDesk(object):
	def __init__(self):
		self.money = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
	def take_money(self, dict):
		for key in dict:
			self.money[key] += dict[key]
	def total(self):
		total = 0
		for key, value in self.money.items():
			total += value * key
		return total

my_cash_desk = CashDesk()
my_cash_desk.take_money({1:2, 50:1, 20:1})
print (my_cash_desk.total())

