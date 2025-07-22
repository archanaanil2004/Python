from calmodule import  addition, substraction, multtiplication, division

while True:
    print("1 . addition")
    print("2 . substraction")
    print("3 . multtiplication")
    print("4 . division")
    print("5.exit")
    choice =int(input("enter your choice :"))
    if (choice == 1):
        a=int(input("enter a number"))
        b=int(input("enter the second num"))
        print(addition(a,b))
        
    elif(choice == 2):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        print(substraction(a,b))
    elif(choice == 3):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        print(multtiplication(a,b))
    elif(choice == 4):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        if(b!=0):
           print(division(a,b))
        else:
            print("undefined")
    elif choice==5:
        print("exiting ......")
        break