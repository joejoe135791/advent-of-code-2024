import os
import sys
import termcolor
currentWorkingDirectory = os.getcwd()
textFile = f"{currentWorkingDirectory}/input/input.txt"
inputList1 = []
inputList2 =[]
openInputFile = open(textFile, 'r')
inputFileLines = openInputFile.readlines()
# Solution from teacher, download the text file (saves in /Day1/inputs) and split whenever it detects a space, rinse and repeat (and loop 1k times since there are 1k lines)
i = 0
for i in range(1001):
    currentInputLine = inputFileLines[i]
    cprint(f"current Line: {currentInputLine}", "light_green")
    listReadyInput = currentInputLine.split()
    inputList1 = listReadyInput[:1]
    cprint(f"List 1 ready: {inputList1}", "light_green")
    inputList2 = listReadyInput[:2]
    cprint(f"List 1 ready: {inputList1}", "light_green")

sys.exit("Finished, yipee")