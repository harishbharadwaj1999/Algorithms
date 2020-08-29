def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[start]=nums[start],nums[mid]
                mid+=1
                start+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
