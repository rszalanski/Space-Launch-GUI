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
	master = tk.Tk(className="\\Upcoming Space Launch List")
	master.configure(bg=darkblue)
	# Create title box
	titleBox = tk.Frame(master, bg=darkblue, relief=RAISED, borderwidth=2, height=5)
	titleBox.pack(side=TOP, fill=BOTH, expand=False)
	titleTxt = tk.Label(titleBox, text='Upcoming Space Launches', foreground='white', bg=darkblue)
	titleTxt.pack()
	
	
	# Create box containing upcoming launch info
	launchBox = tk.Frame(master, bg='cyan', relief=SUNKEN, borderwidth=3, width=500, height=500)
	launchBox.pack(fill=BOTH, expand=True, padx=10, pady=10)



# Main function to be executed
def main():
	global master
	refreshList()
	master.mainloop()
	



main()