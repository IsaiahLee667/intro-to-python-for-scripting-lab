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
    
    

     


#checkLetter()
#checkVotingEligibility()
#calculateDogYears()
#weatherAdvice()

