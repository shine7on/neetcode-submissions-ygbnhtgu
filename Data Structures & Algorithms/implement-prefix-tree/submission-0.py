class PrefixTree:

    def __init__(self):
        self.prefixTree = []
        

    def insert(self, word: str) -> None:
        self.prefixTree.append(word)


    def search(self, word: str) -> bool:
        if word in self.prefixTree:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        length = len(prefix)

        for word in self.prefixTree:
            if length <= len(word):
                if str(word[:length]) == prefix:
                    print('here')
                    return True
        return False
        
        