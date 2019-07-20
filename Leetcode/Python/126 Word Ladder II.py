from time import time
import matplotlib.pyplot as plt

class Timer():
    def __init__(self):
        self.initial_time = None
        self.times_list = []

    def start(self):
        if self.initial_time is None:
            self.initial_time = time()
        self.tic = time()

    def stop(self, accumulate=False):
        dt = time() - self.tic
        if accumulate:
            self.times_list.append(self.tic)
        print("dt = {:.4e} sec".format(dt))

    def cumulative(self):
        dt = time() - self.initial_time
        print("Cumulative time = {:.4e} sec".format(dt))

class Solution:

    def isAdjacent(self, w1, w2):
        """ Figures out if words are 'adjacent' to each other. """
        differences = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                differences += 1
        if differences == 1:
            return True
        else:
            return False

    def makeAdjacencyDict(self, words):
        """ Makes an adjacency dictionary from the word list in the form of a dictionary mapping nodes to their adjacent nodes. """
        # First, map words to their index in the list (and vice versa), since manipulating integers is easier than strings
        self.word_to_idx = {w: i for i, w in enumerate(words)}
        self.idx_to_word = {i: w for i, w in enumerate(words)}
        # Initialize empty dict
        adjacency_dict = {i: [] for i in range(len(words))}
        for i1, w1 in enumerate(words[:-1]):
            for i2, w2 in enumerate(words[i1 + 1:], start=i1 + 1):
                if self.isAdjacent(w1, w2):
                    adjacency_dict[i1].append(i2)
                    adjacency_dict[i2].append(i1)
        self.adjacency_dict = adjacency_dict

    def findLaddersBFS(self, beginWord, endWord, wordList):
        """
        Finds word ladders using a breadth-first search which keeps track of every possible path enroute to the end.
        Definitely more memory-intensive than a depth-first search. Maybe high overhead since I need to create new lists
        all the time - should find a way to speed that up.
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        timer = Timer()

        # Immediately detect edge cases
        if endWord not in wordList:
            return []
        elif (beginWord == endWord) or (self.isAdjacent(beginWord, endWord)):
            return [[beginWord, endWord]]

        # Make adjacency dict from word list
        wordList.append(beginWord)
        self.makeAdjacencyDict(wordList)

        # Convert words to indices
        start = self.word_to_idx[beginWord]
        end = self.word_to_idx[endWord]
        # wordList = list(range(len(wordList)))

        # Enter search loop
        done = False
        possiblePaths = [{"path": [start], "visited": []}]
        validPaths = []
        while not done:
            # Iterate over all valid paths backwards (so we can add/modify paths as we pass)
            for p in reversed(range(len(possiblePaths))):
                timer.start()
                path = possiblePaths.pop(p)
                # If final node in path is end, add to validPaths
                if path["path"][-1] == end:
                    validPaths.append(path["path"])
                    continue
                # Else continue adding other nodes to path
                else:
                    # Get adjacent nodes to end of path
                    nodes = self.adjacency_dict[path["path"][-1]]
                    # If any nodes are in list of visited nodes, ignore them
                    nodes = list(filter(lambda node: node not in path["visited"], nodes))
                    # If no new nodes, discard path
                    if len(nodes) == 0:
                        continue
                    # Create new paths with new nodes appended on and the current node marked as visited and append new paths to possiblePaths
                    for node in nodes:
                        newPath = {"path": path["path"] + [node], "visited": path["visited"] + [path["path"][-1]]}
                        possiblePaths.append(newPath)
                timer.stop(accumulate=True)
            # Check if any paths in validPaths, and return them if so
            if (len(validPaths) != 0) or (len(possiblePaths) == 0):
                done = True
        validPaths = [[self.idx_to_word[idx] for idx in path] for path in validPaths]
        plt.plot(timer.times_list)
        plt.show()
        return validPaths





# Test things
beginWords = ["hit", "hit", "a", "qa"]
endWords = ["cog", "cog", "c", "sq"]
wordLists = [
    ["hot", "dot", "dog", "lot", "log", "cog"],
    ["hot", "dot", "dog", "lot", "log"],
    ["a", "b", "c"],
    ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
]
answers = [
    [["hit", "hot", "lot", "log", "cog"], ["hit", "hot", "dot", "dog", "cog"]],
    [],
    [["a", "c"]],
    [["qa","pa","pt","st","sq"],["qa","la","lt","st","sq"],["qa","ma","mt","st","sq"],["qa","ca","cr","sr","sq"],["qa","la","lr","sr","sq"],["qa","fa","fr","sr","sq"],["qa","ba","br","sr","sq"],["qa","ma","mr","sr","sq"],["qa","ca","ci","si","sq"],["qa","na","ni","si","sq"],["qa","la","li","si","sq"],["qa","ta","ti","si","sq"],["qa","pa","pi","si","sq"],["qa","ba","bi","si","sq"],["qa","ha","hi","si","sq"],["qa","ma","mi","si","sq"],["qa","pa","ph","sh","sq"],["qa","ra","rh","sh","sq"],["qa","ta","th","sh","sq"],["qa","ca","co","so","sq"],["qa","ga","go","so","sq"],["qa","ta","to","so","sq"],["qa","na","no","so","sq"],["qa","la","lo","so","sq"],["qa","pa","po","so","sq"],["qa","ya","yo","so","sq"],["qa","ma","mo","so","sq"],["qa","ha","ho","so","sq"],["qa","la","ln","sn","sq"],["qa","ra","rn","sn","sq"],["qa","ma","mn","sn","sq"],["qa","ca","cm","sm","sq"],["qa","ta","tm","sm","sq"],["qa","pa","pm","sm","sq"],["qa","fa","fm","sm","sq"],["qa","ta","tc","sc","sq"],["qa","na","nb","sb","sq"],["qa","pa","pb","sb","sq"],["qa","ra","rb","sb","sq"],["qa","ya","yb","sb","sq"],["qa","ma","mb","sb","sq"],["qa","ta","tb","sb","sq"],["qa","ga","ge","se","sq"],["qa","la","le","se","sq"],["qa","na","ne","se","sq"],["qa","ra","re","se","sq"],["qa","ba","be","se","sq"],["qa","ya","ye","se","sq"],["qa","fa","fe","se","sq"],["qa","ha","he","se","sq"],["qa","ma","me","se","sq"]]
]

for beginWord, endWord, wordList, answer in zip(beginWords, endWords, wordLists, answers):
    tic = time()
    sol = Solution().findLaddersBFS(beginWord, endWord, wordList)
    toc = time()
    sol_set = {tuple(path) for path in sol}
    ans_set = {tuple(path) for path in answer}
    print(len(sol_set.intersection(ans_set)), "/", len(ans_set), "\t({:.4} sec)".format(toc-tic))
