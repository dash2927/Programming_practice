# This problem was asked by Zillow.
#
# A ternary search tree is a trie-like data structure where each node may have
# up to three children. Here is an example which represents the words code, cob
# , be, ax, war, and we.
#
#       c
#    /  |  \
#   b   o   w
# / |   |   |
# a  e  d   a
# |    /|   | \
# x   b e   r  e
#
# The tree is structured according to the following rules:
#
# left child nodes link to words lexicographically earlier than the parent
# prefix right child nodes link to words lexicographically later than the
# parent prefix
# middle child nodes continue the current word
#
# For instance, since code is the first word inserted
# in the tree, and cob lexicographically precedes
# cod, cob is represented as a left child extending
# from cod.
#
# Implement insertion and search functions for a
# ternary search tree.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.middle = None
        self.end = False


class ternaryTree:
    def __init__(self):
        self.head = None

    def _insert(self, node, word):
        if not word:
            return node

        head, tail = word[0], word[1:]

        if not node:
            node = Node(head)

        if head < node.data:
            node.left = self._insert(node.left, word)
        elif head > node.data:
            node.right = self._insert(node.right, word)
        else:
            if not tail:
                node.end = True
            else:
                node.middle = self._insert(node.middle, tail)
        return node

    def insert(self, word):
        self.head = self._insert(self.head, word)

    def _search(self, node, word):
        if not node or not word:
            return False

        head, tail = word[0], word[1:]

        if head < node.data:
            return self._search(node.left, word)
        elif head > node.data:
            return self._search(node.right, word)
        else:
            if not tail and node.end:
                return True
            return self._search(node.middle, tail)

    def search(self, word):
        return self._search(self.head, word)


if __name__ == '__main__':
    tTree = ternaryTree()
    tTree.insert('code')
    tTree.insert('cob')
    tTree.insert('cod')
    tTree.insert('be')
    tTree.insert('ax')
    tTree.insert('war')
    tTree.insert('we')
    print(tTree.search('we'))
    print(tTree.search('ax'))
    print(tTree.search('cob'))
    print(tTree.search('be'))
