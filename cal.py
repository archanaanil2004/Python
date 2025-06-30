while True:
    print("1 . ADDITION")
    print("2 . substraction")
    print("3 . multtiplication")
    print("4 . division")
    print("5.exit")
    choice =int(input("enter your choice :"))
    if (choice == 1):
        a=int(input("enter a number"))
        b=int(input("enter the second num"))
        c=a+b
        print(c)
        
    elif(choice == 2):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        c=a-b
        print(c)
    elif(choice == 3):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        c=a*b
        print(c)
    elif(choice == 4):
        a=int(input("enter a num"))
        b=int(input("enter second num"))
        if(b!=0):
            c=a/b
            print(c)
        else:
            print("undefined")
    elif choice==5:
        print("exiting ......")
    break