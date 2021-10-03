import numpy

class Board:
  def __init__(self, xsize = 10, ysize = 10):
    """Creates board where battleships will fight"""
    self.xsize = xsize
    self.ysize = ysize
    self.grid_arr = [[i * j for i in range(1,self.xsize + 1)] for j in range(1, self.ysize + 1)]
    print(np.shape(self.grid_arr))
  
  def show_board(self):
    print(self.grid_arr)


class Battleship(Board):
  def __init__(self, start_row = 5, start_col = 2, xsize = 1, length = 5, width = 0, orientation = 'x'):
    """Creates a battleship object with x and y size. Inherits from Board class."""
    Board.__init__(self)

    self.start_col = start_col
    self.length = length
    self.width = width
    self.start_row = start_row
    self.orientation = orientation

    self.health = length*width  #ensures the length of the battleship is total health of the ship.
    print('Ship starts at row {} column {}.'.format(self.start_row, self.start_col))

    if self.orientation == 'x':
      print(self.grid_arr[self.start_row - 1:self.start_row+width][:1][0][self.start_col - 1:length + 1])
      self.ship_vals = self.grid_arr[self.start_row - 1:self.start_row+width][:1][0][self.start_col - 1:length + 1]                                                                                                                  )
    else:
      ##handles logic if the player decides to play the battleship in another orientation.
      pass                            

  def shoot(self, target_grid):
    """Shoots a missile at the enemy battleship"""
    ## take an input
    row_positions = []
    col_positions = []

    # for i, row_idx in enumerate(range(np.size(target_grid)[0])):
    #   for j, col_idx in enumerate(range(np.size(target_grid)[1])):
    #     row_positions.append(row_idx)
    #     col_positions.append(col_idx)
    
    row_input = int(input('What row do you guess? Please pick a number.'))
    col_input = int(input('What column do you guess? Please pick a number.'))

    print('You guessed row {} and column {}'.format(row_input, col_input))

    ## check if the battleship is at the index

    ## if it hit, print hit! reduce hp of battleship by 1 and check if the spot is already hit

    ##print life of the battleship
    pass

  def healthbar(self): 
    """Prints the status of the battleship health."""
    print(self.health)

  def place(start_row = 5, start_col = 2, length = 5, width = 0):
    """Passes a battleship within the game grid."""
    print(self.grid_arr)
