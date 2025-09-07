#Using the same concept as what we did for the hello python, Im sure there's a way to extract 3 variables from one string, but i'd rather not just spam copilot/gpt a million times and feel like im "learning"
#Had to lookup float, used to indicate to python, this is a float/number or at the very least not a string, else it will think we are multiplying words. Sincei ts a float it will take numbers with decimal values.
firstNumber = float(input("Type a number as an input "))
signal = input("Type one of these 4 symbols: *,/,+ or -  ")
secondNumber = float(input("Type a second number as an input "))

#Remember we need to denotate that it is a value and not an actual + for scripting, hence the quotes, 
# same idea for double equals instead of a single one to indicate a comparison instead of assigning a value like in the top 3 lines.  Also single quotes would work here as well.
if signal == "+":
    result = firstNumber + secondNumber
# continuing the other 3 symbols using a slew of else ifs.
elif signal == '=':
    result = firstNumber - secondNumber

elif signal == '*':
    result = firstNumber * secondNumber

#Has error if 2nd number is 0
elif signal == '/':
    result = firstNumber /secondNumber


        

print(f"The final result is: {result}")