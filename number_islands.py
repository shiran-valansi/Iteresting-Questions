class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Breadth First Search. Put it into a queue and set its value as '0' to mark as visited node. Iteratively search the neighbors of enqueued nodes until the queue becomes empty.

        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        counter = 0
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    counter += 1
                    self.dfs(grid, row,col, num_rows, num_cols)          
        return counter
    
    
    def dfs(self, grid, row, col, num_rows, num_cols):

        grid[row][col] = 0
        # add neighbors that are 1 to neighbors stack
        self.check_neighbors(grid, row, col, num_rows, num_cols)
       
        # return self.dfs(grid, row, col, neighbors, num_rows, num_cols)


    def check_neighbors(self,grid, row, col, num_rows, num_cols):

        if row > 0:
            # check above
            if grid[row-1][col] == '1':
                self.dfs(grid, row-1, col, num_rows, num_cols)
        if row < num_rows - 1:
            # check below
            if grid[row+1][col] == '1':
                self.dfs(grid, row+1, col, num_rows, num_cols)
        if col > 0:
            # check left
            if grid[row][col-1] == '1':
                self.dfs(grid, row, col-1, num_rows, num_cols)
        if col < num_cols - 1:
            # check right
            if grid[row][col+1] == '1':
                self.dfs(grid, row, col+1, num_rows, num_cols)


