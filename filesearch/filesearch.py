# File Search

"""
Write a script that searches a folder you specify (as well as all its subfolders) on your computer and compiles a list of
all `.jpg` files. The list should contain the complete path of each `.jpg` file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check whether your program is working correctly. Then switch that
small folder name with a bigger folder.

This program should work for any specified folder on your computer.
"""

import os

os.system('cls' if os.name == 'nt' else 'clear')  # just clearing the screen

htext = ' FILE TYPE IDENTIFIER SCRIPT '
stars1 = '*' * ((80-len(htext))//2)
stars2 = '*' * (80-len(stars1) - len(htext))
print(f"\n{'*'*80}")
print(f"{stars1}{htext}{stars2}")
print(f"{'*'*80}")
filext = input(f"\nEnter file extension to find (e.g. '.jpg'): ")
print(f"\nThe search folder may be entered using relative or absolute path.")
folder_in = input(f"Search folder: ")

# f_list = os.listdir(f"{folder_in}")  # just lists all the files in the given search folder

fol_list = []
for folder in os.walk(f"{folder_in}"):
	fol_list.append(folder[0])  # makes a list of every subfolder in the directory

ftypes = []  # list containing all file extensions found
filextlist = []  # list containing all files with requested .ext with their full absolute path
for folder in fol_list:
	for myfile in os.listdir(folder):  # for every file in the particular folder
		if myfile.endswith(filext):
			filextlist.append(os.path.abspath(os.path.join(folder, myfile)))
		if myfile.find('.') not in [-1, 0]:  # -1 means there is no '.', 0 means it's the first character
			for i in range(len(myfile)):
				if myfile[i] == '.':
					myext = myfile[i:]
			if myext not in ftypes:
				ftypes.append(myext)

if len(filextlist) > 0:
	print(f"\nAll {filext} files found in search and subfolders: ")
	for i in filextlist:
		print(f"{i}")
else:
	print(f"\nNo {filext} files found in search and subfolders.")

print(f"\nAll file extensions found in search and subfolders:")
for i in ftypes:
	print(f"{i}")
