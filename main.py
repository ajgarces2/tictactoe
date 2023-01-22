
#import game modueles
import pygame, sys

pygame.init() #initialize
 
#create game parameters and set images
WIDTH, HEIGHT = 900, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")
BOARD = pygame.image.load("images/Board.png")
X_IMG = pygame.image.load("images/X2.png")
O_IMG = pygame.image.load("images/O3.png")
O_WIN= pygame.image.load("images/owin.png")
X_WIN= pygame.image.load("images/xwin.png")
DRAW = pygame.image.load("images/draw.png")
BLIND= pygame.image.load("images/blind.png")
BG_COLOR = (213, 239, 245)

#drawing
SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))

#create game board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
#next move
to_move = 'X'


pygame.display.update()

#creating playing board
def render_board(board, ximg, oimg):
    global graphical_board  
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                #create object image and boxes
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

#place x or o
def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2
    if board[round(converted_y)][round(converted_x)] != 'O' and board[round(converted_y)][round(converted_x)] != 'X':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
            pygame.display.set_caption("It is X's turn!!")
        else:
            to_move = 'O'
            pygame.display.set_caption("It is O's turn!!")
    
    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
    
    return board, to_move

game_finished = False

#check for winner
def check_win(board):
    global winner
    winner = None
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            for i in range(0, 3):
                graphical_board[row][i][0] = pygame.image.load(f"images/Winning{winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            #print(winner)
            return winner

    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner =  board[0][col]
            for i in range(0, 3):
                graphical_board[i][col][0] = pygame.image.load(f"images/Winning{winner}.png")
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            #print(winner)
            return winner
   
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner =  board[0][0]
        graphical_board[0][0][0] = pygame.image.load(f"images/Winning{winner}.png")
        SCREEN.blit(graphical_board[0][0][0], graphical_board[0][0][1])
        graphical_board[1][1][0] = pygame.image.load(f"images/Winning{winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][2][0] = pygame.image.load(f"images/Winning{winner}.png")
        SCREEN.blit(graphical_board[2][2][0], graphical_board[2][2][1])
        pygame.display.update()
        #print(winner)
        return winner
          
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner =  board[0][2]
        graphical_board[0][2][0] = pygame.image.load(f"images/Winning{winner}.png")
        SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
        graphical_board[1][1][0] = pygame.image.load(f"images/Winning{winner}.png")
        SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
        graphical_board[2][0][0] = pygame.image.load(f"images/Winning{winner}.png")
        SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
        pygame.display.update()
        #print(winner)
        return winner
    
    #draw in case no one wins
    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    return None
        return "DRAW"

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, to_move = add_XO(board, graphical_board, to_move)

            if game_finished:
                board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                graphical_board = [[[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]]]

                to_move = 'X'

                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))

                game_finished = False

                pygame.display.update()
            
            if check_win(board) is not None:
                game_finished = True
                if (winner == 'O'):
                    SCREEN.blit(BLIND,(0,0))
                    SCREEN.blit(O_WIN,(0,0))
                    pygame.display.set_caption("O has won!")
                elif(winner == 'X'):
                    SCREEN.blit(BLIND,(0,0))
                    SCREEN.blit(X_WIN,(0,0))
                    pygame.display.set_caption("X has won!")
                else:
                    SCREEN.blit(BLIND,(0,0))
                    SCREEN.blit(DRAW,(0,0))
                    pygame.display.set_caption("Draw!")

            
            pygame.display.update()
