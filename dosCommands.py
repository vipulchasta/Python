import os

exit = 0
while (exit == 0) :
    print("To Clear Screen Press 1")
    print("To Make a Directory Press 2")
    print("To Make a File Press 3")
    print("To Exit Press 4")
    print("Enter Your Choice: ",end="")
    ch =  input("") 
    if ch == '1':
        os.system("cls")
    elif ch == '2':
        fileName = input("Enter the File Name: ")
        os.system("md " + fileName)
        print("File Sucessfully Created.")
    elif ch == '3':
        fileName = input("Enter the File Name: ")
        os.system("copy con " + fileName )
        print("File is Successfully Created.")
    elif ch == '4':
        exit = 1
    else:
        print("Wrong Input.")
input("Program terminated Successfully.")
