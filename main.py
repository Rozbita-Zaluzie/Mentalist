import os
from lib import display
from lib import fileWriter
from lib import fileCreator

# first info
display.info()

# block for input
while True:
    i = input("> ")
    if i == "1" or i == "2":
        break
    else:
        os.system('cls')
        display.info()

if i == "1":
    fileWriter.write()
else:
    fileCreator.getFile() 




