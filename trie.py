# Change this to 2 if using numbers in trie
SIZE = 26
class TrieNode: 
    def __init__(self): 
        self.data = '/'
        self.children = [None]*SIZE
        self.count = 0
        self.isEndOfWord = False
class Trie:
    # base for binary (0 - 1) -> str = "0" and alphabet (a - z) -> str = "a"
    def __init__(self, base):
        self.root = TrieNode()
        self.BASE = base
    def Ord(self, str):
        return ord(str) - ord(self.BASE)
    def insert(self,string):
        at = self.root
        matches = True
        for i in string:
            # If Already Present, Just Crawl Down.
            if(matches and at.children[self.Ord(i)]):
                at = at.children[self.Ord(i)]
            # Else Create a new TrieNode and Mark data as i and matches False
            else:
                at.children[self.Ord(i)] = TrieNode()
                at = at.children[self.Ord(i)]
                at.data = i
                matches = False
        at.isEndOfWord = True
        # Count of end of string is increased by 1
        at.count += 1
    def search(self,string):
        at = self.root
        matches = True
        found = ""
        for i in string:
            if(matches and at.children[self.Ord(i)]):
                at = at.children[self.Ord(i)]
                found += at.data
            else:
                matches = False
                break
        if(matches and at.isEndOfWord and found):
            return f"found whole {found}"
        elif(matches and found):
            return f"partial match {found}"
        else:
            return "NOT FOUND"
    # You can also give "at" at any position like foot and it will return footpath and football
    # Print in sorted order (You can change this by changing for loop)
    def content(self, at, start, curr = ""):
        if(at != start):
            curr += at.data
        if(at.isEndOfWord == True):
            print(curr, at.count)
        for i in range(SIZE):
            if(at.children[i]):
                self.content(at.children[i], start, curr)
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
T = Trie("a")
keys = ["the","a","there","answer","there","any","by","their"]
for key in keys:
    T.insert(key)
# print(T.search("ther"))
T.content(T.root, T.root)
T.autoComplete("the")
           



    