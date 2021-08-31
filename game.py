import random

def guess():
    num = input("Your guess? - ")
    return int(num)

def guess_eval(correct_num, local_guess):
    if local_guess == correct_num:
        return True, "Correct"
    elif local_guess > correct_num:
        return False, "Your guess is too high, try again."
    else:
        return False, "Your guess is too low, try again."

def main(min, max):
    name = input("Whaddup, homeslice! What's your name dawg?\nType name here: ")
    tries = 0
    correct = False

    print("{name}, I'm thinking of a number between {min} and {max}.".format(name = name, min = min, max = max))

    correct_num = random.randint(min, max)


    while correct == False:
        current_guess = guess()
        tries += 1

        current_guess_eval = guess_eval(correct_num, current_guess)
        
        if current_guess_eval[0] == True:
            print("Well done, {name}! You found my number in {tries} tries!".format(name = name, tries = str(tries)))
            correct = True
        else:
            print(current_guess_eval[1])


main(1, 100)
