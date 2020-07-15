import random
# Write your code here
list_choice = ('python', 'java', 'kotlin', 'javascript')
computer_choice = random.choice(list_choice)
guessword = str(computer_choice[:3]).ljust(len(computer_choice), '-')
print('H A N G M A N\nGuess the word {}:'.format(guessword))
user_choice = input()
if user_choice == computer_choice:
    print('You survived!')
else:
    print('You are hanged!')