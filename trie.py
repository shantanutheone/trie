SIZE = 26
class TrieNode: 
    def __init__(self): 
        self.data = '/'
        self.children = [None]*SIZE
        self.count = 0                                      # For delete operation to work out
        self.numEndOfWord = 0                               # To find Occurance of String
        self.isEndOfWord = False                            # To find Existance of String
class Trie:
    def __init__(self, base):
        self.root = TrieNode()
        self.BASE = "a"                                     # Only working with alphabets "a"-"z"
    # return order of string "a" - 0, "b" - 1
    def Ord(self, str): 
        return ord(str) - ord(self.BASE)
    # inserts string in trie
    def insert(self,string):
        at = self.root
        matches = True                                      # if prefix already found matches remains true otherwise make new TrieNodes
        for i in string:
            # If Already Present, Just Crawl Down.
            if(matches and at.children[self.Ord(i)]):
                at = at.children[self.Ord(i)]               # Crawl Down
                at.count += 1                               # Count++ because one more prefix exists now.
            # Else Create a new TrieNode and Mark data as i and matches False
            else:
                at.children[self.Ord(i)] = TrieNode()       # New TrieNode Created
                at = at.children[self.Ord(i)]               # Crawl Down to newly Created Trienode
                at.count += 1                               # Count++ because one more prefix exists now.
                at.data = i                                 # Add the data to TrieNode
                matches = False                             # Matches false because now every time we have to create new TrieNode
        at.isEndOfWord = True                               # Seperate work for last one
        at.numEndOfWord += 1                                # Count of end of string is increased by 1
    # search string in trie                           
    def search(self,string):
        at = self.root                                      # Initialize Crawler
        matches = True                                      # if prefix already found it remains true
        found = ""                                          # stores prefix of string which is present in trie
        for i in string:
            if(matches and at.children[self.Ord(i)]):       # matches + children is not null
                at = at.children[self.Ord(i)]               # Crawl down
                found += at.data                            # Add data
            else:
                matches = False                             # Break cause data not found
                break
        if(matches and at.isEndOfWord and found):           # Last is "isEndOfWord" then found whole
            return f"found whole {found}"
        elif(matches and found):                            # not "isEndOfWord" then partial 
            return f"partial match {found}"
        else:                                               
            return "NOT FOUND"
    # dfs to find content in trie
    # You can also give "at" at any position like foot and it will return footpath and football
    # Print in sorted order (You can change this by changing for loop)
    def content(self, at, start, curr = ""):
        if(at != start):
            curr += at.data
        if(at.isEndOfWord == True):
            print(curr, at.numEndOfWord)
        for i in range(SIZE):
            if(at.children[i]):
                self.content(at.children[i], start, curr)
    # finds remaining suffix possible
    # ["the", "their", "there"] for prefix = "the" then prints ["", "ir", "er"]
    def autoComplete(self, prefix):
        at = self.root
        matches = True
        for i in prefix:
            if(matches and at.children[self.Ord(i)]):
                at = at.children[self.Ord(i)]
            else:
                matches = False
                break
        if(matches == True):
            self.content(at, at)
    # prints count of each word along with whole string occurance
    def contentCount(self, at, start, curr = ""):
        if(at != start):
            curr += at.data
        print(at.data, at.count)
        if(at.isEndOfWord == True):
            print(curr, "->", at.numEndOfWord)
        for i in range(SIZE):
            if(at.children[i]):
                self.contentCount(at.children[i], start, curr)
    # Assumes that string is present in trie
    def delete(self, string):
        at = self.root                                      # Initialize Crawler
        for i in string:
            at = at.children[self.Ord(i)]                   # Crawl down
            at.count -= 1                                   # --count cuz removing one occurance
        at.numEndOfWord -= 1                                # one numEndOfWord negated
        if(at.numEndOfWord == 0):
            at.isEndOfWord = False                          # Mark "isEndOfWord" as False if "numEndOfWord" becomes 0
        # If at any point children doesn't exist mark that as none otherwise memory wasted.
        at = self.root
        for i in string:
            if(at.children[self.Ord(i)].count == 0):
                at.children[self.Ord(i)] = None
                break
            at = at.children[self.Ord(i)]
T = Trie("a")
keys = ["the","a","there","answer","there","any","by","their","anyway", "ask", "afk","ask"]
for key in keys:
    T.insert(key)
# print(T.search("ther"))
T.contentCount(T.root, T.root)
T.delete("any")
print("----")
T.contentCount(T.root, T.root)