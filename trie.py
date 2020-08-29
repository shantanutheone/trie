class TrieNode: 
    def __init__(self): 
        self.data = '/'
        self.children = [None]*26
        self.count = 0
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,string):
        at = self.root
        matches = True
        for i in string:
            if(matches and at.children[ord(i)-ord('a')]):
                at = at.children[ord(i)-ord('a')]
                at.count += 1
            else:
                at.children[ord(i)-ord('a')] = TrieNode()
                at = at.children[ord(i)-ord('a')]
                at.data = i
                matches = False
                # print(at.data,end = " ")
        at.isEndOfWord = True
    def search(self,string):
        at = self.root
        matches = True
        found = ""
        for i in string:
            if(matches and at.children[ord(i)-ord('a')]):
                at = at.children[ord(i)-ord('a')]
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

T = Trie()
keys = ["the","a","there","anaswe","any","by","their"]
for key in keys:
    T.insert(key)
print(T.search("by"))
           



    