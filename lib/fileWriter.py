import os
from os import path

def write():

    text = ["00. Put information inside () after finish open terminal and continue",
        "00. You can separate mor informations in single place by [,] without space",
        "00. Format for dates [DDMMYYYY] - !!! DO NOT ADD LINES !!!",
        "00. ",
        "01. Personal:",
        "02.    FirstName__________()",
        "03.    LastName___________()",
        "04.    UserNames__________()",
        "05.    Age________________()",
        "06.    Birthday___________()",
        "07.    Sign of the Zodiac_()",
        "08.    Pet name___________()",
        "09.    Favorite animal____()",
        "10.    Favorite flover____()",
        "11.    Favorite color_____()",
        "12.    Worst animal_______()",
        "13.    Job________________()",
        "14.    Car________________()",
        "15.    State______________()",
        "16.    City_______________()",
        "17.    Street_____________()",
        "18.    House number_______()",
        "19.    Favorite number____()",
        "20.    BornState__________()",
        "21.    BornCity___________()",
        "22.    Phone number_______()",
        "23.    Favorite sport_____()",
        "24.    Important dates____()",
        "25.",
        "26. Partner:",
        "27.    FirstName__________()",
        "28.    LastName___________()",
        "29.    UserNames__________()",
        "30.    Age________________()",
        "31.    Phone number_______()",
        "32.    Job________________()",
        "33.    Birthday___________()",
        "34.    FirstDateData______()",
        "35.    Important dates____()",
        "36.",
        "37. Family:",
        "38.    Dad:",
        "39.        FirstName______()",
        "40.        LastName_______()",
        "41.        Birthday_______()",
        "42.    Mother:",
        "43.        FirstName______()",
        "44.        LastName_______()",
        "45.        Birthday_______()",
        "46.    Sister:	",
        "47.        FirstName______()",
        "48.        LastName_______()",
        "49.        Birthday_______()",
        "50.    Brother:",
        "51.        FirstName______()",
        "52.        LastName_______()",
        "53.        Birthday_______()"]

    os.system('cls')
    print("\033[1;34;40m[1]\033[1;37;40m - Create new file to complete")    
    print("\033[1;32;40mAdd new file name [etc. file.txt]")

    exis = True
    while exis:
        fileName = input("> ")
        if not fileName.endswith(".txt"):
            fileName += ".txt"
        if not path.exists(fileName):
            exis = False
            os.system('cls')
            print("\033[1;34;40m[1]\033[1;37;40m - Create new file to complete")
            print(f"\033[1;34;40mCreated file > \033[1;37;40m{fileName}")
        else:
            print("File alredy exist... please try another name")
    
    file = open(fileName, 'x')
    for x in text:
        file.write(x + "\n") 

