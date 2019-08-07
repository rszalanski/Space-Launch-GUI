import tkinter as tk
from tkinter import constants
import requests



main()



# Main function to be executed
def main():
	refreshList()



# Function to refresh the window by closing and re-opening it
def refreshList():
	# Attempt to close any already opened window
	try:
		master.destroy()
	except:
		pass
		
		
	# Create main window
	master = tk.Tk(classname="Upcoming Space Launch List")
	