def main_menu():
    menu = """ 
    NOKIA LIST OF MENU FUNCTIONS. PRESS
    1. Phone book
    2. Messages
    3. Chat
    4. Call register
    5. Tones
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
    10. Reminders
    11. Clock
    12. Profiles
    13. SIM services
    Press 14 to quit
    """
    print(menu)
    return int(input("Enter menu number: "))

def phone_book():
    phonebook_menu = """ 
    1. Search
    2. Service Nos
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Options
    9. Speed dials
    10. Voice tags 
    """
    print(phonebook_menu)
    option = int(input("Press 8 to enter option: "))
    if option == 8:
        print("1. Type of view")
        print("2. Memory Status")
    else:
        print("Invalid choice.")

    while True:
        back =  int(input("Enter (0) to go back to menu: "))
    if back == 0:
        print(phonebook_menu)	 
    continue
def messages():
    messages_menu = """ 
    1. Write messages
    2. Inbox
    3. Outbox
    4. Picture messages
    5. Templates
    6. Smileys
    7. Message settings
    8. Info service
    9. Voice mailbox number
    10. Service command editor
    """
    print(messages_menu)
    option = int(input("Press 1 or 2 for message settings (7): "))
    if option == 1:
        print("SET 1")
        print("1. Message center number")
        print("2. Messages sent as")
        print("3. Message validity")
    elif option == 2:
        print("COMMON")
        print("1. Delivery reports")
        print("2. Reply via same center")
        print("3. Character support")

def chat():
    print("CHAT")
    input("Enter (0) to go back to menu: ")

def call_register():
    call_register_menu = """ 
    1. Missed call
    2. Received call
    3. Dialed numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call costs
    7. Call cost settings
    8. Prepaid credit
    """
    print(call_register_menu)
    call_duration = int(input("Enter 5 call duration 0r 6 and 7: "))

    if call_duration == 5:
        print (""" 1. Last call duration
		   2. All calls' duration
        	   3. Received call duration
		   4. Dialled calls' duration
		   5. clear timers """)
    elif call_duration == 6:
        print (""" 1. Last call cost
		   2. All calls' cost
	  	   3. Clear counters """) 
    elif call_duration == 7:
        print (""" 1. Call cost limit
		   2. Show costs in """) 
    else:
        print("invalid input")
def tones():
    Tones_menu = """ 
    1. Ringing tone
    2. Ringing volume
    3. Incoming call alert
    4. Keypad tones
    5. Warnig and games tone
    6. Vibrating alert
    7. Composer
    8. Message alert tone
    9. Screen saver
    """
    print(Tones_menu) 
    input("Enter (0) to go back to menu: ")

def setting():
    settings_menu = """ 
    1. Call settings
    2. Phone settings
    3. Security Settings
    4. Restore factory settings
    """
    print(settings_menu)
    settings = int(("Enter a number between 1 to 3: "))

    if settings == 1:
        print("""  1. Automatic redial
		   2. Speed dialling
        	  3. Call waiting options
		   4. Own number sending
		   5. Phone line in use
		   6. Automatic answer  """)
    elif settings == 2:
        print("""  1. Language
		   2. Lights
        	   3. Cell info display
		   4. Welcome note
		   5. Network selection
		   6. Confirm SIM service actions  """)
    elif settings == 3:
        print("""  1. Pin code request
		   2. call barring service
        	   3. Fixed dialling
		   4. Closed user group
		   5. Phone security
		   6. Change access codes  """)

def call_divert():
    print("Call divert")
    input("Enter (0) to go back to menu: ")

def games():
    print("Games")
    input("Enter (0) to go back to menu: ")

def calculator():
    print("Calculator")
    input("Enter (0) to go back to menu: ")

def reminders():
    print("Calculator")
    input("Enter (0) to go back to menu: ")

def clock():
    print("""  1. Alarm clock
	       2. Clock settings
               3. Date settings 
	       4. Stopwatch
	       5. Countdown timer
	       6. Auto update of date and time  """)
def profiles():
    print("Profiles")
    input("Enter (0) to go back to menu: ")

def Sim_services():
    print("SIM services")
    input("Enter (0) to go back to menu: ")

menu_actions = {
    1: phone_book,
    2: messages,
    3: chat,
    4: call_register,
    5: tones,
    6: setting,
    7: call_divert,
    8: games,
    9: calculator,
    10: reminders,
    11: clock,
    12: profiles,
    13: Sim_services,
}
      
while True:
    choice = main_menu()
    if choice == 14:
        print("Bye!")
        break
    elif choice in menu_actions:
        menu_actions[choice]()
    else:
        print("Invalid input. Try again!")