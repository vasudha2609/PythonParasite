try:
    with open('Test.txt') as reader:   #when the text file exists and no error occurs
        reader.read()
except:
    print("This will be displayed in case of any error in try block")


#when text file doesnt exists, failure of code has been wrapped in try and exception msg gets displayed.
try:
    with open('Filelog.txt') as reader:
        reader.read()

except:
    print("This will be displayed in case of any error in try block")

#when text file doesnt exists, code failure/ catch error msg should be displayed in python default error msg
try:
    with open('Filelog.txt') as reader:
        reader.read()

except Exception as e:
    print(e)               # output: [Errno 2] No such file or directory: 'Filelog.txt'

#finally
try:
    with open('Filelog.txt') as reader:
        reader.read()

except Exception as e:
    print(f"Catch Block Exception thrown is {e}")
finally:
    print("clear records")

