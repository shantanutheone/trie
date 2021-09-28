SIZE = 2
class TrieNode: 
    def __init__(self): 
        self.data = '/'
        self.children = [None]*SIZE
        self.count = 0                                      # For delete operation to work out
        self.numEndofNumber = 0                               # To find Occurance of String
        self.isEndOfNumber = False                            # To find Existance of String
