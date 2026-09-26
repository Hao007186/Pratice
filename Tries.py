class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Tries:
    
    def init(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root

        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isEnd = True

    def serch(self,word):
        cur = self.root

        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.isEnd


    def startwith(self,prefix):
        cur = self.root

        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True