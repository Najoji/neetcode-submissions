class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums :
            if i not in dict1 :
                dict1[i] = 1
            else :
                dict1[i] += 1 
       
            

        sorted_nums = sorted(dict1, key = dict1.get, reverse = True )

        return sorted_nums[:k]

        