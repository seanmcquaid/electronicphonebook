cont = True

phoneBook = {}

while(cont == True):
    print """Electric Phone Book
====================
1. Look up a contact
2. Create a new contact
3. Delete a contact
4. List all contacts
5. Quit"""
option = raw_input("Which option would you like to do? Choose a number between 1 and 5:  ")
    
if (option == "1"):
    searchContact = raw_input("Whose number are you looking for?  ").upper()
    if (searchContact) in phoneBook.keys():
        print "Their number is " + phoneBook[searchContact]
    else:
        print "Number not found, please try again!"
elif (option == "2"):
    contactName = raw_input("What's their name?  ").upper()
    contactNum = raw_input("What's their phone number? Please use the following format: xxx-xxx-xxxx:  ")
    phoneBook[contactName] = contactNum
elif (option == "3"):
    deleteContact = raw_input("Who do you want to delete?  ").upper()
    del phoneBook[deleteContact]
elif (option == "4"):
    for (k,v) in phoneBook.items():
        print (k,v)
elif (option == "5"):
        cont = False
else:
    print "Option not found, please select a number between 1 and 5"