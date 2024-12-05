import os
import sys
from termcolor import cprint
os.system('color')

# currentWorkingDirectory = os.getcwd()
# cprint(f"CWD: {currentWorkingDirectory}", "light_green")
# currentCorrectDirectory = f"{currentWorkingDirectory}/Day1"
textFile = f"C:/Users/jandino1921/Downloads/other/advent-of-code-2024/Day1/inputs/input.txt"
cprint(f"text file: {textFile}", "light_green")
inputList1 = []
inputList2 =[]
openInputFile = open(textFile, 'r')
inputFileLines = openInputFile.readlines()
# Solution from teacher, download the text file (saves in /Day1/inputs) and split whenever it detects a space, rinse and repeat (and loop 1k times since there are 1k lines)
i = 0
for i in range(1000):
    currentInputLine = inputFileLines[i]
    cprint(f"current Line: {currentInputLine}", "light_green")
    listReadyInput = currentInputLine.split()
    listInput1 = listReadyInput[:1]
    cprint(f"List 1 ready: {listInput1}", "light_green")
    listInput2 = listReadyInput[1:]
    cprint(f"List 2 ready: {listInput2}", "light_green")
    inputList1.append(listInput1)
    cprint(inputList1, "blue")
    inputList1.append(listInput2)
    cprint(inputList2, "red")

inputList1.sort()
cprint(inputList1, "blue")

inputList2.sort()
cprint(inputList2, "red")

for z in range(500):
    pass
input("Press Enter to close...")
sys.exit("Finished, yipee")