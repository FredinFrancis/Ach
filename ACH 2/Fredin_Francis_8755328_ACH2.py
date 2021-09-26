print("Welcome !")

print("Program to Change Input Character to Upper Case/Lower Case") # Welcome message

l=str(input("Enter a character:  "))

if((l >= 'a' and l <= 'z') or( l >= 'A' and l <='Z')):   
    # Check whether the entered input is character or not. If yes, if statement executes
    
    if(l == str.lower(l)): # Checking the input is lower/upper case

        print("The output is: " + str.upper(l)) # If the input is lower case, outputs upper case

    elif(l == str.upper(l)): # Checking the input is lower/upper case

        print("The output is: " + str.lower(l)) # If the input is upper case, outputs lower case
    
else:   # As the input is not valid, this else statement is executed
    print(" Sorry ! Please enter a character.")



