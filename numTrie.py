SIZE = 2
class TrieNode: 
    def __init__(self): 
        self.data = '/'
        self.children = [None]*SIZE
        self.count = 0                                        # For delete operation to work out
        self.numEndOfNumber = 0                               # To find frequency of number
# For numbers only
class Trie:
    def __init__(self):
        self.root = TrieNode()
    # Return a string of len 31 which represents binary equivalent of decimal
    def convert31(self, num) -> str:
        curr = bin(num)[2:]
        return "0" * (31 - len(curr)) + curr
    def insert(self, num) -> None:
        at = self.root                                        # Initialize crawler
        string = self.convert31(num)                          # Convert num to string format (31 bit)
        for i in string:
            idx = int(i)                                      # Convert to int format
            # If already present in trie, just crawl down.
            if(at.children[idx]):                      
                at = at.children[idx]                         # Just Crawl down
                at.count += 1                                 # Increase the count of data
            # Else make a new TrieNode and add data
            else:
                at.children[idx] = TrieNode()                 # new TrieNode
                at = at.children[idx]                         # Crawling down
                at.data = idx                                 # Adding data
                at.count += 1
        at.numEndOfNumber += 1                                # Frequency of the num increases by 1
    def search(self, num) -> bool:
        at = self.root                                        # Initialize crawler
        string = self.convert31(num)                          # Convert num to string format (31 bit)
        found = True                                        
        for i in string:
            idx = int(i)                                      # Convert "0" to 0 for index of children to work out
            # If found then just crawl down.
            if(at.children[idx]):                             
                at = at.children[idx]
            # Else not exist
            else:
                found = False
                break
        return found
    # Assumes num is present in Trie and deletes it
    def delete(self, num):
        at = self.root                                        # Initialize Crawler
        string = self.convert31(num)                          # Convert num to string format (31 bit)
        # Crawl down whole string and decrement count 
        for i in string:        
            idx = int(i)                                    
            at = at.children[idx]
            at.count -= 1
        at.numEndOfNumber -= 1                                # Remove one occurance from trie
        # Starts memory cleanup
        at = self.root
        for i in string:
            idx = int(i)
            if(at.children[idx].count == 0):                  # If down that path nothing exists
                at.children[idx] = None                       # Point that path to None else it will exist with count 0
                break
            at = at.children[idx]                             # Crawl down
    # USAGE: T.content(T.root, T.root) => content of trie in decimal form
    def content(self, at, start, curr = "") -> None:
        if(at != start):
            curr += str(at.data)
        if(len(curr) == 31):
            print(int(curr, 2),"->",at.numEndOfNumber)
        for i in range(SIZE):
            if(at.children[i]):
                self.content(at.children[i], start, curr)
    # Assumes atleast one number is present in trie
    # Return int
    def xor_max(self, num) -> int:
        at = self.root
        string = self.convert31(num)
        res = ""
        for i in string:
            idx = int(i)
            if(at.children[1 - idx]):                          # Check if we can go down the opposite
                at = at.children[1 - idx]                      # Crawl down to opposite
                res += "1"                                     # Add 1 because opposite xor makes 1
            else:                                              # Else crawl down to what available...it is always available because of 31 bit for each num
                at = at.children[idx]                          # Crawl down to same
                res += "0"                                     # Add 0 because same xor makes 0
        return int(res, 2)
T = Trie()
nums = [12, 456, 64, 128]
for i in nums:
    T.insert(i)
x =58
real_ans = 0
for i in nums:
    real_ans = max(real_ans, i ^ x)
print(real_ans)
T.content(T.root, T.root)
print(T.xor_max(x))