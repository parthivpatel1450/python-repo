class Solution:
    def longestSubarray(self,arr, k):
        dic = {}
        answer = 0
        pSum = 0

        for i in range(len(arr)):
            pSum += arr[i]


            if pSum == k:
                answer = i + 1


            elif (pSum - k) in dic:
                answer = max(answer, i - dic[pSum - k])

            if pSum not in dic:
                dic[pSum] = i

        return answer