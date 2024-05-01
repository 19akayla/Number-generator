from colorama import Fore
#Gives color
import random


def play():
  #FUNction called play to continue reusing the code
  # gives random number between 0 to 299
  value = random.randint(0, 200)
  count = 1
  #Amount of guesses
  rounds = random.randint(1, 10)
  print(Fore.RED + "Welcome to the guessing game!"+ Fore.RESET)
  print()
  print("Pick a color!!\n Red \n Green \n Blue \n Yellow")
  print()
  color = input().title()
  
  if color == "Red":
    print()
    name = input(Fore.RED + 'What is your username? ' + Fore.RESET)
    print(f"Hello {name} this is the guessing game.")
  elif color == "Green":
    print()
    name = input(Fore.GREEN + 'What is your username? ' + Fore.RESET)
    print(f"Hello {name} this is the guessing game.")
  elif color == "Blue":
    print()
    name = input(Fore.BLUE + 'What is your username? ' + Fore.RESET)
    print("Hello " + Fore.BLUE + name + Fore.RESET + " this is the guessing game.")
  elif color == "Yellow":
    print()
    name = input(Fore.YELLOW + 'What is your username? ' + Fore.RESET)
    print()
    print("Hello " + Fore.YELLOW + name + Fore.RESET + " this is the guessing game.")
  else:
    print(Fore.RED + "Invalid color. You cant play." + Fore.RESET)
    exit()
  
  
  print()
  print(f"The rules are you have {rounds} tries to guess the number..")
  print()
  print("I am thinking of a number between 0 and 200.")
  #warning = int(input("When do you want to be warned of the rounds you have left? "))
  #Ex if they put in 2 you want to be warned when you have 2 rounds left
  print()
  
  
  guess = False  
  while(count <= rounds):
    try:
      guess = int(input("Enter your lottery number: "))
      print()
      print()
      #Trys the code if they enter a number
      if guess > 200 or guess < 0:
          print(Fore.RED + 'Your limit is 0 to 200'+ Fore.RESET)
          print()


        #This would only happen if the input is greater than 200 or less than 0
      elif guess == value:
        print(Fore.GREEN + "Congratulations " + name + " you won the lottery!")
        # prints the number of guesses
        print("You guessed it in " + str(count))
        # if the guess is correct then print you won
        print()
        print(f"Correct!! the number was {guess} please play again {name}")
        print(Fore.GREEN + '''              ⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀
        ⢠⣤⣤⣤⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⣤⣤⣠
        ⢸⠀⡶⠶⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⠶⠶⡆⡼
        ⠈⡇⢷⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢸⢁⡗
        ⠀⢹⡘⡆⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⢀⡏⡼⠀
        ⠀⠀⢳⡙⣆⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢀⠞⡼⠁⠀
        ⠀⠀⠀⠙⣌⠳⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⡴⣫⠞⠀⠀⠀
        ⠀⠀⠀⠀⠈⠓⢮⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣩⠞⠉⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠉⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠋⠁⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⢀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⡇⢸⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠖⠒⠓⠚⠓⠒⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣀⣠⣞⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣙⣆⣀⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠓⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠖⠃⠀⠀⠀⠀⠀⠀''' + Fore.RESET)
        break
        #End of the game
      elif(guess < value):
      #if the guess is less than the value then print the number is too low
          print(Fore.RED + "Your guess is too low!! Please try again" + Fore.RESET)
        
          print()
        # when the number is too high print number is too high
      elif(guess > value):
          print(Fore.GREEN + "Your guess is too high!!" + Fore.RESET)
          print()
      else:
        print("You are incorrect")
      count += 1
      #count is the amount of guesses they made
      if count == rounds:
        print(Fore.YELLOW + "You have one guess left. You got this" + Fore.RESET)
      elif count > rounds:
        print(Fore.BLACK , "YOU LOST try again later the number was" , value , Fore.RESET)
      #if warning == rounds:
      #  print(f"You have {rounds} guesses left")
      #elif warning > rounds:
      #  print("I cant give you a warning")
      #  print(" If the warning is more than the rounds")
      #  print("Please try again")
      #  break
    except:
      print()
      print(Fore.BLACK, "Not a number. You cant play.", Fore.RESET)
      break
      #Code does not work if the number is not inputed

play() 
#Call the function