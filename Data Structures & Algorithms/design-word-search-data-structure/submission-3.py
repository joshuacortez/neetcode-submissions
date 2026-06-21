class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()      
    
    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_word = True

    def search(self, word: str) -> bool:

        def _search(word, curr: TrieNode) -> bool:

            for i in range(len(word)):
                char = word[i]
                if char == ".":
                    for key in curr.children:
                        result = _search(word[(i+1):], curr.children[key])
                        if result:
                            return True
                    return False
                else:
                    if char not in curr.children:
                        print(f"{char} not found in {curr.children}")
                        return False
                    curr = curr.children[char]
            
            return curr.is_word

        result = _search(word, self.root)
        return result