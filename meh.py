import configparser
import os
from glob import glob
import git 
 
DIR = ""
PROJECTS = []

def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
  
def init():
	global DIR 
	config = configparser.ConfigParser()
	config.read("./meh.conf")
	DIR = config['CORE']['Directory']

def read_proyects():
	global DIR, PROJECTS
	print(DIR)
	PROJECTS = glob("{}/*/".format(DIR))

def menu():
	global PROJECTS
	while True:
		clear()
		print("+++ Select a project to update +++")
		i = 0
		for p in PROJECTS:
			print("{}. {}".format(i,p.split(os.sep)[-2]))
			i += 1
		print("{}. all".format(i))
		pr = int(input("Pick one: "))
		if(pr > 0 and pr < len(PROJECTS)):
			print("Updating..")
			g = git.cmd.Git(PROJECTS[pr])
			g.pull()
			print("Updated")
		elif(pr == len(PROJECTS)):
			print("Update all..")
			for p in PROJECTS:
				g = git.cmd.Git(p)
				g.pull()
			print("Updated..")
			break
		else:
			print("Out of scope")
			input("Press enter to continue")


init()
read_proyects()
menu()