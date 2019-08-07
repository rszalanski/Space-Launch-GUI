import tkinter as tk
from tkinter.constants import *
import requests



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
	master = tk.Tk(className="Upcoming Space Launch List")
	master.configure(bg=darkblue)
	# Create title box
	titleBox = tk.Frame(master, bg=darkblue)
	titleBox.pack(side=TOP, fill=BOTH)
	titleTxt = tk.Label(titleBox, text='Upcoming Space Launches', foreground='white', bg=darkblue)
	titleTxt.pack()



# Main function to be executed
def main():
	global master
	refreshList()
	master.mainloop()
	



main()