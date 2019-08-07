import tkinter as tk
from tkinter import constants
import requests



main()



# Main function to be executed
def main():
	refreshList()



# Function to refresh the window by closing and re-opening it
def refreshList():
	# Define window colors
	darkblue = '#000064'


	# Attempt to close any already opened window
	try:
		master.destroy()
	except:
		pass
		
		
	# Create main window
	master = tk.Tk(classname="Upcoming Space Launch List")
	master.configure(bg=darkblue)
	# Create title box
	titleBox = tk.Frame(master)
	titleBox.pack(side=TOP, fill=BOTH)
	titleTxt = tk.Label(titleBox, text='Upcoming Space Launches' ,foreground='white')