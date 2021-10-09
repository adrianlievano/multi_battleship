import numpy as np

class Board:
  def __init__(self, x_size = 10, y_size = 10):
    """Creates board where battleships will fight"""
    self.x_size = x_size
    self.y_size = y_size
    self.grid_arr = [[i * j for i in range(1,self.x_size + 1)] for j in range(1, self.y_size + 1)]
    print(np.shape(self.grid_arr))
  
  def show_board(self):
    print(self.grid_arr)


class Battleship:
  def __init__(self, board, start_row = 5, start_col = 2, length = 5, width = 0, orientation = 'x'):
    """Creates a battleship object with x and y size.
        start_row = A valid location on a board object.
        start_col = A valid column location on a board object.
        length = The length of the battleship, in terms of board indice steps.
        width = The thickness of the battleship, in terms of board indice steps.
        board = A board class object.
    """
    self.start_col = start_col
    self.length = length
    self.width = width
    self.start_row = start_row
    self.orientation = orientation

    #Health of the ship is total area of indices the ship occupies. 
    self.health = length + length*width 
    print('Ship starts at row {} column {}.'.format(self.start_row, self.start_col))

    board.grid_arr[self.start_row - 1][self.start_col - 1:] = [0 for i in board.grid_arr[self.start_row - 1][self.start_col - 1:]]
    self.ship_vals = board.grid_arr[self.start_row - 1][self.start_col - 1:]                        

  def shoot(self, target_board, target_battleship):
    """Shoots a missile at the enemy battleship on an enemy grid."""
    ## take an input
    row_positions = []
    col_positions = []

    target_grid = np.array(target_board.grid_arr)

    row_input = int(input('What row do you guess? Please pick a number.'))
    col_input = int(input('What column do you guess? Please pick a number.'))

    print('You guessed row {} and column {}'.format(row_input, col_input))

    ## check if the battleship is at the index
    val = target_grid[row_input - 1][col_input - 1]


    if val == 0:
      print('KABOOM! Direct hit. YAR!')
      target_battleship.health -= 1 
      val = -1
      target_grid[row_input - 1][col_input - 1] = val

      if target_battleship.health == 4:
        print('keep shooting! We found them!')
      elif target_battleship.health == 1:
        print('One more shot and we send them to the bottom of the sea!')
      elif target_battleship.health == 0:
        print('Turned to Rubble!')
      else:
        pass
    elif val == -1:
      print('Already hit this spot!')
    else:
        val = -1
        print('Yar! Reload you lazy bums! We missed!')

    target_board.grid_arr = target_grid

    #Returns an updated state on the target_board and target_battleship
    return target_board, target_battleship

  def show_health(self): 
    """Prints the status of the battleship health."""
    print(self.health)

  def place(self, board):
    """Places a battleship object on a game board.
        board = A board class object.
    """
    print(self.grid_arr)

  def show_location(self):
    print(self.ship_vals)