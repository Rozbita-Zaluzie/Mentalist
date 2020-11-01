import os
from os import path
import time
from lib import display

# get file name
def getFile():
    os.system('cls')
    print("\033[1;34;40m[2]\033[1;37;40m - Load complete file")
    print("\033[1;32;40mWrite file name [etc. file.txt]")

    while True:
        fileName = input("> ")
        if not fileName.endswith(".txt"):
            fileName += ".txt"
        if path.exists(fileName):
            break
        else:
            print("Invalid file.... please try another name")

    os.system('cls')
    print("\033[1;34;40m[2]\033[1;37;40m - Load complete file")
    print(f"\033[1;34;40mLoading file > \033[1;37;40m{fileName}")
    print('\033[1;32;40mWrite new word list name [etc. file.txt]')
    while True:
        nFileName = input("> ")
        if not nFileName.endswith(".txt"):
            nFileName += ".txt"
        if not path.exists(nFileName):
            break
        else:
            print("File alredy exist... please try another name")
    display.progress(fileName, nFileName, 0)
    time.sleep(1)
    
    create(fileName, nFileName)

def create(fName, nfName):
    newFile = open(fName, "r")
    try:
        names = []
        ages = []
        numbers = []
        favorite = []
        dates = []
        places = []
        
        for line in newFile:
            
            num = int(line[:2])
            
            if num > 1 and num <= 4:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    names.append(x)
            elif num == 5:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    ages.append(x)
            elif num == 6:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x)
            elif num >= 7 and num < 15:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    favorite.append(x)
            elif num >= 15 and num <= 17:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    places.append(x)
            elif num == 18 or num == 19:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    ages.append(x)
            elif num == 20 or num == 21:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    places.append(x) 
            elif num == 22:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    numbers.append(x)
            elif num == 23:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    favorite.append(x)
            elif num == 24:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x)
            elif num >= 27 and num < 30:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    names.append(x)
            elif num == 30:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    ages.append(x)
            elif num == 31:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    numbers.append(x)
            elif num == 32:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    favorite.append(x)
            elif num >= 33 and num <= 35:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x) 
            elif num == 39 or num == 40:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    names.append(x)
            elif num == 41:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x)
            elif num == 43 or num == 44:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    names.append(x)
            elif num == 45:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x)
            elif num == 47 or num == 48:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    names.append(x)
            elif num == 49:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x)
            elif num == 51 or num == 52:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    names.append(x)
            elif num == 53:
                for x in line[line.find('(')+1: line.find(')')].split(","):
                    dates.append(x)    
    except:
        display.progress(fName, nfName, 3)
        time.sleep(2)
    else:
        display.progress(fName, nfName, 1)
        time.sleep(1)
    
    # dates format
    try:
        newDates = []
        for date in dates:
            days = date[:2]
            shDays = days
            if (days.startswith("0")):
                shDays = days[1:]
            months = date[2:4]
            shMonths = months
            if (months.startswith("0")):
                shMonths = months[1:]
            years = date[4:]
            shYear = years[2:]
            if (years.endswith("00")):
                shYear = years[:3]
            
            v0 = years
            v1 = shMonths
            v2 = shMonths + years
            v3 = shDays + shMonths + shDays
            v4 = days + months + years
            v5 = shDays + shMonths + shYear
            v6 = days + months
            v7 = shDays + shMonths
            
            newDates.append(date)
            newDates.append(v0)
            newDates.append(v1)
            newDates.append(v2)
            newDates.append(v3)
            newDates.append(v4)
            newDates.append(v5)
            newDates.append(v6)
            newDates.append(v7)
    except:
        display.progress(fName, nfName, 4)
        time.sleep(2)
    else:
        display.progress(fName, nfName, 2)
        time.sleep(1)

    try:
        file = open(nfName, "x")

        while (names.count('')): 
            names.remove('') 

        while (ages.count('')): 
            ages.remove('') 

        while (newDates.count('')): 
            newDates.remove('') 

        while (favorite.count('')): 
            favorite.remove('') 

        while (places.count('')): 
            places.remove('') 

        while (numbers.count('')): 
            numbers.remove('') 

        for x in names:
            for xa in ages:
                file.write(x + xa)
                file.write("\n")
            for xb in favorite:
                file.write(x + xb)
                file.write("\n")
            for xc in newDates:
                file.write(x + xc)
                file.write("\n")
            for xd in places:
                file.write(x + xd)
                file.write("\n")    
            
        for x in favorite:
            for xa in ages:
                file.write(x + xa)
                file.write("\n")
            for xb in names:
                file.write(x + xb)
                file.write("\n")
            for xc in newDates:
                file.write(x + xc)
                file.write("\n")
            for xd in places:
                file.write(x + xd)
                file.write("\n")

        for x in places:
            for xa in ages:
                file.write(x + xa)
                file.write("\n")
            for xb in favorite:
                file.write(x + xb)
                file.write("\n")
            for xc in newDates:
                file.write(x + xc)
                file.write("\n")
            for xd in names:
                file.write(x + xd)
                file.write("\n")

        for x in names:
            file.write(x)
            file.write("\n")

        for x in favorite:
            file.write(x)
            file.write("\n")

        for x in numbers:
            file.write(x)
            file.write("\n")

        for x in newDates:
            file.write(x)
            file.write("\n")

        for x in places:
            file.write(x)
            file.write("\n")    

    except:
        display.progress(fName, nfName, 5)
    else:
        display.progress(fName, nfName, 6)
    