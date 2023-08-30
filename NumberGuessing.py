import random

attempts_list = []

def show_score():
    if not attempts_list:
        print('there is currently no high score,'
              'it\'s yours for the taking!')
    else:
        print(f'The current high score is'
              f'{min(attempts_list)}attempts')

def start_game():
    attempts=0
    rand_num=random.randint(1, 10)
    print('hello traveler! welcome to the game of guesses!')
    player_name=input('what is your name')
    wanna_play=input(
        f'Hi,{player_name}, would you like to play'
        f'the guessing game?(Enter Yes/No):')
    if wanna_play.lower() !='yes':
        print('That\'s cool, thanks!')
    else:
        show_score()
    while wanna_play.lower()=='yes':
        try:
            guess=int(input('pick a number between 1 and 10:'))
            if guess<1 or guess>10:
                raise ValueError(
                    'Please guess a number within the given range')
            attempts +=1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('nice you got it!')
                print(f'It took you{attempts} attempts')
                wanna_play=input(
                    'would you like to play again? (Enter Yes/No):')
                if wanna_play.lower() !='yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts=0
                    rand_num=random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess>rand_num:
                    print('It\'s lower')
                elif guess<rand_num:
                    print('it"s higher')
        except ValueError as err:
            print('oh no!, that is not a valid value. Try again...')
            print(err)

start_game()

# if __name__ =='_main_':
#     start_game()