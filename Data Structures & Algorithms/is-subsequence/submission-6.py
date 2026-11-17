from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dt = defaultdict(list)
        for i, char in enumerate(t):
            dt[char].append(i)


        last_matching_index = -1

        for char in s:
            if char not in dt:
                return False

            found_valid_position = False
            
            for index in dt[char]:
                if index > last_matching_index:
                    last_matching_index = index
                    found_valid_position = True
                    break
            if not found_valid_position:
                return False
        return True




        