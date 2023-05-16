file = open('Test.txt')
#print(file.read()) #reads all the contents of the file
#print(file.read(7))  # to read n number of characters by passing parameters
#print(file.readline())
#print(file.readline())
#print(file.readline())

line = file.readline()  #print all the contents line by line using readline method

#while line != "":  #using while loop
    #print(line)
   # line = file.readline()


for line in file.readlines():  #using for loop, readlines reads entire contents of the file in list format
    print(line)

file.close()

