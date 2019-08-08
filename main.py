import tkinter as tk
from tkinter.constants import *
import requests



# Function to add infromation from API
def populateList():
	global launchBox
	
	
	# Create left and right columns for populating list
	leftBox = tk.Frame(launchBox, bg='cyan', relief=FLAT, borderwidth=2, width=150)
	leftBox.pack(side=LEFT, fill=BOTH, expand=False)
	rightBox = tk.Frame(launchBox, bg='cyan', relief=FLAT, borderwidth=2)
	rightBox.pack(side=RIGHT, fill=BOTH, expand=False)
	
	
	# Populate list with launch information



# Function to call to exit the program
def exitProgram():
	global master
	# Close master window
	master.destroy()



# Function to refresh the window by closing and re-opening it
def refreshList():
	# Define window colors
	darkblue = '#000064'


	# Specify that 'master' is a global variable
	global master


	# Attempt to close any already opened window
	try:
		master.destroy()
	except:
		pass
		
		
	# Create main window
	master = tk.Tk(className="\\Upcoming Space Launch List")
	master.configure(bg=darkblue)
	# Create title box
	titleBox = tk.Frame(master, bg=darkblue, relief=RAISED, borderwidth=2, height=5)
	titleBox.pack(side=TOP, fill=BOTH, expand=False)
	titleTxt = tk.Label(titleBox, text='Upcoming Space Launches', foreground='white', bg=darkblue)
	titleTxt.pack()
	
	
	# Create box containing upcoming launch info
	global launchBox
	launchBox = tk.Frame(master, bg='cyan', relief=SUNKEN, borderwidth=3, width=500, height=500)
	launchBox.pack(fill=BOTH, expand=True, padx=10, pady=10)
	
	
	# Create list of upcoming launches
	populateList()
	
	
	# Create 'EXIT' and 'REFRESH' buttons
	buttonBox = tk.Frame(master, bg=darkblue, relief=RAISED, borderwidth=2, height=50)
	buttonBox.pack(side=BOTTOM, fill=BOTH, expand=False)
	exitButton = tk.Button(buttonBox, bg='red', foreground='white', text='EXIT', command=exitProgram)
	exitButton.pack(side=LEFT, fill=BOTH, expand=True)
	refrButton = tk.Button(buttonBox, bg='green', foreground='white', text='REFRESH', command=refreshList)
	refrButton.pack(side=RIGHT, fill=BOTH, expand=True)



# Main function to be executed
def main():
	global master
	refreshList()
	master.mainloop()



main()