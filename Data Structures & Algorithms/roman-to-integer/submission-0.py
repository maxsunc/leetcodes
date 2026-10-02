class Solution:
    def romanToInt(self, s: str) -> int:
        # dictionary O(1) lookup
        vals = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        pairs = {'I' : ('V', 'X'),'X' : ('L','C'), 'C' : ('D','M')}
        specials = {'V' : 4, 'X' : 9, 'L' : 40, 'C' : 90, 'D' : 400,'M' : 900}
        # the whole thing is additive, the special case is the 4 and 9's
        # pairs: {I : ( V, X)}
        # {X : (L,C)}

        # iterate through the string

        # when we find a value in the pairs
        # MDCCCLXXXIV
        # 1000 + 500 + 100 + 100 + 100 + 50 + 
        expected = None
        res = 0
        for c in s:
            if expected:
                if expected[1] == c or expected[2] == c:
                    res += specials[c]
                    expected = None # used up two spaces
                    continue
                else:
                    # we didnt find what we wanted, lets add it and reset
                    res += vals[expected[0]]
                    expected = None
            # if its apart of the pair lets pause
            # only if we're not looking for a pair already
            if not expected and c in pairs:
                # load into expected and pause
                expected = (c, pairs[c][0],pairs[c][1])
            else:
                res += vals[c]  
        if expected:
            res += vals[expected[0]]
        return res
