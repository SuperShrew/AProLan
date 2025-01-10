import os

class memory:

  def __init__(self):
    self.vars = {}

class assembly_commands:

  def __init__(self):
    pass
    
  def ADD(self, a, b, var):
    try:
      mem.vars[var.replace("\n", "")] = float(eval(a)) + float(eval(b))
    except:
      print("ERROR: ADD command requires two FLOATS or INTEGERS")
      exit(1)

  def SUB(self, a, b, var):
    try:
      mem.vars[var.replace("\n", "")] = float(eval(a)) - float(eval(b))
    except:
      print("ERROR: SUB command requires two FLOATS or INTEGERS")
      exit(1)

  def MUL(self, a, b, var):
    try:
      mem.vars[var.replace("\n", "")] = float(eval(a)) * float(eval(b))
    except:
      print("ERROR: MUL command requires two FLOATS or INTEGERS")
      exit(1)

  def DIV(self, a, b, var):
    try:
      mem.vars[var.replace("\n", "")] = float(eval(a)) / float(eval(b))
    except:
      print("ERROR: DIV command requires two FLOATS or INTEGERS")
      exit(1)

  def MOD(self, a, b, var):
    try:
      mem.vars[var.replace("\n", "")] = float(eval(a)) % float(eval(b))
    except:
      print("ERROR: MOD command requires two FLOATS or INTEGERS")
      exit(1)

  def PWR(self, a, b, var):
    try:
      mem.vars[var.replace("\n", "")] = float(eval(a)) ** float(eval(b))
    except:
      print("ERROR: PWR command requires two FLOATS or INTEGERS")
      exit(1)

  def OUT(self, string):
    exec("print(" + string + ")")

  def IN(self, var):
    mem.vars[var.replace("\n", "")] = input("> ")

  def SET(self, var, value):
    mem.vars[var] = value.replace("\n", "")

  def CLR(self):
    os.system("clear")
  
mem = memory()
cmd = assembly_commands()
labels = {}

with open("code.txt", "r+") as file:
  current_pos = 0
  for i in file:
    current_pos += len(i)
    i = i.split(" ")
    if i[0][0] == "@":
      labels[i[0].replace("\n", "")] = current_pos
      print(".", end="")
  print()
with open("code.txt", "r+") as file:
  current_pos = 0
  for line in file:
    current_pos = len(line)
    line = line.split(" ")
    if line[0] == "ADD":
      cmd.ADD(line[1], line[2], line[3])
    elif line[0] == "SUB":
      cmd.SUB(line[1], line[2], line[3])
    elif line[0] == "MUL":
      cmd.MUL(line[1], line[2], line[3])
    elif line[0] == "DIV":
      cmd.DIV(line[1], line[2], line[3])
    elif line[0] == "MOD":
      cmd.MOD(line[1], line[2], line[3])
    elif line[0] == "PWR":
      cmd.PWR(line[1], line[2], line[3])
    elif line[0].replace("\n", "") == "CLR":
      cmd.CLR()
    elif line[0] == "OUT":
      cmd.OUT(line[1])
    elif line[0] == "GOTO" and line[2] == "IF":
      if eval(line[3]) and line[1] in labels:
        file.seek(labels[line[1]])
    elif line[0] == "IN":
      cmd.IN(line[1])
