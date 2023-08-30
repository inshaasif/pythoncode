import random
import os
import re
def check_play_status():
    valid_responses=['yes', 'no']
    while True:
        try:
            response=input('Do you wish to play again?(yes or no):')
            if response.lower() not in valid_responses:
                raise ValueError('yes or no only')
            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('thanks for playing!')
                exit()
        except ValueError as err:
            print(err)

def play_rps():
    play=True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, paper, scissors - shoot!')

        user_choice=input('choose your weapon'
                          '[R]ock, [p]aper or [s]cissors:')
        if not re.match("[SsRrPp]", user_choice):
            print('please choose a letter')
            print('[R]ock, [P]aper or [S]cissor')
            continue
        print(f'You chose: {user_choice}')
        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)
        print(f'I chose: {opp_choice}')
        if opp_choice == user_choice.upper():
             print('Tie!')
             play = check_play_status()
        elif opp_choice == 'R' and user_choice.upper() == 'S':
             print('Rock beats scissors, I win!')
             play = check_play_status()
        elif opp_choice == 'S' and user_choice.upper() == 'P':
             print('Scissors beats paper! I win!')
             play = check_play_status()
        elif opp_choice == 'P' and user_choice.upper() == 'R':
             print('Paper beats rock, I win!')
             play = check_play_status()
        else:
             print('You win!\n')
             play = check_play_status()
                         
play_rps()