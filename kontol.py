#coding "UTF 8"
#python 2.7 ++
#by Mr.w0n6ed4n
#tools installer AOC

from os import system
from time import sleep
from subprocess import call

h = "\033[92m"
k = "\033[93m"
u = "\033[95m"
p = "\033[97m"
r = "\033[0m"
bm = "\033[96m"
b = "\033[94m"
m = "\033[91m"

def lilo_kontol():
		call("clear", shell = True)
		print "\nsilahkan pilih toolsnya\n"
		print m+"["+p+"1"+m+"]"+h+".tools hack fb by R00tm3ex\n"
		print "yang lain nyusul yah :v\n"
		kirana = raw_input("pilih cuk:v: ")
		if kirana == "1":
			system("apt-get install git python python2")
			sleep(1)
			system("git clone https://github.com/rootM3eX/FbB")
			sleep(0.5)
			system("cd FbB")
			print "please wait running tools.."
			sleep(1)
			system("python2 bb.py")
		else:
			call("clear", shell = True)
			print "\nharap masukam pilihan\n"
			sleep(2)
			lilo_kontol()
			
if __name__ == "__main__":
	lilo_kontol()
		
    