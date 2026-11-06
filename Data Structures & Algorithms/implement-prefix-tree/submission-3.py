class PrefixTree:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def insert(self, word: str) -> None:
        curNode = self
        for i,c in enumerate(word):
            if c not in curNode.children:
                curNode.children[c] = PrefixTree()
            curNode = curNode.children[c]
        curNode.endOfWord = True
        

    def search(self, word: str) -> bool:
        curNode = self
        for c in word:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return curNode.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self
        for c in prefix:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)