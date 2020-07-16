import random
from string import ascii_lowercase, ascii_letters


# Write your code here
def validate_ascii_chars(user_char):
    if len(user_char) != 1:
        print('You should input a single letter')
        return False
    elif user_char not in ascii_letters or user_char not in ascii_lowercase:
        print('It is not an ASCII lowercase letter')
        return False
    else:
        print('No such letter in the word')
        return True


list_choice = ('python', 'java', 'kotlin', 'javascript')
print('H A N G M A N')
computer_choice = random.choice(list_choice)
guessword = '-' * len(computer_choice)
temp = set()
fail_case = set()
fail_counter = 1
run = True
while run:
    play = input('Type "play" to play the game, "exit" to quit:')
    if play == 'play':

        while fail_counter <= 8 and guessword != computer_choice:
            print('\n{}'.format(guessword))
            user_choice = input("Input a letter:")
            guessword_temp = ''
            if (user_choice in computer_choice and user_choice in temp) or (user_choice in fail_case):
                print('You already typed this letter')
                continue
            elif user_choice == '':
                validate_ascii_chars(user_choice)
            elif user_choice not in computer_choice:
                if validate_ascii_chars(user_choice):
                    fail_counter += 1
                    fail_case.add(user_choice)
                continue
            elif user_choice in computer_choice:
                temp.add(user_choice)
                for char in computer_choice:
                    if char in temp:
                        guessword_temp += char
                        continue
                    guessword_temp += '-'
                guessword = guessword_temp

        if guessword == computer_choice:
            print("You guessed the word {}!\nYou survived!\n".format(guessword))
        else:
            print("You are hanged!\n")
    else:
        print('exit')
        run = False
        exit(0)
