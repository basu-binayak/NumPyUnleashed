import numpy as np

class Miniframe:
    def __init__(self, data, dtype=None):
        self.data = np.array(data, dtype=dtype) # converts data to one structured array
    
    def __repr__(self):
        return str(self.data)
    
    def head(self, n=2):
        return self.data[:n]
    
    def tail(self, n=2):
        # note that indexing starts at 0 
        index = len(self.data) - n
        return self.data[index:]
    
    def dtype(self):
        return self.data.dtype
    
    def shape(self):
        return self.data.shape
    
    def size(self):
        self.rows = self.data.shape[0]
        self.cols = len(self.data[0])
        return self.rows*self.cols
        