theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
            ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def check(board, turn):
  # check Horizontal
  if board['top-L'] == board['top-M'] == board['top-R'] == turn:
    return True
  elif board['mid-L'] == board['mid-M'] == board['mid-R'] == turn:
    return True
  elif board['low-L'] == board['low-M'] == board['low-R'] == turn:
    return True
  #Check Vertical
  if board['top-L'] == board['mid-L'] == board['low-L'] == turn:
    return True
  elif board['top-M'] == board['mid-M'] == board['low-M'] == turn:
    return True
  elif board['top-R'] == board['mid-R'] == board['low-R'] == turn:
    return True
  # Check Diagonal
  if board['top-L'] == board['mid-M'] == board['low-R'] == turn:
    return True
  elif board['top-R'] == board['mid-M'] == board['low-L'] == turn:
    return True  


Win = False
turn = 'X'
for i in range(9):
  printBoard(theBoard)
  print('Turn for ' + turn + '. Move on which space?')
  move = input("> ")
  theBoard[move] = turn

  #Check for winner
  win = check(theBoard, turn)
  if win:
    print(turn, 'Wins')
    break
  else:
    if turn == 'X':
      turn = 'O'
    else:
      turn = 'X'
if not(win):
  print('It is a draw')
