"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
"...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example,
"cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a
concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".



Note:

    The length of words will be at most 100.
    Each words[i] will have length in range [1, 12].
    words[i] will only consist of lowercase letters.
"""

import string

class Solution:

    morse_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                   "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_dict = {char:code for char, code in zip(string.ascii_lowercase, morse_table)}

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # Convert strings to morse code
        morse_words = []
        for word in words:
            morse_words.append(self.encodeMorse(word))
        # Separate code strings into groups according to length
        morse_dict = {}
        for word in morse_words:
            if len(word) in morse_dict:
                morse_dict[len(word)].append(word)
            else:
                morse_dict[len(word)] = [word]
        # Pass each group into the helper function
        count = 0
        for word_len in morse_dict:
            count += self.morseHelper(morse_dict[word_len])
        # Return count
        return count

    def morseHelper(self, words):
        if len(words) == 0:
            return 0
        elif len(words) == 1:
            return 1
        elif all([len(word) < 1 for word in words]):
            return 1
        else:
            dashes = []
            dots = []
            for i in range(len(words)):
                c = words[i][0]
                if (c == "-"):
                    dashes.append(words[i][1:])
                else:
                    dots.append(words[i][1:])
            return self.morseHelper(dashes) + self.morseHelper(dots)

    def encodeMorse(self, word):
        morse_string = []
        for c in word:
            morse_string.append(self.morse_dict[c])
        return "".join(morse_string)

print(Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg", "zulu"]))