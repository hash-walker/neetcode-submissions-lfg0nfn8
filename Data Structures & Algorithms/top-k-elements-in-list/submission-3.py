class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        frequent = []

        for num in nums:
            freqs[num] += 1
        
        for key in freqs:
            if freqs[key] >= k:
                frequent.append(key)

        return frequent