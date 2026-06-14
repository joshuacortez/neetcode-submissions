class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        
        curr_node.is_word = True
    
    def search(self, word: str) -> bool:
        curr_node = self.root

        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
    
        return curr_node.is_word
            
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for c in prefix:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        
        return True
        
        