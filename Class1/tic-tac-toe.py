import random

### ---Person 1: X
# Pick an empty spot, randomly in location 1-8
# Place your X

### ---Person 2: 0
# Pick an empty spot
# Place your 0 in that location

### ---Person 1: X

### Commonality:
# Find an empty spot
# Pick a random location

### Stopping criteria to end game: no more empty spot of if someone win
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def exit_condition(theBoard):
    if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
        return True
    elif theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
        return True
    elif theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
        return True
    elif theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X':
        return True
    elif theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X':
        return True
    elif theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X':
        return True
    elif theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X':
        return True
    elif theBoard['top-R'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-L'] == 'X':
        return True

    elif theBoard['top-L'] == '0' and theBoard['top-M'] == '0' and theBoard['top-R'] == '0':
        return True
    elif theBoard['mid-L'] == '0' and theBoard['mid-M'] == '0' and theBoard['mid-R'] == '0':
        return True
    elif theBoard['low-L'] == '0' and theBoard['low-M'] == '0' and theBoard['low-R'] == '0':
        return True
    elif theBoard['top-L'] == '0' and theBoard['mid-M'] == '0' and theBoard['low-R'] == '0':
        return True
    elif theBoard['top-L'] == '0' and theBoard['mid-L'] == '0' and theBoard['low-L'] == '0':
        return True
    elif theBoard['top-M'] == '0' and theBoard['mid-M'] == '0' and theBoard['low-M'] == '0':
        return True
    elif theBoard['top-R'] == '0' and theBoard['mid-R'] == '0' and theBoard['low-R'] == '0':
        return True
    elif theBoard['top-R'] == '0' and theBoard['mid-M'] == '0' and theBoard['low-L'] == '0':
        return True
    else:
        return False

def game():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print(theBoard)
    play = list(theBoard.keys())
    random.shuffle(play)
    print(play)

    turn = 'X'
    for i in range(len(play)):
        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')

        theBoard[play[i]] = turn
        if exit_condition(theBoard):
            print('Congrats! ' +turn+ ' won!')
            break

        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'

    printBoard(theBoard)

if __name__ == "__main__":
    game()
