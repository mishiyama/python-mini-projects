#just a rough idea of how the code is going to be : )
# 
#  def main():
#     initialize board
#     decide who goes first
#     while game not over:
#         print the board
#         get move from player or computer
#         update board
#         check for win or tie
#         switch turns


import numpy as np
import random

PLAYER_X = '❌'
PLAYER_O = '🔵'



def print_board(board):
   for i in range(3):
    row = ' | '.join(board[i])
    print("\t" + row)
    if i < 2:
      print("\t" + "-" * 10)

def update_board(board,row,column,current_player):
  board[row,column]=current_player

def first_turn():
   return random.choice([PLAYER_O,PLAYER_X])


def get_move(board):
   while True:
        try:
            move = input("Enter your move as row,col (0-2, e.g. 1,2): ")
            row, col = map(int, move.split(','))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue
            if board[row, col] != ' ':
                print("Cell already occupied. Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid format. Please enter row and column separated by a comma.")


def winning_condition(board,player):
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def board_full(board):
  return not np.any(board == ' ')
  

def main():
    print("\n********* TIC - TAC - TOE ********* \n")
    board=np.full((3,3),' ')

    current_player=first_turn()
    print(f"\n {current_player} gets the first chance")

    while True:
      print_board(board)
      if current_player==PLAYER_X:
        print("Player ❌ turn")
        row, col = get_move(board)
        update_board(board, row, col, current_player)

      else:
        print("Player 🔵 turn")
        row, col =get_move(board)
        update_board(board, row, col, current_player)
      
      if winning_condition(board,current_player):
        print_board(board)
        print(f"Player {current_player} wins! 🎉")
        break
      

      if board_full(board):
        print_board(board)
        print("It's a tie! ")
        break

      if (current_player==PLAYER_O):
        current_player=PLAYER_X
      else:
        current_player=PLAYER_O
while True:
 main()
 rematch=input("Go for another round??? yes or no ")
 if rematch.lower()=="yes":
  main()
 else:
  print("Good game and thanks for playing")
  break
         
      
      
if __name__=="__main__":
 main()