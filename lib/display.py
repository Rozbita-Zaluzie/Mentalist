import os

# write main info
def info():
    os.system('cls')
    os.system('color 0')
    print("\033[1;34;40m[1]\033[1;37;40m - Create new file to complete")
    print("\033[1;34;40m[2]\033[1;37;40m - Load complete file")

def progress(readF, createF, mode):
    os.system('cls')
    print("\033[1;34;40m[2]\033[1;37;40m - Load complete file")
    print(f"\033[1;34;40mLoading file > \033[1;37;40m{readF}")
    print(f'\033[1;34;40mWordlist name > \033[1;37;40m{createF}')
    if mode == 0:
        print(f'\033[1;32;40mReading file...')
    elif mode == 1:
        print(f'\033[1;32;40mProcesing...')
    elif mode == 2:
        print(f'\033[1;32;40mGenerating file...')
    elif mode == 3:
        print(f'\033[1;32;40mReading Failed...')
    elif mode == 4:
        print(f'\033[1;32;40mProcesing Failed...')
    elif mode == 5:
        print(f'\033[1;32;40mGenerating Failed...')    
    elif mode == 6:
        print(f'\033[1;32;40mGenerating complete...')
