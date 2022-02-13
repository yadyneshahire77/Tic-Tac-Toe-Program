#TIC TAC TOE Programme
import random
def display_board(board):
  print (' | |')
  print (' ', board[7], '| ', board[8], '| ', board[9])
  print( '----|----|----')
  print(' ', board[4], '| ', board[5], '| ', board[6])
  print( '----|----|----')
  print( ' ', board[1], '| ', board[2], '| ', board[3])
  print (' | |')
def player_input():
  marker = ' '
  while not (marker == 'X' or marker == 'O'):
    marker = input('player1: Do you want to be X or O ? ').upper()
    if marker == 'X':
     return ('X', 'O')
    else:
     return ('O', 'X')
def place_marker(board, marker, position):
  board[position] = marker
def win_check(board, mark):
  if ((board[7] == mark and board[8] == mark and board[9] == mark) or
     (board[4] == mark and board[5] == mark and board[6] == mark) or
     (board[1] == mark and board[2] == mark and board[3] == mark) or
     (board[1] == mark and board[5] == mark and board[9] == mark) or
     (board[7] == mark and board[5] == mark and board[3] == mark) or
     (board[1] == mark and board[4] == mark and board[7] == mark) or
     (board[2] == mark and board[5] == mark and board[8] == mark) or
     (board[3] == mark and board[6] == mark and board[9] == mark)):
   return True
  else:
   return False

def win_check(board, mark):
  if ((board[7] == board[8] == board[9] == mark) or
     (board[4] == board[5] == board[6] == mark) or
     (board[1] == board[2] == board[3] == mark) or
     (board[1] == board[5] == board[9] == mark) or
     (board[7] == board[5] == board[3] == mark) or
     (board[1] == board[4] == board[7] == mark) or
     (board[2] == board[5] == board[8] == mark) or
     (board[3] == board[6] == board[9] == mark)):
   return True
  else:
   return False

def choose_first():
  if random.randint(0, 1) == 1:
   return 'Player 1'
  else:
   return 'Player 2'
def space_check(board, position):
  return board[position] == ' '
#space_check function tells us there is a empty space on the board
def full_board_check(board):
  for i in range(1, 10):
    if space_check(board, i):
     return False
  else:
   return True
def player_choice(board):
   position = ' '
   while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
     position = input('Choose a position (1-9): ')
   return int(position)
def replay():
  return input('Do you wanna play again? y/n').upper().startswith('Y')
print('Welcome to TICTACTOE!')
while True:
  theBoard = [' '] * 10
  display_board(theBoard)
  player1_marker, player2_marker = player_input() #('X','O'),('O','X')
  turn = choose_first()
  print(turn + " will go first")
  game_on = True
  while game_on:
    if turn == 'Player 1':
       display_board(theBoard)
       position = player_choice(theBoard)
       place_marker(theBoard, player1_marker, position)
       if win_check(theBoard, player1_marker):
           display_board(theBoard)
           print('Player 1 win')
           game_on = False
       else:
          if full_board_check(theBoard):
              display_board(theBoard)
              print('Draw')
              game_on = False
          else:
             turn = "Player 2"
    else:
       display_board(theBoard)
       position = player_choice(theBoard)
       place_marker(theBoard, player2_marker, position)
       if win_check(theBoard, player2_marker):
            display_board(theBoard)
            print ('Player 2 win')
            game_on = False
       else:
          if full_board_check(theBoard):
             display_board(theBoard)
             print ('Draw')
             game_on = False
          else:
             turn = "Player 1"
  if not replay():
      break