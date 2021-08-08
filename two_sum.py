class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict, pair, index, found_pair = {}, [], 0, False
        
        # Key: number, Value: index
        while index < len(nums):
            mydict[nums[index]] = index
            index += 1
        
        # Reset index
        index = 0
        
        # Iterate through list and find complement of value at index
        while index < len(nums) and not found_pair:
            complement = target - nums[index]
            if complement in mydict:
                if index != mydict[complement]:
                    pair.append(index)
                    pair.append(mydict[complement])
                    found_pair = True
            index += 1
        return pair