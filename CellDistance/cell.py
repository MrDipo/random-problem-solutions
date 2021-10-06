# ***CELL.PY***

# checks if two cells are white
# if they are, sumOfCorrespondingCoordinates mod 2 should be 0
# function returns 1 if both are white, returns 0 otherwise
def isWhite(x1, y1, x2, y2): 
  isCellOneWhite = (x1+y1) % 2
  isCellTwoWhite = (x2+y2) % 2
  areBothWhite = isCellOneWhite | isCellTwoWhite 

  return int(areBothWhite == 0)
  
# uses slope of a straight line formula to determine if 2 cells are on the same diagonal
def isDiagonal(x1, y1, x2, y2): 
    return int((y2 - y1)/(x2 -x1) == 1)

# returns positive distance between 2 cells
# if cells are on a diagonal, distance is difference between any 2 corresponding coordinates |x1 - x2| or |y1 - y2|
def getLength(y1, y2):
  return  abs(y2-y1)
