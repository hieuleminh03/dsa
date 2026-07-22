class Solution:
    def to_dict(self, string: List[str]) -> dict:
        val = {}
        for char in string:
            if char not in val:
                val[char] = 1
            else:
                val[char] += 1
        return val

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outs : List[List[str]] = []
        for idx, string in enumerate(strs):
            if len(outs) == 0:
                outs.append([string])
            else:
                is_new = True
                for out in outs:
                    if self.to_dict(out[0]) == self.to_dict(string):
                        out.append(string)
                        is_new = False
                        break
                if is_new:
                    outs.append([string])
        return outs

## Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]