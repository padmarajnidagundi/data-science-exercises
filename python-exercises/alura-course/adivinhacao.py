print("********************")
print("Welcome to the game!")
print("********************")

# Setting the secret
secret_number = 42
number_of_tries = 5
winner = 0

while number_of_tries > 0:
    # User input
    guess_str = input("Type a number: ")
    guess_int = int(guess_str)

    compare = (guess_int == secret_number)

    if compare:
        print("You won!")
        number_of_tries = 0
        winner = 1
    else:
        if (guess_int > secret_number):
            print("You lost! Your guess ({}) was greater than the secret".format(guess_str))
        elif (guess_int < secret_number):
            print("You lost! Your guess ({}) was less than the secret".format(guess_str))
        
        try_number = number_of_tries - 1
        try_number_str = str(try_number)

        if number_of_tries == 2:
            print("You still have {} try.".format(try_number_str))  
        elif number_of_tries != 1:
            print("You still have {} tries.".format(try_number_str))
        else:
            pass
        
        number_of_tries -= 1

if number_of_tries == 0 and winner != 1:
    print("You are out of tries.")
else:
    pass

print("End of game.")
print("************")
