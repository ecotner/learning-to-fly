"""
The purpose of this script is to generate anagrams (if possible) of a given
word. Words are part of the english dictionary found here:
    http://www.gwicks.net/textlists/english3.zip
which has about 194k words.

The stupid way to do this would be to enumerate all permutations of a given
word and test to see if they're in the dictionary (length D). This will take
forever because if there are N letters in a word (assume average length w), 
there are N! permutations (assuming all distinct letters). If we hash the
dictionary beforehand this will speed things up a bit. Time complexity: O(D*w)
to hash dictionary, O(w*N!) to check potential anagrams. Space complexity: O(D)
to store the dictionary.

A slight improvement might be to simply iterate through the dictionary and
check each word to see if it's an anagram of the given word. This is probably
O(D*N) (with a small prefactor) because you need to iterate over every dict
word, and every character in both words (but only those words that have the
same length as the seed word, otherwise the length check is O(1)/pair).

We can improve on this even further by performing a tree search; turn the
dictionary into a tree where each branch is the next character in a word whose
previous characters are the parents in the tree. In this way, one can do a
depth-first search on the dictionary where we can prune nodes that can't be
created from the seed word. Building this tree takes O(D*w) time, but
subsequent anagram searches should only take O(N) (if there are multiple
anagrams this should scale approximately linearly with their number).

Edit: I benchmarked both of these ways of calculating, and it seems the
tree-based dictionary method is indeed much faster when looking up anagrams,
unless the words are ridiculously long and have a lot of unique characters.

Tree-based:
    Dictionary construction: 1.05 s ± 2.96 ms
    Anagram search: 37.5 us ± 122 ns (search with "asd")
    Anagram search: 11.4 ms ± 43.8 us (search with "supercalifragilistic")
    Anagram search: 76 ms ± 181 us (search with "abcdefghijklmnopqrstuvwxyz")
Brute-force:
    Dictionary construction: 0 (just load raw data)
    Anagram search: 23.9 ms ± 36.1 us (search with "asd")
    Anagram search: 22.6 ms ± 64.7 us (search with "supercalifragilistic")
    Anagram search: 22.5 ms ± 79.9 us (search with "abcdefghijklmnopqrstuvwxyz")
"""

# The slightly better way
def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    d1 = dict()
    d2 = dict()
    for c1, c2 in zip(w1, w2):
        d1[c1] = d1.get(c1, 0) + 1
        d2[c2] = d2.get(c2, 0) + 1
    return d1 == d2

def find_anagrams(word, dict_words):
    anagrams = list()
    for dw in dict_words:
        if is_anagram(word, dw):
            anagrams.append(dw)
    return anagrams

# The "best" way
class CharacterNode:
    def __init__(self, char, parent):
        self.char = char
        self.parent = parent
        self.children = list()

    def create_child(self, char):
        """ Creates a child node with the given character """
        child = CharacterNode(char, self)
        self.children.append(child)
        return child

    def _word(self, chars):
        chars.append(self.char)
        if self.parent is not None:
            return self.parent._word(chars)
        return chars

    def word(self):
        """ Returns the word constructed by traversing the tree from the root
        down to this point
        """
        chars = self._word([])
        return "".join(reversed(chars))

class TreeDictionary:
    def __init__(self, words=None):
        self.root = CharacterNode("", None)
        if words is None:
            return None
        for word in words:
            self.add_word(word)
        self.add_word("#")

    def add_word(self, word, node=None):
        if len(word) == 0:
            return None
        if node is None:
            node = self.root
            word = word + "#"   # Stop token
        for child in node.children:
            if child.char == word[0]:
                self.add_word(word[1:], child)
                return None
        node = node.create_child(word[0])
        self.add_word(word[1:], node)
        return None

    def seed(self, file_path):
        with open(file_path, "r") as fp:
            dict_words = fp.read().split("\n")
        for word in dict_words:
            self.add_word(word)

    def contains(self, word, node=None):
        if len(word) == 0:
            return True
        if node is None:
            node = self.root
            word = word + "#"
        for child in node.children:
            if child.char == word[0]:
                return self.contains(word[1:], child)
        return False

    def _find_anagrams(self, word, node, ana_set):
        if node.char in word:
            word = word.replace(node.char, "", 1)
            if len(word) == 0:
                ana_set.add(node.parent.word())
            else:
                for child in node.children:
                    ana_set |= self._find_anagrams(word, child, ana_set)
        return ana_set

    def find_anagrams(self, word):
        return list(self._find_anagrams(word + "#", self.root, set()))

if __name__ == "__main__":
    words = ["he","hell","hello","hi"]
    d = TreeDictionary(words)
    print(d.contains(""))
    print(d.contains("hello"))
    print(d.contains("asdf"))
    print(d.contains("helloo"))
    print(d.contains("hel"))
    print(d.contains("he"))
    print(d.contains("hell"))
    print(d.contains("hell#"))

    print(d.find_anagrams("eh"))
    print(d.find_anagrams("ass"))
    print(d.find_anagrams("lelh"))
    print(d.find_anagrams("looelh"))
    print(d.find_anagrams(""))

