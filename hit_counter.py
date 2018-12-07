import time
class HitCounter:

    def __init__(self):
        """
        Initialized data structure 
        """
        self.record = []
        self.length = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.record.append(timestamp)
        
        self.length +=1
        
        

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # init start time, and make sure start is positive
        start = timestamp - 300
        if start < 0:
            start = 0
       
        i = 0
        counter = 0
        # find starting timestamp value to count
        while i<self.length and self.record[i] <= start :
            i+=1
        # count number of timestamps in time range
        while  i < self.length and self.record[i] <= timestamp :
            counter +=1
            i+=1
        
        return counter
            
            


        
        
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)