class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # build a hash map
        # go over each row in wall
        # for each brick we have a sum wich is the length so far of the bricks including our current brick
        # the map is a dictionary, each key is the comulative sum of lengths of bricks, 
        # the value is the count of bricks which uptil then add up to that sum
        sums_map = {}
        if not wall:
            return 0
        height = len(wall)
     
        for row in wall:
            length = 0
            row_len = len(row)
            for brick in row[:-1]:
                length += brick
                sums_map[length] = sums_map.get(length,0) +1
        # print(sums_map)
        if not sums_map:
            return height
        max_sum = max(sums_map.values())
        crossed = height - max_sum
        return crossed