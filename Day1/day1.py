import os
import sys
from termcolor import cprint
from dotenv import load_dotenv
load_dotenv()
os.system('color')

# currentWorkingDirectory = os.getcwd()
# cprint(f"CWD: {currentWorkingDirectory}", "light_green")
# currentCorrectDirectory = f"{currentWorkingDirectory}/Day1"
textFile = os.getenv("inputTXTPath")
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
    inputList2.append(listInput2)
    cprint(inputList2, "red")

inputList1.sort()
cprint(inputList1, "blue")

inputList2.sort()
cprint(inputList2, "red")

finalNumber = 0
for z in range(1000):
    sortedInputLine1 = str(inputList1[z])
    sortedInputStripped1 = sortedInputLine1.strip("[']")
    cprint(f"Sorted line 1: {sortedInputStripped1}", "light_green")
    sortedInputLine2 = str(inputList2[z])
    sortedInputStripped2 = sortedInputLine2.strip("[']")
    cprint(f"Sorted line 2: {sortedInputStripped2}", "light_green")
    if float(sortedInputStripped1) <= float(sortedInputStripped2):
        sortedInputDifference = float(sortedInputStripped2)-float(sortedInputStripped1)
    elif float(sortedInputStripped1) > float(sortedInputStripped2):
        sortedInputDifference = float(sortedInputStripped1)-float(sortedInputStripped2)
    cprint(f"Difference: {sortedInputDifference}", "light_green")
    finalNumber += abs(sortedInputDifference)
    cprint(f"current total: {finalNumber}", "light_green")
    

cprint(f"Sorted list 1: {inputList1}", "magenta")
cprint(f"Sorted list 2: {inputList2}", "red")
cprint(f"Final Number: {finalNumber}")
input("Press Enter to close...")
sys.exit("Finished, yipee")