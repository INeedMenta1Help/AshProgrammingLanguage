from sys import *

tokens = []
classes = []
# Classes
# Functions
class func:
	def __init__(self, arg):
		self.arg = arg


class println(func):
	def __init__(self, arg):
		func.__init__(self, arg)

	def run(self):
		print(self.arg)



def open_file(filename):
	data = open(filename, "r").read()
	return data


def lex(filecontents):
	filecontents = list(filecontents)
	#print(filecontents)
	tok = ""

	state = 0
	string = ""

	for char in filecontents:
		tok += char
		if tok == " " and state == 0:
			tok = ""
		elif tok == " " and varstate = 1:
			tokens.append(["variable", tok])
		elif tok == "\n" and state == 0:
			tok = ""
		elif tok == "println":
			#print("Found Println")
			tokens.append(["func", tok])
			tok = ""
		elif tok == "\"":
			if state == 0:
				state = 1
			elif state == 1:
				#print("Found A String: ", string)
				tokens.append(["string", string])
				state = 0
				tok = ""
				string = ""
		elif tok == "VAR":
			tok = ""
			varstate = 1
		elif state == 1:
			string += char
			tok = ""
		elif varstate == 1:
			variable += tok
			tok = ""

	# for i in tokens:
	# 	print(i[0], i[1])

def parse():
	i = 0
	while i < len(tokens):
		if tokens[i][0] == "func":
			if tokens[i][1] == "println":
				classes.append(println(tokens[i+1][1]))
				i += 1

		i += 1

def exe():
	#print(classes)
	for i in range(0, len(classes)):
		classes[i].run()


def run():
	data = open_file(argv[1])
	lex(data)
	parse()
	exe()

run()