import random
import sys

def random_win(excluded, low, high):
    number = random.randint(low, high)
    while number == excluded:
        number = random.randint(low, high)
    return number


def random_win(excluded, low, high):
    number = random.randint(low, high)
    while number == excluded:
        number = random.randint(low, high)
    return number


def quit_game():
    print('Game Over')
    sys.exit()


def update_distance(): 
    global distance, distance_x, distance_y
    distance_x = abs(x - win_x)
    distance_y = abs(y - win_y)
    distance = distance_x + distance_y        


direction_dictionary = {0 : "FINISH", 1 : "Boiling. You're one tile from the goal!", 2 : 'Melting', 3 : 'Melting', 4 : 'Burning', 5 : 'Burning', 6 : 'Hot', 7 : 'Hot', 8 : 'Warm', 9 : 'Warm', 10 : 'Nuetral', 11 : 'Cool', 12 : 'Cool', 13 : 'Chilly', 14 : 'Chilly',
 15 : 'Cold', 16 : 'Cold', 17: 'Freezing', 18: 'Freezing', 19 : 'Absolute Zero. Wow, you are as far away as possible', 20 : 'Absolute Zero. Wow, you are as far away as possible'}


def startg():
    print('''
You are in a 10x10 grid at a random point. Your goal is to get to another randomly generated finish point. You will be told how close you are and where you are every time you move. Type start to begin the game.
          ''')
    while True:
        starting_help = input('>').lower().strip()
        if starting_help == 'start':
            start()
        if starting_help == 'quit':
            quit_game()
        else:
            print('Use start to begin, or quit to end.')


def start():
    print('''
           Controls:
           Right - Positive move on x axis
           Left - Negative move on y axis
           Up - Positive move on y axis
           Down - Negative move on y axis
           Quit - End Game
          
           Type go to begin.
                                        ''')
    startgame = input('>').lower().strip()
    if startgame == "quit":
        quit_game()
    elif startgame == 'go':
        print(f'''
\033[1mThe Game Has Started.\033[0m
              

               
{direction_dictionary[distance]}              
You are at {x}, {y}.
              ''')
        decision_maker()
    else:
        print('Start the game or quit.')
        start()


def decision_maker():
    if (win_x, win_y) == (x, y):
        print('You made it! You win.')
        sys.exit()
    choice = input('>')
    movement(choice.lower())
    

def movement(direction):
    global x, y, distance_last
    distance_last = distance
    if direction == 'right':
        if x == 10:
            border('right')
        else:
            x += 1
    elif direction == 'left':
        if x == 0:
            border('left')
        else:
            x -= 1
    elif direction == 'up':
        if y == 10:
            border('up')
        else:
            y += 1
    elif direction == 'down':
        if y == 0:
            border('down')
        else:
            y -= 1
    elif direction == 'quit':
        quit_game()
    else:
        print('''
              Only controls are Right, Left, Up, Down, and Quit''')
        decision_maker()
    update_distance()
    if distance_last > distance:
        print('''
              
              \033[91mWarmer +\033[0m''')
    else:
        print('''
              
              \033[96mColder -\033[0m''')
    print(f'''


{direction_dictionary[distance]}
You are now at {x}, {y}
         ''')
    decision_maker()


def border(direction):
        if direction == 'right':
            print(f'You have gone to far {direction}. You are still at {x}, {y}')
        elif direction == 'left':
            print(f'You have gone to far {direction}. You are still at {x}, {y}')
        elif direction == 'up':
            print(f'You have gone to far {direction}. You are still at {x}, {y}')
        elif direction == 'down':
            print(f'You have gone to far {direction}. You are still at {x}, {y}')
        else:
            print('Only controls are Right, Left, Up, and Down')
        decision_maker()


x = random.randint(0, 10)
y = random.randint(0, 10)
win_x = random_win(x, 0, 10)
win_y = random_win(y, 0, 10)


update_distance()
startg()