class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        frequent = []

        for num in nums:
            freqs[num] += 1

        sorted_freqs = dict(sorted(freqs.items(), key = lambda item : item[1], reverse=True))
        count = 0
        for key in sorted_freqs:
            count += 1
            if count > k:
                break
            frequent.append(key)

        return frequent