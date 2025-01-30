from hashlib import sha256
import os
Logged_in = False
message_shown = False
Listed_Users = []
Listed_Passwords = []
USSB_is_Disabled = True
User_Active = True

try:
  Secure_data_extraction = open(r"Secure_data_storage.txt", "r")
  Secure_data_extraction.close()
except FileNotFoundError:
  Secure_data_insertion = open(r"Secure_data_storage.txt", "a")
  Secure_data_insertion.write("USSB, 3cfe05e65868e8e21f0704212907fe9929322ee21e9d7c6bb848155eb60e483b\n")
  Secure_data_insertion.close()
Secure_data_extraction = open(r"Secure_data_storage.txt", "r")
Extracted_Data = Secure_data_extraction.readlines()
Secure_data_extraction.close()
for i in range(len(Extracted_Data)):
  Extracted_Data[i] = Extracted_Data[i].strip("\n")
  Extracted_Data[i] = Extracted_Data[i].split(", ")
  Listed_User_Element = Extracted_Data[i][0]
  Listed_Password_Element = Extracted_Data[i][1]
  Listed_Users.append(Listed_User_Element)
  Listed_Passwords.append(Listed_Password_Element)

Option = input("Log in or Sign in? ")
if Option.lower() == "log in":
  Username = input(str("Enter your username: "))
  Password = input(str("Enter your password: "))
  h = sha256()
  h.update(f'{Password}'.encode('utf-8'))
  Encoded_Password = h.hexdigest()
  for i in range(len(Listed_Passwords)):
    if Username == Listed_Users[i] and Encoded_Password == Listed_Passwords[i]:
      while User_Active:
        Logged_in = True
        try:
          Current_User = open(f"User_{i+1}.txt", "r")
          Current_User.close()
        except FileNotFoundError:
          Current_User = open(f"User_{i+1}.txt", "w")
          Current_User.write("Perm:b All~s None\n")
          Current_User.close()
        Current_User = open(f"User_{i+1}.txt", "r")
        Current_User_Data = Current_User.readlines()
        Accessibility = Current_User_Data[0]
        Current_User_Data.remove(Current_User_Data[0])
        Current_User.close()
        for i in range(len(Current_User_Data)):
          Current_User_Data[i] = Current_User_Data[i].strip("\n")
          Current_User_Data[i] = Current_User_Data[i].split(", ")
        if Username == "USSB":
          Setting_change_affirmation = input("Open USSB setting changer? [y/n] ")
          if Setting_change_affirmation == "y":
            USSB_TM = open(r"User_1.txt", "w+")
            USSB_TM_Data = USSB_TM.read()
            USSB_TM_Data = USSB_TM_Data.split(",")
            USSB_TM.close()
            Setting_change = input("USSB setting change: ")
            Secure_data_insertion = open(r"User_1.txt", "w")
            Secure_data_insertion.write("User Special Status Bot, Bot Activation Or Settings Change,"+Setting_change+",")
          elif Setting_change_affirmation == "n":
            USSB_TM = open(r"User_1.txt", "r")
            USSB_TM_Data = USSB_TM.read()
            USSB_TM_Data = USSB_TM_Data.split(",")
            USSB_TM.close()

            if Current_User_Data == "Affirmed User Deletion" and not USSB_is_Disabled:
              print("User Deletion Affirmed")
              Selective_Deletion = input("Selective Deletion? [y/n] ")
              if Selective_Deletion == "y":
                  print("Selective Deletion Selected")
                  User_found = False
                  User_ID = 0
                  User_Deletion = input("Which user is to be deleted? ")
                  if User_Deletion == "USSB":
                    print("USSB cannot be deleted")
                  elif User_Deletion != "USSB":
                    for i in range(len(Listed_Passwords)):
                      if User_Deletion == Listed_Users[i]:
                        os.remove(f"User_{i+1}.txt")
                        User_found = True
                        User_ID = i+1
                      elif User_found == True and User_ID < i+1:
                        os.rename(f"User_{i+1}.txt", f"User_{i}.txt")
                    Secure_data_removal = open(r"Secure_data_storage.txt", "w")
                    Secure_data_removal.write("")
                    Secure_data_removal.close()
                    for i in range(len(Listed_Passwords)):
                      if User_Deletion != Listed_Users[i]:
                        Secure_data_removal = open(r"Secure_data_storage.txt", "a")
                        Secure_data_removal.write(Listed_Users[i])
                        Secure_data_removal.write(",")
                        Secure_data_removal.write(Listed_Passwords[i])
                        Secure_data_removal.write(",")
                        Secure_data_removal.close()
                  else:
                    print("An error has occured")
              elif Selective_Deletion == "n":
                print("Delete all Selected")
                User_wipe = open(r"Secure_data_storage.txt", "w")
                User_wipe.write(Username+","+Encoded_Password+",")
                User_wipe.close()
                for i in range(len(Listed_Passwords)):
                  if Username != Listed_Users[i]:
                    if f"User_{i+1}" in os.listdir():
                      os.remove(f"User_{i+1}.txt")

            elif Current_User_Data == "Affirmed User Info Clear" and not USSB_is_Disabled:
              print("User Info Clear Affirmed")
              Selective_Clear = input("Selective Clear? [y/n] ")
              if Selective_Clear == "y":
                print("Selective Clear Selected")
                User_Clear = input("Which user is to be cleared? ")
                if User_Clear == "USSB":
                  print("USSB cannot be cleared")
                elif User_Clear != "USSB":
                  for i in range(len(Listed_Users)):
                    if User_Clear == Listed_Users[i]:
                      os.remove(f"User_{i+1}.txt")
              elif Selective_Clear == "n":
                print("Clear all Selected")
                for i in range(len(Listed_Passwords)):
                  if Username != Listed_Users[i]:
                    os.remove(f"User_{i+1}.txt")

            User_Permission_Change = input("Which Users permission is to be changed? ")
            if User_Permission_Change == "USSB":
              print("USSB has a set Permission which cant be changed.")
            elif User_Permission_Change != "USSB":
              New_Perm_Level = input("What is the new permission for this user? ")
              for i in range(len(Listed_Users)):
                if User_Permission_Change == Listed_Users[i]:
                  Current_User = open(f"User_{i+1}.txt", "a+")
                  Current_User.close()
                  Current_User = open(f"User_{i+1}.txt", "r")
                  Current_User_Data = Current_User.readlines()
                  Current_User.close()
                  for i in range(len(Current_User_Data)):
                    Current_User_Data[i].strip("\n")
                    Current_User_Data[i] = Current_User_Data[i].split(", ")
                  try:
                    Current_User_Data[0][0] = f"{New_Perm_Level}\n"
                  except SyntaxError:
                    Current_User_Data = f"{New_Perm_Level}\n"
                  Secure_data_change = open(f"User_{i+1}.txt", "w")
                  for i in range(len(Current_User_Data)):
                    Secure_data_change.write(Current_User_Data[i])
                    Secure_data_change.close()
            quit()

        else:
          if not message_shown:
            message_shown = True
            print("Welcome back, " + Username)
            print("Your file data is:")
            for i in range(len(Current_User_Data)):
              print(f"Line {i}: " + ", ".join(Current_User_Data[i]))
            Accessibility = Accessibility.strip("\n")
            Accessibility = Accessibility.split(":")[1]
            Accessibility = Accessibility.split("~")
            Base_Access = Accessibility[0]
            Special_Access = Accessibility[1]
  
  if not Logged_in and not message_shown:
    message_shown = True
    print("Incorrect username or password")
 
elif Option.lower() == "sign in":
  Username = input("Create a username: ")
  Password = input("Create a password: ")
  if Username in Listed_Users:
    print("This username is already taken, but remember that your display name can be changed later in settings. (display name does not equal username)")
  else:
    h = sha256()
    h.update(f'{Password}'.encode('utf-8'))
    Encoded_Password = h.hexdigest()
    Secure_data_insertion = open(r"Secure_data_storage.txt", "a")
    Secure_data_insertion.write(f"{Username}, {Encoded_Password}\n")
    Secure_data_insertion.close()
    print("You have signed in!")
else:
  print("Invalid command.")