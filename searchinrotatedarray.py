def search(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            for i in range(len(nums)-1,0,-1):
                if target==nums[i]:
                    return i
            return -1
        else:
            for i in range(len(nums)):
                if target==nums[i]:
                    return i
            return -1
