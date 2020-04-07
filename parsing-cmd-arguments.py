#-------------------
# Author: Iman Irajian
# 		  iman.irajian@gmail.com
# Program: Saving n x n Multiplication table in a file,
#          accepting arguments n, file_name (f) and verbose (v).
# Date: Wednesday, April 08, 2020
# Sample running code:
# python parsing-cmd-arguments.py -n 3 --file_name="data.txt" -v
#-------------------

#-------------------
# Required modules
import sys, getopt
#-------------------

#-------------------
# Main program
def main():
	with open(file_name, "w") as f:
		if need_save_comments:
			f.write(str(n) + " x " + str(n) + " Multiplication table" + "\n")
		for r in range(1, n+1):
			for c in range(1, n+1):
				f.write(str(r*c))
				f.write("\t\t")
			f.write("\n")
#-------------------

#-------------------
# Parsing arguments
args_values = getopt.getopt(sys.argv[1:], "n:f:v", ["file_name=", "verbose"])[0]

n = 5
file_name = ""
need_save_comments = False

for arg, value in args_values:
	arg = arg.lower().replace("-", "").replace("_", "")

	if arg=="n":
		n = int(value)
	if arg in ["f", "filename"]:
		file_name = value.strip()
	if arg in ["v", "verbose"]:
		need_save_comments = True
#-------------------

#-------------------
# Calling Main program
if __name__ == "__main__":
	if file_name != "":
		main()
#-------------------