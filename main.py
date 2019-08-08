import tkinter as tk
from tkinter.constants import *
import requests



# Funtion to get time of a given launch number from launch list
def getTime(launchList, launchNum):
	# Get information for individual launch
	launch = launchList[launchNum]
	# Get time from launch information
	return launch.get('net')



# Funtion to get name of given launch number from launch list
def getName(launchList, launchNum):
	# Get information for individual launch
	launch = launchList[launchNum]
	# Get name from launch information
	return launch.get('name')



# Function to add infromation from API
def populateList():
	global launchBox
	# Number of launches to show
	numLaunches = 20
	
	
	# Create left and right columns for populating list
	leftBox = tk.Frame(launchBox, bg='cyan', relief=RAISED, borderwidth=2, width=150)
	leftBox.pack(side=LEFT, fill=Y, expand=False)
	rightBox = tk.Frame(launchBox, bg='cyan', relief=RAISED, borderwidth=2, width=350)
	rightBox.pack(side=RIGHT, fill=BOTH, expand=True)
	rightTopBox = tk.Frame(rightBox, bg='cyan')
	rightTopBox.pack(side=TOP, fill=X, expand=False)
	
	
	# Initialize lists to be used for holding launch information
	missionNameBox = []
	missionTimeBox = []
	missionName    = []
	missionTime    = []
	launchList     = []
	# Get launch information list
	response = requests.get('https://launchlibrary.net/1.4/launch?next=' + str(numLaunches))
	jsonResponse = response.json()
	launchList = jsonResponse.get('launches')
	# Populate GUI with launch information
	for i in range(numLaunches):
		# Create boxes to hold launch information
		missionNameBox.append(tk.Frame(rightTopBox, bg='cyan', relief=RAISED, borderwidth=2, height=5))
		missionNameBox[i].pack(fill=X, expand=True)
		missionTimeBox.append(tk.Frame(leftBox, bg='cyan', relief=RAISED, borderwidth=2, height=5, width=150))
		missionTimeBox[i].pack(fill=X, expand=False)
		# Fill created boxes with launch information
		missionName.append(tk.Label(missionNameBox[i], bg='cyan', foreground='black', text=getName(launchList, i)))
		missionName[i].pack()
		missionTime.append(tk.Label(missionTimeBox[i], bg='cyan', foreground='black', text=getTime(launchList, i)))
		missionTime[i].pack()
		
		



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