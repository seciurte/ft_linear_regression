import matplotlib.pyplot as plt
import pandas
import sys

def	main() :
	# print (data)
	while True :
		line = input
		(
			"""	Commands available :
				set-data [new data set]: set the data for training to [new data set].
				show: shows the dataset.
				exit: exits the program.
				help: show this message.
			"""
		)
		if line == "exit" :
			break
		elif line == "show" :
			plt.plot(data["km"], data["price"], "ro")
			plt.show()

if __name__ == '__main__' :
	main()