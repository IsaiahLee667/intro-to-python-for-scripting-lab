#Defining methods to be run 

#Definetly some google and gpt for reseaching 
def checkLetter():
    #.lower is a built in method that converts it to lowercase in case it was capitalized
    letter = input("Enter in a letter here and I will tell you if it is a vowel or consonant:").lower()
    if letter.isalpha():
        if letter in 'aeiou':
            print ("You entered in a vowel")
        else:
            print ("You entered in a consonant")
    else: 
        print("This is not a letter")

def checkVotingEligibility():
    #Originally had issues when this is not a float/int and did what i did in calculator and just started as an int, but .isDigit only works if the value is a string 
    #so keeping it string here and converting it later to an int
    age = input("Please enter your age: ")
    votingAge = 18
    #Converting to an int here for comparison purposes.
    if age.isdigit():
        intAge = int(age)
        if intAge >= votingAge:
            print("You are of voting age, go vote!")
        else:
            print(f"You are not of voting age, the age to vote is : {votingAge}")
    else:
        print("This is not a number/value I can use to check your age with, please try again.")
    

def calculateDogYears():
    age = float(input("Input a dog's age: "))
    if age <= 2:
        dogAge = age * 10
        print(f"Your dog is {dogAge} years old.")
    if age > 2:
        #this formula is hardcoded is hell and im sure there's something more elegant to do here, but screw it.
        dogAge = ((age - 2) * 7) + 20
        print(f"Your dog is {dogAge} years old.")


def weatherAdvice():
    temp = input("Is it cold? Answer as either yes or no: ").lower()
    if temp == "yes":
        isCold = True
    else:
        isCold = False
    rain = input("Is it raining? Answer as either yes or no: ").lower()
    if rain == "yes":
        isRaining = True
    else:
        isRaining = False
    if isRaining == True and isCold == True:
        print("Wear a rainproof coat.")
    if isRaining == True and isCold == False:
        print ("Carry an umbrella.")
    if isRaining == False and isCold == True:
        print ("Wear a warm coat.")
    if isRaining == False and isCold == False:
        print ("Wear light clothing.")

def determineSeason():
    #Defining a list of months for the sake of the month input
    validMonthValues = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    #Similar to .lower, a method of ensuring data is entered in a more standardized fashion for comparisons sake.  
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    #Not is a way to check if a value is in a given list/tuple.
    if month not in validMonthValues:
        print ("The entered month is not a valid month, please enter as the first 3 letters of the month")
        #Method/command to essentially start over/start again
        return
         
      
    #Try is for a Try-Except block, which is best for handling our exception errors in more graceful fashion
    #I suppose we could have also done a list from [1,2,3,4....,31] and then just done the if check for if it was in the listed value but that seems excessive
    try: 
        day = int(input("Enter the day of the month: "))    
        if day < 1 or day > 31:
            print("Invalid day, must be within a possible day of a month")
            return
        if month == "Feb" and day > 29:
            print("Invalid day, Feburary has at most, 29 days even including leap years")
            return
    #Except is a way of handling exceptions in a custom manner or at least in a way besides crashing/more on our terms, like giving a more custom message on what/how an error was triggered.
    #ValueError is an exception when it is given a value not expected, in this case, day is defined as an int but we give it say a string/letters. Would also trigger for things outside an int boundary, like decimals.
    except ValueError:
        print("Day must be a number")
        return
    

    # Determine season
    if (month == "Dec" and day >= 21) or month in ("Jan", "Feb") or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ("Apr", "May") or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ("Jul", "Aug") or (month == "Sep" and day <= 21):
        season = "Summer"
    elif (month == "Sep" and day >= 22) or month in ("Oct", "Nov") or (month == "Dec" and day <= 20):
        season = "Fall"
    else:
        season = "Unknown"

    # Output result
    print(f"{month} {day} is in {season}.")

#Sidenote, this lesson was a real reminder that python really cares about colons as its form of period.


#checkLetter()
#checkVotingEligibility()
#calculateDogYears()
#weatherAdvice()
determineSeason()

