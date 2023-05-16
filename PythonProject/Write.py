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

with open('Test.txt','r') as reader:
    content= reader.readlines()
    print(f"List out the contents before reversing, {content}")
    reversed_list= list(reversed(content))
    print(f"List out the list after reversing, {reversed_list}")
    with open('Test.txt', 'w') as writer:
        reversed_list = list(reversed(reversed_list))
        for i in reversed_list:
            writer.write(i)
            print(i)