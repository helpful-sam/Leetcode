class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        ### PSEUDO CODE ###
        
        # 1. Order strings from shortest to longest
        # 2. Create an array of ordered pairs (tuples) with the format of (string length, highest index of this-length string)
        # 3. For each strings from 0 to "shortest_upper_index", calculate chain length
        # 4. Return longest chain


        ### ACTUAL CODE ###

        # 1. sort #

        sorted_words = sorted(words, key=len)

        # 2. indexing #

        categories = {key: 0 for key in range(1,17)}

        for index in range(len(words)):
            word_length = len(words[index])
            
            if word_length in categories:
                categories[word_length] += 1

        # 3. chain length calculation #

        # dictionary to store length information
        chain_lengths = {}

        # calculation function
        def calculate_chain_length(word):
            if word in chain_lengths:
                return chain_lengths[word]
            
            max_length = 1  # Minimum chain length is 1 (the word itself)
            
            # Try removing each character from the word
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in words:
                    max_length = max(max_length, 1 + calculate_chain_length(new_word))
            
            chain_lengths[word] = max_length
            return max_length
        
        # recursive logic #
        max_chain_length = 0
        for word in sorted_words:
            max_chain_length = max(max_chain_length, calculate_chain_length(word))

        # 4. return longest chain length #
        return max_chain_length