class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # 1. Order strings from shortest to longest
        # 2. Create an array of ordered pairs (tuples) with the format of (string length, highest index of this-length string)
        # 3. For each strings from 0 to "shortest_upper_index", calculate chain length
            # a. split current_string and next_string into arrays
            # b. compare current_string[0] to next_string[0] and next_string[1]
                # bb. if no match, move next_string pointer by 1
                # bb. if match, continue
            # c. compare current_string[1] to next_string[1] and next_string[2] or next_string[2] and next_string[3]
                # note. use upper and lower letter pointers to shift reading frame by 1 or 2 depending on where the match was in step b
        # 4. Return longest chain length as integer 