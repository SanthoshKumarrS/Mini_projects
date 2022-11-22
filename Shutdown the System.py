import os

shutdown = input("Do you want to shutdown ? : (yes / no) - ")

if shutdown == 'no':
    exit()
elif shutdown == 'yes':
    os.system("shutdown /s /t 1")
else:
    print("Sorry i dont understand")