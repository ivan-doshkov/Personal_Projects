from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_list = []
        for idx in range(len(nums)):
            for i in range(len(nums)):
                if idx == i:
                    continue
                elif nums[idx] + nums[i] == target:
                    idx_list.append(idx)
                    idx_list.append(i)
                    return idx_list


