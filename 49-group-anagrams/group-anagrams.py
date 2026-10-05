class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)

        if n == 0 or n == 1:
            return [strs]

        result = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in result:
                result[key] = []
            result[key].append(word)

        return [val for val in result.values()]


