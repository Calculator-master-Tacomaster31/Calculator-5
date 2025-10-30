import os
import sys

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import id_token
from google.auth.transport import requests

global passYes, username

def google_sign_in():
    global passYes, username
    print("Opening browser for Google sign-in...")
    time.sleep(2)
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json',
        scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email']
    )
    creds = flow.run_local_server(
        port=0,
        authorization_prompt_message="",
        )
    id_info = id_token.verify_oauth2_token(creds.id_token, requests.Request())
    email = id_info['email']
    print(f"\nSuccessfully signed in as: {email}\n")
    username = email
    passYes = True
    return email

def resource_path(relative_path):
    #Get absolute path to resource, works for dev and PyInstaller exe
    try:
        # PyInstaller stores temp files in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Imports
import random
import time
import math

# Determine a writable path for users.txt
def get_user_data_path():
    # Store next to the exe or script
    base_path = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    return os.path.join(base_path, "users.txt")

#Clear shell
def clearShell():
    count = 0
    while count < 100:
        print("\n")
        count += 1

#Set numbers
num1 = 0
num2 = 0

#Log in
while True:
    #Define verable that desides if you are logged in or not
    passYes = False

    #Code is approved by Malakai
    print("This code is Malakai aproved as of 10/24/25!")
    input("Press enter to continue...")
    time.sleep(.5)
    clearShell()

    def googleSignIn():
        username = google_sign_in()
    #Load users from text file
    def loadUsers():
        users = {}
        file_path = get_user_data_path()
        try:
            with open(file_path, "r") as file:
                for user in file:
                    name, password = user.strip().split(":")
                    users[name] = password
        except FileNotFoundError:
            open(file_path, "w").close()
        return users

    #Create new user
    def newUser(username, newPassword):
        file_path = get_user_data_path()
        with open(file_path, "a") as file:
            file.write(f"{username}:{newPassword}\n")
    while passYes == False:
        users = loadUsers()
        #Ask for username to login or signup
        while True:
            try:
                loginType = int(input("Press 1 for login with Google\nPress 2 for login with Username\nSelection: "))
                break
            except:
                print("Not an option!")
        if loginType == 2:
            while True:
                try:
                    username = input("Enter username: ")
                    break
                except:
                    print("Not an option!!!")
                    time.sleep(2)
                    input("Press enter to continue...")
            if username in users:
                #Enter password
                while True:
                    try:
                        password = input("Enter your password ")
                        break
                    except:
                        print("Not an option!!!")
                        time.sleep(2)
                        input("Press enter to continue...")
                if users[username] == password:
                    print("Login SUSSESFULL")
                    passYes = True
                    time.sleep(2)
                else:
                    print("Login UNSSESFULL")
                    passYes = False
                    time.sleep(2)
                    count = 0
                    while count < 2:
                        print("\n")
                        count += 1
            else:
                print("User name not found")
                time.sleep(1.2)
                while True:
                    try:
                        create = input("Do you want a new account? ").lower()
                        break
                    except:
                        print("Not an option!!!")
                        time.sleep(2)
                        input("Press enter to continue...")
                if create == 'yes':
                    newPassword = input("Enter a password ")
                    newUser(username, newPassword)
                    print("Your account has been created succesfully!")
                    passYes = True
                else:
                    print("Ok going back to password enter screen...")
        elif loginType == 1:
            googleSignIn()
            
    #Define operation numbers for responces.txt and other .txt file
    operationNames = {
        0: 'Leave',
        1: 'Add',
        2: 'Subtract',
        3: 'Multiply',
        4: 'Devide',
        5: 'Exponit',
        6: 'Square Root',
        7: 'Reamender',
        8: 'Abasulte Value',
        9: 'Power Of 10',
        10: 'Squared Number',
        11: 'Cubed Number',
        12: '% Calculator',
        13: 'Round',
        14: 'Round Down',
        15: 'Round Up',
        16: 'Log',
        17: 'Log10',
        18: 'Sin',
        19: 'Cos',
        20: 'Tan',
        21: 'Factoral',
        22: 'GCD',
        23: 'LCM',
        24: 'Root',
        25: 'Asin',
        26: 'Acos',
        27: 'Atan',
        28: 'Degrees',
        29: 'Rosons',
        30: 'Random Sayings',
        31: 'IN to CM',
        32: 'CM to IN',
        33: 'MI to KM',
        34: 'KM to MI',
        35: 'Pounds to Kilograms',
        36: 'Kilograms to Pounds',
        37: 'Farenhight to Celsis',
        38: 'Celsis to Farenhight',
        39: 'Random number settings',
        40: 'Full Eqation',
        41: 'Read History',
        42: 'Games',
        43: 'Math Quiz',
        44: 'Memery Wipe',
        45: 'Date and Time',
        46: 'Weather',
        47: 'magic 8 ball',
        48: 'ASCII art',
        49: 'prime Checker',
        50: 'jokes',
        51: 'Sign out',
        52: 'Signed In',
        }

    #Define verables
    start = 0
    total = 1
    codeLooped = False

    #Random loading screens
    with open(resource_path("loading.txt"), "r") as file:
        responce = file.read().split("\n")
    def loading():
        print(random.choice(responce))
        time.sleep(2)

    #Round/format
    def roufor(start):
        total = start
        while True:
            try:
                forround = int(input("Do you want to round or format?\nPress 1 for round\nPress 2 for format\nPress 3 to leave alone\nSelection: "))
                break
            except:
                print("Not an option!!!")
        #Round
        if forround == 1:
            while True:
                try:
                    roundAmount = int(input("Press 1 for nearest tenth\nPress 2 for nearest hundredth\nPress 3 for nearest thousandth\nand so on.....\nSelection: "))
                    break
                except:
                    print("Not an option!!!")
            if roundAmount >= 1:
                total = (f"%.{roundAmount}f") % total # f-string, curly brackets {} containing an expression will insert into string, eg. f"Total: {1+1}" -> "Total: 2"
            else:
                print("not an option")
        #Format
        elif forround == 2:
            while True:
                try:
                    formatAmount = int(input("Press 1 to format to tenth\nPress 2 to format to hundredth\nPress 3 to format to thousandth\nAnd so on.......\nSelection: "))
                    break
                except:
                    print("Not an option!!!")
            if formatAmount >= 1:
                total = (f"#.{formatAmount}f") % total
            else:
                print("Not an option!!!!")
        
        #Do nothing
        elif forround == 3:
            pass

        else:
            print("Not an option")

        return total

    #Press enter to contiue
    def entcon():
        input("Press enter to continue..... ")
        time.sleep(2.5)

    #Countdown to selection
    def countdownToSelection():
        entcon()
        print("Back to seletion in")
        time.sleep(2)
        print('5')
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1.25)

    # Save result to file
    def saveResult(num1, num2, choice, total):
        try:
            with open(resource_path("responces.txt"), "a") as file:  
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {choice} | {num1}, {num2} = {total}\n")
        except:
            print("Error saving result!")

    #Save all resalts to dev file
    def devSaveResult(num1, num2, choice, total):
        try:
            with open(resource_path("Develper Responces.txt"), "a") as file:
                file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {operationNames[choice]} | {num1}, {num2} = {total}\n")
        except:
            print("Error")

    #Read history
    def readHistory():
        loading()
        try:
            with open('responces.txt', 'r') as file:
                print('-------History-------')
                print(file.read())
        except FileNotFoundError:
            print("No history!!!!")
        entcon()

    #sign out
    def signOut():
        global passYes, codeLooped
        print(f"Good bye {username}, Thank you for using my calculator!")
        input("Press enter to continue...")
        passYes = False
        codeLooped = False
        total = "signout"
        return total
        
    #Exit
    def leave():
        loading()
        clearShell()
        print("Good Bye")
        time.sleep(5)
        with open(resource_path("operationCount.txt"), "w") as file:
            for key, count in operation_count.items():
                file.write(f"{operationNames.get(key, key)}: {count}\n")
        devSaveResult(num1, num2, choice, total)
        import sys
        sys.exit()
        
    #Add
    def add(num1,num2):
        loading()
        total = num1+num2
        return total

    #Subtract
    def subtract(num1,num2):
        total = num1-num2
        return total

    #Multiply
    def multiply(num1,num2):
        total = num1*num2
        return total

    #Devide
    def devide(num1,num2):
        total = num1/num2
        return total

    #Exponit
    def exponit(num1,num2):
        total = num1 ** num2
        return total

    #Square root
    def sqareRoot(num1):
        total = num1 ** 0.5
        return total

    #Remander
    def remaneder(num1,num2):
        total = num1%num2
        return total

    #Absulote value
    def absuloteValue(num1):
        total = abs(num1)
        return total

    #Power of 10
    def powerOf10(num1):
        total = 10 ** num1
        return total

    #Squared number
    def squaredNumber(num1):
        total = num1 ** 2
        return total

    #Cubed number
    def cubedNumber(num1):
        total = num1 ** 3
        return total

    #% calculator
    def persentageCalcultor(num1,num2):
        if num2 != 0:
            total = (num1/num2) * 100
            return total
        #Cannot devide by 0
        elif num2 == 0:
            print("Can not devide by 0!!!")
            time.sleep(5)
            countdownToSelection()
            return 0

    #Round
    def rond(num1):
        total = round(num1)
        return total

    #Round down
    def roundDown(num1):
        total = math.floor(num1)
        return total

    #Round up
    def roundUp(num1):
        total = math.ceil(num1)
        return total

    #log
    def log(num1):
        total = math.log(num1)
        return total

    #log10
    def log10(num1):
        total = math.log10(num1)
        return total

    #sin
    def sin(num1):
        total = math.sin(num1)
        return total

    #cos
    def cos(num1):
        total = math.cos(num1)
        return total

    #tan
    def tan(num1):
        total = math.tan(num1)
        return total

    #factoral
    def factoral(num1):
        if num1 >= 0 and float(num1).is_integer():
            total = math.factorial(int(num1))
            return total
        else:
            print("Not avalible")

    #gcd
    def gcd(num1,num2):
        if float(num1).is_integer() and float(num2).is_integer():
            total = math.gcd(int(num1), int(num2))
            return total
        else:
            print("Not avalable")

    #Lcm
    def lcm(num1,num2):
        if float(num1).is_integer() and float(num2).is_integer:
            a, b = int(num1), int(num2)
            total = abs(a * b) // math.gcd(a, b) if b != 0 else None
            return total
        else:
            print("Not anvalable")

    #Root
    def root(num1,num2):
        if num2 != 0:
            total = num1 ** (1/num2)
            return total

        elif num2 == 0:
            print("Not avalible")

    #Radians
    def asin(num1):
        total = math.radians(num1)
        return total

    #Acos
    def acos(num1):
        total = math.acos(num1)
        return total

    #Atan
    def atan(num1):
        total = math.atan(num1)
        return total

    #Degrees
    def degrees(num1):
        total = math.degrees(num1)
        return total

    #Rosons
    def rosons(num1):
        total = math.radians(num1)
        return total

    #Random sayings
    def randomSayings():
        count = int(input("How many? "))
        global count2
        while True:
            try:
                timesleepYes = input("Do you want to hit enter after every random saying? (Yes/No)").lower()
                break
            except:
                print("Not an option!!!")
                time.sleep(2)
                input("Press enter to continue...")
        if timesleepYes == 'yes':
            timesleep2 = False
        elif timesleepYes == 'no':
            while True:
                try:
                    timesleep = float(input("How many seconds would you like to wait between each random saying? "))
                    break
                except:
                    print("Not an option!!!")
                    time.sleep(2)
                    input("Press enter to continue...")
            timesleep2 = True
        count2 = 0
        while count2 < count:
            loading()
            if timesleep2:
                time.sleep(timesleep)
            if not timesleep2:
                input("Press enter to continue...")
            count2 += 1
        return 0

    #IN to CM
    def INtoCM(num1):
        total = num1 * 2.54
        return total

    #CM to IN
    def CMtoIN(num1):
        total = num1 / 2.54
        return total

    #MI to KM
    def MItoKM(num1):
        total = num1 * 1.60934
        return total

    #KM to MI
    def KMtoMI(num1):
        total = num1 / 1.60934
        return total

    #Pounds to kilograms
    def poundsToKilograms(num1):
        total = num1 * 0.45359237
        return total

    #Kilograms to pounds
    def kilogramsToPounds(num1):
        total = num1 / 0.45359237
        return total

    #F to C
    def FtoC(num1):
        total = (num1 - 32) * 5/9
        return total

    #C to F
    def CtoF(num1):
        total = (num1 * 9/5) + 32
        return total

    #Random number settings
    def randomNumberSettings():
        try:
            clearShell()
            randomNumberSettingsChange = str(input("Do you want random numbers?\nYes or No: ")).lower()
        except:
            clearShell()
            print("Not an option")

        if randomNumberSettingsChange == 'yes':
            num1 = random.randint(-50000,50000)
            num2 = randint(-50000,50000)
            ran1 = True
            ran2 = True
            time.sleep(5)
            countdownToSelection()
        elif randomNumberSettingsChange == 'no':
            ran1 = False
            ran2 = False
            time.sleep(5)
            countdownToSelection()

        return 0

    #Enitre equation entering
    def fullEQ():
        eq = input("What is your equation? ")
        total = 0
        try:
            total = eval(eq, {"__builtins__": None}, {"math": math})
        except Exception:
            print("Not correct format!!!")

        return total

    #Easter egg
    def easterEgg():
        clearShell()
        print("You found me!")
        time.sleep(5)
        countdownToSelection()
        return 0

    #Games
    def games():
        clearShell()
        while True:
            try:
                gamein = int(input("Press 1 for number guessing game\nPress 2 for Rock Paper Sisters\nSelection: "))
                break
            except:
                print("Not an option!!!")
        #Number guessing game
        if gamein == 1:
            while True:
                try:
                    raninput = input("Do you want random numbers?\nPlease enter 'yes' or 'no' ").lower()
                    break
                except:
                    print("Not an option!!!")
                    
            if raninput == 'yes':
                numGuessNum = random.randint(-50000,50000)
            elif raninput == 'no':
                while True:
                    try:
                        numGuessNum = int(input("Enter number: "))
                        break
                    except:
                        print("Not an option!!!")
            while True:
                try:
                    guessAmount = int(input("How many guesses would you like? "))
                    break
                except:
                    print("Not an option!!!")
            clearShell()
            while True:
                try:
                    NumGuessGameIn = int(input("Enter guess: "))
                    break
                except:
                    print("Not an option!!!")
            while NumGuessGameIn != numGuessNum:
                print("INCORRECT")
                guessAmount -= 1
                print(guessAmount, "guesses left!")
                while True:
                    try:
                        NumGuessGameIn = int(input("Enter guess: "))
                        break
                    except:
                        print("Not an option!!!")
            if NumGuessGameIn == numGuessNum:
                print("Good job! You won!")
                time.sleep(3.14)
            elif NumGuessGameIn != numGuessNum:
                print("Your out of guesses!\nSorry you lost")
        #Rock paper sisters
        elif gamein == 2:
            RPSComputer = random.choice(['Rock', 'Paper', 'Sister'])
            while True:
                try:
                    RPSUser = input("What would you like to use? ")
                    break
                except:
                    print("Not an option!!!")
            while RPSUser != 'rock' and RPSUser != 'paper' and RPSUser != 'sister' and RPSUser != 'cheat':
                print("Not an option!!!\nMake sure you spelled your option correctly!")
                while True:
                    try:
                        RPSUser = input("What would you like to use? ").lower()
                        break
                    except:
                        print("Not an option!!!")
            if RPSUser == 'cheat':
                print(RPSComputer)
                RPSUser = RPSComputer
            if RPSUser == RPSComputer:
                print("Good job!\nYou won!")
                time.sleep(2)
            elif RPSUser != RPSComputer:
                print("Sorry, you lost!")
                time.sleep(2)

    #math quiz
    def mathQuiz():
        print("Welcome to Math Quiz")
        time.sleep(2)
        mathQuizSelect = random.randint(1,3)
        if mathQuizSelect == 1:
            mathAwnser = 2
            while True:
                try:
                    mathUserAwnser = int(input("1+1\nWhat do you think the awnser is?\nAwnser: "))
                    break
                except:
                    print("Not an option!!!")
        elif mathQuizSelect == 2:
            mathAwnser = 15
            while True:
                try:
                    mathUserAwnser = int(input("Square root of 225\nWhat do you think the awnser is?\nAwnser: "))
                    break
                except:
                    print("Not an option!!!")
        elif mathQuizSelect == 3:
            mathAwnser = 21
            while True:
                try:
                    mathUserAwnser = int(input("7*3\nWhat do you think the awnser is?\nAwnser: "))
                    break
                except:
                    print("Not an option!!!")
        else:
            print("Error!!!")
        if mathUserAwnser == mathAwnser:
            print("Correct!!!")
            time.sleep(2)
        elif mathUserAwnser != mathAwnser:
            print("Incorrect!")
            time.sleep(2)
        else:
            print("error!!!")
        

    #memery wipe
    def memeryWipe():
        loading()
        sure = input("Are you sure you want to wipe this calculator's memery?\n(Y or N)").lower()
        if sure == 'y':
            try:
                with open(resource_path("responces.txt"), "w") as file:
                    file.write("")
                time.sleep(5)
                print("Memery is deleated (Gone for a really long time)")
                time.sleep(2)
            except:
                print("No memery found!")
                time.sleep(2)
        else:
            print("Memery not deleated!")
            time.sleep(2)

    #Time
    def date():
        import time
        print(time.strftime('todays date is %m-%d-%Y \nThe current time is %H:%M:%S'))
        import time
        time.sleep(2)

    #Weather forcast
    def weatherForcast():
        with open(resource_path("Weather.txt"), "r") as file:
            forcast = file.read().split("\n")
        weather = random.choice(forcast)
        print("Today's weather is", weather)
        time.sleep(2)

    def magic8ball():
        input("What is your yes/no question?")
        print(random.choice(['yes', 'no', 'mabey later', 'I see no in the futcher']))
        time.sleep(2)

    def ASCIIart():
        try:
            with open(("ASCIIart.txt"), "r", encoding="utf-8") as file:
                art_blocks = file.read().rsplit('---')  # Split by your delimiter
                art = random.choice(art_blocks)
                print(art.rstrip())  # Remove extra blank lines
                time.sleep(2)
        except FileNotFoundError:
            print("ASCIIart.txt not found!")
            time.sleep(2)

    def primeChecker(num1, num2):
        num1 = int(float(num1))
        if num1 <= 1:
            print("False")
            time.sleep(2)

        for i in range(2, num1):
            if num1 % i == 0:
                print("False")
                time.sleep(2)
        print("True")
        time.sleep(2)
        
    def jokes():
        while True:
            try:
                count = int(input("How many jokes would you like? "))
                break
            except:
                print("Please input a intager!!!")
                time.sleep(2)
                input("Press enter to continue...")
                time.sleep(2)
        while True:
            try:
                timesleepYes = input("Dou you want to press enter every joke? (Yes/No)").lower()
                break
            except:
                print("Not an option!!!")
                time.sleep(2)
                input("Press enter to continue...")
        if timesleepYes == 'yes':
            timesleep2 = False
        elif timesleepYes == 'no':
            while True:
                try:
                    timesleep = float(input("How many seconds would you like between each joke? "))
                    break
                except:
                    print("Not an option!!!")
                    time.sleep(2)
                    input("Press enter to continue...")
            timesleep2 = True
        try:
            with open(resource_path("jokes.txt"), "r", encoding="utf-8", errors="ignore") as file:
                joke = file.read().split("\n")
                count2 = 0
                while count2 < count:
                    ranJoke = random.choice(joke)
                    print(ranJoke)
                    if timesleep2:
                        time.sleep(timesleep)
                    if not timesleep2:
                        input("Press enter to continue...")
                    count2 += 1
        except FileNotFoundError:
            print("Error!")
        time.sleep(5)

    def signedIn():
        print(f"{username} is currently logged in!")
        time.sleep(2)

    #Diffrent operations to call(So I don't have lots of elifs)
    operations = {
        0: leave,
        1: add,
        2: subtract,
        3: multiply,
        4: devide,
        5: exponit,
        6: sqareRoot,
        7: remaneder,
        8: absuloteValue,
        9: powerOf10,
        10: squaredNumber,
        11: cubedNumber,
        12: persentageCalcultor,
        13: rond,
        14: roundDown,
        15: roundUp,
        16: log,
        17: log10,
        18: sin,
        19: cos,
        20: tan,
        21: factoral,
        22: gcd,
        23: lcm,
        24: root,
        25: asin,
        26: acos,
        27: atan,
        28: degrees,
        29: rosons,
        30: randomSayings,
        31: INtoCM,
        32: CMtoIN,
        33: MItoKM,
        34: KMtoMI,
        35: poundsToKilograms,
        36: kilogramsToPounds,
        37: FtoC,
        38: CtoF,
        39: randomNumberSettings,
        40: fullEQ,
        41: readHistory,
        42: games,
        43: mathQuiz,
        44: memeryWipe,
        45: date,
        46: weatherForcast,
        47: magic8ball,
        48: ASCIIart,
        49: primeChecker,
        50: jokes,
        51: signOut,
        52: signedIn,
        }

    #Start all operation counters at 0
    operation_count = {key: 0 for key in operations.keys()}

    #Imports that need reset each loop
    while True:
        import time

        #Verables that need reset each time
        num1NotNeeded = False
        num2Needed = True
        noNum = False
        num1 = 0
        num2 = 0
        
        clearShell()

        
        while True:
            
            #Ask for operation
            for key, func in operations.items():
                name = operationNames.get(key, "Unknown operation")
                print(f"Press {key} for {operationNames[key]}")
                time.sleep(.25)
            choice = int(input("Selection: "))
            break
            '''except:
                print("Not an option!!!")
                time.sleep(2)
                input("Press ENTER to continue....")
                count = 0
                while count < 100:
                    print("\n")
                    count += 1'''

        #Only ask for numbers if there needed
        num2Needed = choice in(1,2,3,4,5,7,12,22,23,24,42,52)
        num1NotNeeded = not choice in(0,30,39,40,45,46,47,48,50,52)

        #Make sure you enter proper number and ask for random numbers
        if choice <= 53:
            if choice != 0 and choice != 30 and choice != 39 and choice != 41 and choice != 42 and choice != 43 and choice != 44 and choice != 45 and choice != 46 and choice != 47 and choice != 48 and choice != 50 and choice != 51 and choice != 52:
                if codeLooped == True:
                    while True:
                        try:
                            sameNums = input("Do you want to use the same numbers as last time? ").lower()
                            break
                        except:
                            print("Not an option!!!")
                    if sameNums == 'yes' or sameNums == 'no':
                        if sameNums == 'no':
                            while True:
                                try:
                                    randomNumberChoice = int(input("Select 1 for your own numbers and 2 for random numbers: "))
                                    break
                                except:
                                    print("Not an option!!!")
                            noNum = True
                        elif sameNums == 'yes':
                            print("Ok")
                            num1 = num1Same
                            num2 = num2Same
                    else:
                        print("Not an option!!!")
                        
                        
                else:
                    while True:
                        try:
                            randomNumberChoice = int(input("Select 1 for your own numbers and 2 for random numbers: "))
                            noNum = True
                            break
                        except:
                            print("Not an option!!!")
                            time.sleep(2)
                            input("Press enter to continue...")
        else:
            clearShell()
            print("Not an option!!!")
            time.sleep(5)
            countdownToSelection()

        #Ask for numbers
        if choice <= 53:
            if noNum == True:
                def numberChoice(randomNumberChoice):
                    global num1, num2
                    if randomNumberChoice == 1:
                        if num1NotNeeded:
                            while True:
                                try:
                                    num1 = float(input("Enter your first number: "))
                                    break
                                except:
                                    print("Not an awnser!!!")
                        if num2Needed:
                            while True:
                                try:
                                    num2 = float(input("Enter your second number: "))
                                    break
                                except:
                                    print("Not an option!!!")
                    elif randomNumberChoice == 2:
                        num1 = random.randint(-500,500)
                        num2 = random.randint(-500,500)

            if noNum == True:
                numberChoice(randomNumberChoice)

            #Do operation that user chooses
            operation = operations.get(choice)

            # Only call with numbers if needed
            if choice in (1,2,3,4,5,7,12,22,23,24):  # operations that need two numbers
                total = operations[choice](num1, num2)
            elif choice in (6,8,9,10,11,13,14,15,16,17,18,19,20,21,25,26,27,28,29,31,32,33,34,35,36,37,38,40,49):
                total = operations[choice](num1)  # operations that need one number
            else:
                total = operations[choice]()  # operations that need no numbers

                operation_count[choice] += 1
            

            #Only clear screen if needed
            if choice not in (30,46,45,44,43,42,47,48,49,50,51,52):
                clearShell()

            #Only ask if want to round/format and print total if needed
            if choice not in(0,30,39,41,42,43,44,45,46,47,48,49,50,51,52):
                total = roufor(total)
                print(total)

                #Only save to history file if needed
                if choice != 40 and choice != 46:
                    saveResult(num1, num2, operationNames.get(choice, "Unknown Operation"), total)
            if choice == 51:
                break
            
            #Save everything to dev history file
            devSaveResult(num1, num2, choice, total)

            #Only count down if not viewing history
            if choice != 41 and choice != 51:
                time.sleep(5)
                countdownToSelection()

            #Define ending veriables
            num1Same = num1
            num2Same = num2
            codeLooped = True
