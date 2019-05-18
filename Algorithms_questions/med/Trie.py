class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char = ''
        self.children = []
        self.word_finished = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self
        for c in word:
            is_char_found = False

            for child in node.children:
                if child.char == c:
                    node=child
                    is_char_found = True
                    break
            if is_char_found == False:
                new_node = Trie()
                new_node.char=c
                node.children.append(new_node)
                node =new_node
        node.word_finished = True



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not node.children:
            return False
        for c in word:
            is_char_found = False
            for child in node.children:
                if child.char == c:
                    is_char_found = True
                    node=child
                    break
            if not is_char_found:
                return False
        if node.word_finished:
            return True
        return False




    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not node.children:
            return False
        for c in prefix:
            is_char_found = False
            for child in node.children:
                if child.char == c:
                    is_char_found = True
                    node=child
                    break
            if not is_char_found:
                return False
        return True


if __name__ == "__main__":
    x = Trie()
    x.insert("apple")
    print(x.search("app"))
    print(x.children[0].char)
    print(x.children[0].children[0].char)


