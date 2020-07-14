import random
# Write your code here
user_choice = input()
list_choice = ('python', 'java', 'kotlin', 'javascript')
computer_choice = random.choice(list_choice)
if user_choice == computer_choice:
    print('You survived!')
else:
    print('You are hanged!')