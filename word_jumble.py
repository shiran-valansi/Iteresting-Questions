from copy import copy

def jumble(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool

    >>> jumble([['x','x','b'],['x','x','l'],['m','o','o']], 'bloom')
    True

    """
    
    if not word:
        return False
    num_rows = len(board)
    num_cols = len(board[0])
    # list of all possible positions of first letter of word on the board
    first_pos = find_char(board, word[0], num_rows, num_cols)

    for pos in first_pos:   
        if recurse(board, word[1:], pos, [], num_rows, num_cols):
            return True
    return False
    
        
        
def find_char(board, char, num_rows, num_cols):
    """returns a list of all possible locations of char on board"""
    first_pos = []
    for i in range(num_rows):
        for j in range(num_cols):
            if board[i][j] == char:
                first_pos.append((i,j))
    return first_pos
        
    
        
def recurse(board, word, start, visited, num_rows, num_cols):
    """returns true if found a path on the board that forms the word"""
    visited.append(start)

    if not word:
        return True
    # list of possible neighbors with the value of the next letter in word
    neighbors = find_neighbors(board, word[0], start, num_rows, num_cols)
    
    for neighbor in neighbors:
        if neighbor not in visited:
            # visited list needs to be shared only upon all cells that share a path
            visited_temp = copy(visited)
            found = recurse(board, word[1:], neighbor, visited_temp, num_rows, num_cols)
            if found:
                return True
    
    return False



def find_neighbors(board, char, start, num_rows, num_cols):
    """ returns list of neighbors whos values match char"""
    # neighbors is a list of tuples that represent a position on the board
  
    neighbors = []
    
    row = start[0]
    col = start[1]
    if row > 0:
        # check above
        if board[row-1][col] == char:
            neighbors.append((row-1,col))
    if row < num_rows-1:
        # check below
        if board[row+1][col] == char:
            neighbors.append((row+1,col))
    if col > 0:
        # check right
        if board[row][col-1] == char:
            neighbors.append((row,col-1))
    if col < num_cols-1:
        # check left
        if board[row][col+1] == char:
            neighbors.append((row,col+1))     
    return neighbors