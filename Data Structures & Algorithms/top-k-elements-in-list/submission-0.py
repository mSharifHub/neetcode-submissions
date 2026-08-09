class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        frequency_sorted = sorted(frequency.items(), key= lambda x: x[1], reverse = True)
            
        return [item[0] for item in frequency_sorted[:k]]