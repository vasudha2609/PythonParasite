with open('Test.txt', 'r') as reader:     #object is being stored in reader variable
   content =  reader.readlines()        #readlines reads all the contents in the list
   print(f"Original List before reversing ,{content}")
   reversedList = list(reversed(content))
   print(f"Reversed List after reversing ,{reversedList}")
   #content(variable) holds the list of all the items in the file
   with open('Test.txt','w') as writer:
       for line in reversedList:
           writer.write(line)
           print(line)

