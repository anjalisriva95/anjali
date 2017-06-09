#importing details from another files and libraries
from colorama import init
from termcolor import colored
from spy_details import spy, friends, Spy, ChatMessage
from steganography.steganography import Steganography
from datetime import datetime

init()
#Already stored messages
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

print colored("Hello Let\'s get started",'green')
#Default question, continue as existing Spy or new Spy
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)
#Changing the text to upper case
existing=existing.upper()

#Function to add status for the Spy
def add_status():
    #By Default set updated status to null
    updated_status_message = None

    #Check if there is any message already saved or not
    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    #Choice for you, if you want to select from the older statuses or add a new status
    default = raw_input("Do you want to select from the older status (y/n)? ")

    #Create a new message
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        #Make sure that the length of the status is more than 0
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)#Append the new message in the existing messages
            updated_status_message = new_status_message#update the new message

    #Select from the already existing messages
    elif default.upper() == 'Y':

        item_position = 1

        #Display all the existing messages
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))
       #Select the message that you want to be your status

        if len(STATUS_MESSAGES) >= message_selection: #Checks the length of the message
            updated_status_message = STATUS_MESSAGES[message_selection - 1]#Updates the message

    #Invalid Input
    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        #print if status updated
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        #print if status not updated
        print colored('Invalid Input!! You did not update your status message','red')

    #return the updated status messages to the menu
    return updated_status_message

#Funtion for adding another friend of Spy
def add_friend():
    #Assigning all the variables of new_friend initial value of Spy class
    new_friend = Spy('','',0,0.0)
    #Taking input for Name
    new_friend.name = raw_input("Please add your friend's name: ")
    #Checking for the edge caes
    if len(new_friend.name) > 0 and new_friend.name.isdigit()==False:
        #Taking input for Salutation
        new_friend.salutation = raw_input("Are they Mr. or Ms. or Doc. or Prof.? Please fill in correct format :")
        #Checking for edge cases
        if len(new_friend.salutation) > 0:
            if new_friend.salutation =="Mr." or new_friend.salutation =="Ms." or new_friend.salutation =="Doc." or new_friend.salutation =="Prof.":

                #Taking input for Age
                new_friend.age = raw_input("Age?")

                #Checking for edge cases
                if new_friend.age=="" :
                    print colored("invalid input!!Please enter a valid Spy age",'red')
                elif new_friend.age.isdigit()==False: #isdigit() function checks whether the entered string is digit or not
                    print colored("invalid input!!Please enter a valid Spy age",'red')

                else:
                    new_friend.age = int(new_friend.age)#Change string type age to integer type

                    #Taking input for Rating
                    new_friend.rating = raw_input("Spy rating?")
                    #Checking for edge cases
                    if new_friend.rating=="":
                        print colored("Invalid Input!! Please input valid spy rating",'red')
                    elif new_friend.rating.isalnum()==True:#isalnum() function checks if the string if alphanumeric or not
                        print colored("Invalid Input!! Please input valid spy rating",'red')

                    else:
                        new_friend.rating = float(new_friend.rating)#Changing string type rating to float type

                        #Conditions for a valid spy
                        if len(new_friend.name) > 0 and int(new_friend.age) > 12 and int(new_friend.rating) >= spy.rating:
                            friends.append(new_friend)#Append the friend into your exixting friend list
                            print colored('Friend Added!','green')
                        else:
                            #Display for invalid entry
                            print colored('Sorry! Invalid entry. We can\'t add spy with the details you provided','red')

            else:
                #print for invalid edge cases
                print colored("Invalid Input!!",'red')
        else:
            #print for invalid edge cases
            print colored("Invalid Input!! Please use correct salutation.",'red')

    else:
        #print for invalid edge cases
        print colored("Invalid Input!! Please enter a valid Spy name",'red')

    #return length of the friend
    return len(friends)

#Function for selecting a friend
def select_a_friend():
    item_number = 0#set item number to 0
    print "Your Spy Friends are:\n"
    for friend in friends: #Displays all your spy friends ith their name age and rating
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1#Iterate the item_number by 1 for each friend

    #Choose from your existing friends
    friend_choice = raw_input("Choose from your friends ")
    #Position of the choosen friend in the list
    friend_choice_position = int(friend_choice) - 1#decrement it by one to get the actual position the list

    #Return the loaction of the selected friend
    return friend_choice_position

#Function for sending a scripted message
def send_message():

    friend_choice = select_a_friend()#send to the select_a_friend function and storing the value in friend_choice variable
    if friend_choice + 1 <= len(friends):#check if the number enetered is a part of list or not
        original_image = raw_input("What is the name of the image?")#stores te name and the pat of the image to be scripted
        output_path = 'output.jpg'#scripted image is stored in this variable
        text = raw_input("What do you want to say? Word Limit-100")#secret text
        Steganography.encode(original_image, output_path, text)#the image is encoded using stegnography

        new_chat = ChatMessage(text, True)#meassge added to the chat as send by the user

        friends[friend_choice].chats.append(new_chat)#message appended in the chat of a particular friend

        print colored("Your secret message image is ready!",'green')
    else:
        print colored("Invalid Input!!",'red')#the serial number does not exist


def read_message():

    sender = select_a_friend()#sends to select_a_friend function and storing the returned value in sender variable
    if int(sender) + 1 <= len(friends): #check if the number entered is a part of list or not
        output_path = raw_input("What is the name of the file?")#scripted image stored in OUTPUT.JPG
        if output_path=="output.jpg": #check for the correct output file
            secret_text = Steganography.decode(output_path)#the image is decoded using steganography
            if secret_text.isspace()==False:#Edge case when image contains no message
                if len(secret_text.split()) < 100: #check if the spy is saying more than 100 words
                    secret_text = secret_text.upper() #Changing the text to upper case
                    if "SOS" in secret_text.split():#.split() function split the text and then we search for 'SOS'
                        print colored("Call for more Help;DISTRESS SIGNAL",'green')
                    elif "BLOWN" in secret_text.split():#.split() function split the text and then we search for 'BLOWN'
                        print colored("Agents true identity discovered",'green')
                    elif "HUMINT" in secret_text.split():#.split() function split the text and then we search for 'HUMINT'
                        print colored("Intelligence collected from Human Sources",'green')
                    elif "OSINT" in secret_text.split():#.split() function split the text and then we search for 'OSINT'
                        print colored("Open source Intelligence ",'green')
                    else:
                        print secret_text #print the secret text

                    new_chat = ChatMessage(secret_text, False) #meassge added to the chat as send by the SPY

                    friends[sender].chats.append(new_chat)#message appended in the chat of a particular friend
                    print colored("Your secret message has been saved!",'green')
                else:
                    #the spy said more then 100 words
                    friends.remove(friends[sender])# remove the spy from te list
                    print colored("Your Friend didn't follow the word limit and so he has been deleted!!",'red')
            else:
                #image contains no message
                print colored("Blank Message",'red')
        else:
            #invalid output file
            print colored("Invalid Image",'red')

    else:
        print colored("Invalid Input!!",'red')#the serial number does not exist

#Function used for reading the chat history with a friend
def read_chat_history():

    read_for = select_a_friend()#select the frined from select_a_friend function and returns the value in read_for variable

    print '\n'#print in next line

    for chat in friends[read_for].chats: #for loop for printing the chat
        if chat.sent_by_me: #condition if the message was sent by user
            a=str(chat.time.strftime("%d %B %Y"))# storing the date and time in a variable a using Datetime
            #printing the message using colorama and termcolor
            print colored(a,'red') , colored('You said: ','blue') , colored(chat.message,'green')

        else: #condition if the message was sent by the Spy Friend
            b=str(chat.time.strftime("%d %B %Y"))# storing the date and time in a variable b using Datetime
            #printing the message using colorama and termcolor
            print colored(b,'red') , colored(friends[read_for].name,'blue') , colored(chat.message,'green')

#Function to start a spy chat
def start_chat(spy):

    spy.name=spy.salutation + " " + spy.name #concatinating spy name and spy salutation
    if spy.age >12 and spy.age < 50: #checking if spy is of correct age or not
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of spy is " + str(spy.rating) + " Proud to have you onboard"
        show_menu= True #boolean variable for shoing the menu

        while show_menu:
            #menu choices
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice=raw_input(menu_choices) #input the choice

            if len(menu_choice) > 0:#checking for an empty statement
                menu_choice = int(menu_choice)#changing string to integer type
                if menu_choice==1: #if 1 redirected to add_status function
                    spy.current_status_message = add_status()
                elif menu_choice == 2: #if 2 redirected to add_friend function
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends) #displaying the total number of friends
                elif menu_choice == 3: #if 3 redirected to send_message function
                    send_message()
                elif menu_choice == 4: #if 4 redirected to read_message function
                    read_message()
                elif menu_choice == 5: #if 5 redirected to read_chat_history function
                    read_chat_history()
                else:# if 6 or any other entry exit the menu
                    show_menu = False

    else:# for incorrect age
        print colored("Sorry you are not correct age to be a spy ",'red')

#check if you want to continue as the default user
if existing=="Y":
    start_chat(spy)#redirects to the start_chat(spy)
#check if you dont want to continue as the default user but want to add as a new user
elif existing=="N":
    spy = Spy('', '', 0, 0.0)# Assigning all the variables of new_friend initial value of Spy class
    #Taking input for Nmame
    spy.name= raw_input("Welcome to spy_chat, you must tell me your spy_name first:")
    #Checking for edge cases
    if len(spy.name)>0 and spy.name.isdigit()==False :

        #Taking input for Salutation
        spy.salutation=raw_input("what should we call you'Mr. or Ms. or Doc. or Prof.'?")
        #Checking for edge cases
        if len(spy.salutation) > 0:
            if spy.salutation =="Mr." or spy.salutation =="Ms." or spy.salutation =="Doc." or spy.salutation =="Prof.":

                #Taking input for Age
                spy.age=raw_input("what is your age?")

                #Checking for edge cases
                if spy.age=="" :
                    print colored("invalid input!!Please enter a valid Spy age",'red')
                elif spy.age.isdigit()==False: #isdidgit()function is used to check if the string contains numeric value or not
                    print colored("invalid input!!Please enter a valid Spy age",'red')

                else:
                    spy.age = int(spy.age)#Converting string into integer type
                    #Taking input for Rating
                    spy.rating=raw_input("what is your spy rating?")
                    #Checking for edge cases
                    if spy.rating=="":
                        print colored("Invalid Input!! Please input valid spy rating",'red')
                    elif spy.rating.isalnum()==True: #isalnum() function is used to check for alphanumeric string
                        print colored("Invalid Input!! Please input valid spy rating",'red')
                    else:
                        spy.rating=float(spy.rating)#Converting string to float type
                        #Check for a better type of rating and displaying aproper message
                        if spy.rating > 4.5:
                            print colored("Great ace",'blue')
                        elif spy.rating > 3.5 and spy.rating <= 4.5:
                            print colored("You are one of the good ones.",'blue')
                        elif spy.rating >= 2.5 and spy.rating <= 3.5:
                            print colored("You can always do better",'blue')
                        else:
                            print colored("We can always use somebody to help in the office.",'blue')

                        spy_is_online = True #boolean variable for telling the online situation of the spy

                        start_chat(spy)#redirects to start_chat function
            else:
                #For incorrect salutation
                print colored("Invalid Input!! Please enter proper salutation.",'red')
        else:
            #For incorrect salutation
            print colored("Invalid Input!! Please enter propper salutation.",'red')


    else:
        #For incorrect spy name
        print colored("Please enter a valid name",'red')

else:
    #For invalid input
    print colored("Invalid Input!!",'red')

