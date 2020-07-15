import random
# Write your code here

list_choice = ('python', 'java', 'kotlin', 'javascript')
print('H A N G M A N')
computer_choice = random.choice(list_choice)
guessword = '-' * len(computer_choice)
temp = set()
fail_case = set()
fail_counter = 1

while fail_counter <= 8 and guessword != computer_choice:
    print('\n{}'.format(guessword))
    user_choice = input("Input a letter: ")
    guessword_temp = ''
    if (user_choice in fail_case) or (user_choice not in fail_case and user_choice in temp):
        print('No improvements')
        fail_counter += 1
        fail_case.add(user_choice)
        continue
    elif user_choice not in computer_choice:
        print('No such letter in the word')
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
    print("\n{}\nYou guessed the word!\nYou survived!".format(guessword))
else:
    print("You are hanged!")
