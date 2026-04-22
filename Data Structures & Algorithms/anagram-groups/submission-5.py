class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lsts = []
        hm = {}
        for strng in strs:
            individual_hm = {}
            for letter in strng:
                if letter in individual_hm:
                    individual_hm[letter]+=1
                else:
                    individual_hm[letter] = 1
            hm[strng] = individual_hm

        for i in range(len(strs)):
            key = strs[i]
            if hm[key] != -1:
                lst = [key]
                for j in range(i+1, len(strs), 1):
                    new_key = strs[j]
                    if hm[key] == hm[new_key]:
                        lst.append(strs[j])
                        hm[new_key] = -1
                lsts.append(lst)
        
        return lsts
