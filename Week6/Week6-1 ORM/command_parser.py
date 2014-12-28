class CommandParser():
	def __init__(self):
		self.__commands = {}
		self.__descriptions = {}

	def add_command(self, command, finction, description):
		self.__commands[command] = function
		self.descriptions[command] = description

	def sexecute(self, input):
		input = input.split(" ")
		command = input[0]
		arguments = input[1:]
