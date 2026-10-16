class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True    
    def search(self, word: str) -> bool:
        def helper(index, node):
            if index == len(word):
                return node.end
            c = word[index]
            if c == ".":
                for child in node.children.values():
                    if helper(index + 1, child):
                        return True
                    
                return False
            else:
                if c not in node.children:
                    return False
                return helper(index + 1, node.children[c])
        return helper(0, self.root)
        
