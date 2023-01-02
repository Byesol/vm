import time
import pygame
import random
import os

pygame.init()

width = 300
hight = 400
red = (255, 50, 50)
WHITE = (255, 255, 255)
black = (0, 0, 0)

computer = True
player = False

screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption("tic tac toe")

font = pygame.font.SysFont('timesnewroman', 40)
font2 = pygame.font.SysFont('timesnewroman', 20)
text_x = font.render('X', True, red)
text_o = font.render('O', True, red)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

clock = pygame.time.Clock()

win_image = pygame.image.load(os.path.join(assets_path, 'win1.png'))
lose_image = pygame.image.load(os.path.join(assets_path, 'lose1.png'))
tie_image = pygame.image.load(os.path.join(assets_path, 'tie.png'))


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)

    pygame.draw.line(screen, red, [100, 0], [100, 300], 5)
    pygame.draw.line(screen, red, [200, 0], [200, 300], 5)
    pygame.draw.line(screen, red, [0, 100], [300, 100], 5)
    pygame.draw.line(screen, red, [0, 200], [300, 200], 5)
    pygame.draw.line(screen, red, [0, 300], [300, 300], 5)

    if board[0] == 'X':
        screen.blit(text_x, [30, 30])
    elif board[0] == 'O':
        screen.blit(text_o, [30, 30])
    if board[1] == 'X':
        screen.blit(text_x, [30, 130])
    elif board[1] == 'O':
        screen.blit(text_o, [30, 130])
    if board[2] == 'X':
        screen.blit(text_x, [30, 230])
    elif board[2] == 'O':
        screen.blit(text_o, [30, 230])
    if board[3] == 'X':
        screen.blit(text_x, [130, 30])
    elif board[3] == 'O':
        screen.blit(text_o, [130, 30])
    if board[4] == 'X':
        screen.blit(text_x, [130, 130])
    elif board[4] == 'O':
        screen.blit(text_o, [130, 130])
    if board[5] == 'X':
        screen.blit(text_x, [130, 230])
    elif board[5] == 'O':
        screen.blit(text_o, [130, 230])
    if board[6] == 'X':
        screen.blit(text_x, [230, 30])
    elif board[6] == 'O':
        screen.blit(text_o, [230, 30])
    if board[7] == 'X':
        screen.blit(text_x, [230, 130])
    elif board[7] == 'O':
        screen.blit(text_o, [230, 130])
    if board[8] == 'X':
        screen.blit(text_x, [230, 230])
    elif board[8] == 'O':
        screen.blit(text_o, [230, 230])


def PlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    if random.randint(0, 1) == 0:
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board = board[:move] + letter +board[move+1:]


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or  # across the top
            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle
            (bo[0] == le and bo[1] == le and bo[2] == le) or  # across the bottom
            (bo[6] == le and bo[3] == le and bo[0] == le) or  # down the left side
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the middle
            # down the right side
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[6] == le and bo[4] == le and bo[2] == le) or  # diagonal
            (bo[8] == le and bo[4] == le and bo[0] == le))  # diagonal


def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == '*'


def getPlayerMove(board):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe computer:
    # First, check if we can win in the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(0, 9):
        if isSpaceFree(board, i):
            return False
    return True


def usermove(board):  # takes a mouse move ,

    pygame.event.get()
    x, y = pygame.mouse.get_pos()
    move = ' '

    if (x < 100):
        col = 1
        if y < 100:
            row = 1
            move = 0
        elif y < 200:

            move = 1
        elif y < 300:
            move = 2
    elif (x < 200):
        if y < 100:
            row = 1
            move = 3
        elif y < 200:

            move = 4
        elif y < 300:
            move = 5
    elif x < 300:
        col = 3
        if y < 100:
            row = 1
            move = 6
        elif y < 200:
            move = 7
            move = 7
        elif y < 300:
            move = 8
    else:
        move = -1

    for x in find_empty(board):
        if move == x:
            return move
    


def is_end(board: str) -> bool:
    return isWinner(board, computerLetter) or isWinner(board, playerLetter)


def find_empty(board: str) -> tuple[int, ...]:

    return tuple(x for x, cell in enumerate(board) if cell == '*')







def minimax(board, depth, maxplayer):
    move = -1
    if depth == 0 or isBoardFull(board) or is_end(board):
        return -1, evaluate(board)
    if maxplayer == computer:
        value = float('-inf')
        for each in find_empty(board):
            dum, score = minimax(board[: each] + computerLetter + board[each + 1:], depth - 1, player)
            if score > value:
                value = score
                move = each
            if score == 1:
                break
    else:
        value = float('inf')
        for each in find_empty(board):
            dum, score = minimax(
                board[: each] + playerLetter + board[each + 1:], depth - 1, computer)
            if score < value:
                value = score
                move = each
            if score == -1:
                break
    return move, value



def evaluate(board):
    if isWinner(board, computerLetter):
        score = 1
    elif isWinner(board, playerLetter):
        score = -1
    else:
        score = 0
    return score


def start_s():
    screen.fill(WHITE)
    text_win = font2.render('Press x or y to chosse your letter', True, black)
    screen.blit(text_win, [16, 130])
    
    pygame.display.flip()

    beg = True
    while beg:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsPlaying = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    
                    beg = False
                    return 'X'
                    
                elif event.key == pygame.K_o:
                    beg = False
                    return 'O'                      


gameIsPlaying = True



begin= True

while gameIsPlaying:
    screen.fill(WHITE)
    begin= True
    pygame.display.flip()
    theBoard = '*' * 9 
    turn = whoGoesFirst()
    g2 = True
    if begin == True:
        playerLetter = start_s()
        if playerLetter == "O":
            computerLetter = "X"
        else:
            computerLetter = "O"
        #print(playerLetter, computerLetter)
        begin = False
    # Reset the board
    screen.fill(WHITE)
    pygame.display.flip()
    
    
   
    


    while g2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsPlaying = False
            if turn == 'player':
                drawBoard(theBoard)
                pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    move = usermove(theBoard)
                    print(move)
                    if move != None:

                        
                        print('\n')
                        theBoard = theBoard[:move] + playerLetter +theBoard[move+1:]
                        #makeMove(theBoard, playerLetter, move)
                        
                        print(theBoard)
                        drawBoard(theBoard)
                        pygame.display.flip()

                        if isWinner(theBoard, playerLetter):
                            drawBoard(theBoard)
                            print('You  won !')
                            screen.fill(WHITE)

                            text_win = font2.render('You won ', True, red)
                            screen.blit(text_win, [30, 300])
                            pygame.display.flip()
                            g2 = False
                        else:
                            if isBoardFull(theBoard):
                                drawBoard(theBoard)
                                print('game tie')
                                screen.fill(WHITE)
                                text_tie = font2.render('game tie', True, red)
                                screen.blit(text_tie, [30, 300])
                                
                                screen.blit(tie_image, [50, 50])
                                pygame.display.flip()
                                g2 = False
                            else:
                                turn = 'computer'

            else:
                # Computer's turn.
                pygame.time.delay(1000)

                move, _ = minimax(theBoard, 9, computer)
                print(move)
                theBoard = theBoard[:move] + computerLetter +theBoard[move+1:]
                #makeMove(theBoard, computerLetter, move)
                
                if isWinner(theBoard, computerLetter):

                    drawBoard(theBoard)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    print('The computer has beaten you! You lose.')
                    screen.fill(WHITE)
                    text_lose = font2.render('You lose!', True, red)
                    screen.blit(text_lose, [30, 300])
                    screen.blit(lose_image, [50, 50])
                    pygame.display.flip()
                    g2 = False
                    # pygame.time.delay(3000)
                    # gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('game tie')
                        screen.fill(WHITE)
                        text_tie = font2.render('game tie', True, red)
                        screen.blit(text_tie, [30, 300])
                        
                        screen.blit(tie_image, [50, 50])
                        pygame.display.flip()
                        g2 = False
                    else:
                        turn = 'player'

        # 초당 60 프레임으로 업데이트

    pygame.time.delay(2000)

    #gameIsPlaying = False
    pygame.display.flip()  # = 240 pixels / second
    # 게임 종료
    clock.tick(60)  # 60 frames per second
    # ball_dx = 4
    # ball_velocity_x = 4 pixels / 1 frame * 60 (frames / second)
pygame.quit()
