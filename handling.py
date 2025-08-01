# f=open('file1.py','x')//create new file
# f=open('file1.py','a')   //append file=a
# f=open('file1.py','w')    //write a file 
# f.write("Hello.")
# f.write("\nWorld.")
# f.close()


# f=open('file1.py','r')
# for each in f:
    # print(each)
# print(f.readline())
# //line by line output
# print(f.readline())
# print(f.read())   //complete output


# with open("file1.py")as f: // how we can read a file using the 'with' statement
#     data=f.read()
# print(data)


# f=open("file1.py","r") // illustrate read() mode with character wise
# print(f.read(13))


# with open("file1.py","r")as f:
# data =f.readlines()      // split lines while reading files in python.The split() function split the variable when space is encountered
# for line in data:
#     word=line.split()
#     print(word)

