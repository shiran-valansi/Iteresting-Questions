class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
     
        new_board = make_board(m,n)

        for x in range(m):
            for y in range(n):
                # go over each cell on the board
                # for each one count how many living neighbors it has
                # neighbors are: [x][y-1], [x][y+1],[x-1][y],[x+1][y],[x+1][y-1],[x+1][y+1],[x-1][y+1],[x+1][y-1]
                live_count = count_surrounding(x,y,m,n,board)
                
                new_board[x][y] = dead_or_alive(board[x][y],live_count)
        
        copy_board(board, new_board, m, n)
        
                    
                            
                
def make_board(m,n):
    new_board = []
    for i in range(m):
        new_board.append([])
        for j in range(n):
            new_board[i].append(0)
    return new_board


def count_surrounding(x,y,m,n,board):
    live_count = 0
    for x2 in range(x-1,x+2):
        for y2 in range(y-1,y+2):
            # check if point is inside board dimensions
            if x2>=0 and x2<m and y2>=0 and y2<n:
                #check that the point is not our center point
                if not (x2==x and y2==y):
                    if board[x2][y2] == 1:
                        live_count+=1
    return live_count


def dead_or_alive(num,live_count):
    if num == 1:
        if live_count==2 or live_count==3:
            return 1
    else:
        if live_count == 3:
            return 1
    return 0
        
        
def copy_board(board, new_board, m, n):
    for x in range(m):
        for y in range(n):
            board[x][y] = new_board[x][y]

