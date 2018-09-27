from random import randint

board = []

for x in range(0, 10):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)
# import random number between 0-5

def random_row(board):
    return (randint(0, len(board) - 1))
    
def random_col(board):
    return randint(0, len(board[0]) - 1)
    
Treasure_row = random_row(board)
Treasure_col = random_col(board)
Treasure_row1 = random_row(board)
Treasure_col1 = random_col(board)

Treasure_row2 = random_row(board)
Treasure_col2 = random_col(board)
Treasure_row3 = random_row(board)
Treasure_col3 = random_col(board)

Treasure_row4 = random_row(board)
Treasure_col4 = random_col(board)
Treasure_row5 = random_row(board)
Treasure_col5 = random_col(board)

Treasure_row6 = random_row(board)
Treasure_col6 = random_col(board)
Treasure_row7 = random_row(board)
Treasure_col7 = random_col(board)

rows = [Treasure_row,Treasure_row1,Treasure_row2,Treasure_row3,Treasure_row4,Treasure_row5,Treasure_row6,Treasure_row7]
cols = [Treasure_col,Treasure_col1,Treasure_col2,Treasure_col3,Treasure_col4,Treasure_col5,Treasure_col6,Treasure_col7]
print "Enter this value for Guess row, rows before comparing:" ,rows
print "Enter this value for Guess column, cols before comparing:" ,cols

# shifting the treasure if one falls on each other
def Treasure_on_Treasure(guess):
  for i in range(len(guess)):
    for j in range(i + 1, len(guess)):
      cmp(guess[i], guess[j])
      if guess[i] == guess[j]:
        guess[j]+=1
  return guess
      
      
R = Treasure_on_Treasure(rows)
C = Treasure_on_Treasure(cols)

print " rows after comparing :" ,R
print " cols after comparing :" ,C
  

#print set(rows) & set(R)

        

for chance in range(4):
  print "Chance", chance + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  
  
  if (guess_row == Treasure_row and guess_col == Treasure_col) or \
     (guess_row == Treasure_row1 and guess_col == Treasure_col1) or \
     (guess_row == Treasure_row2 and guess_col == Treasure_col2) or \
     (guess_row == Treasure_row3 and guess_col == Treasure_col3) or \
     (guess_row == Treasure_row4 and guess_col == Treasure_col4) or \
     (guess_row == Treasure_row5 and guess_col == Treasure_col5) or \
     (guess_row == Treasure_row6 and guess_col == Treasure_col6) or \
     (guess_row == Treasure_row7 and guess_col == Treasure_col7):
       
    print "Congratulations! You won the Treasure!"
    board[guess_row][guess_col] = '*'
    
  else:
      
    if guess_row not in range(10) or guess_col not in range(9):
      print "Oops,out of range."
    elif board[guess_row][guess_col] == "-":
      print( "You guessed that one already." )
    else:
      print "You missed the Treasure!"
      board[guess_row][guess_col] = "-"
      
    if (chance == 6):
      print "Game Over"
    print_board(board)
