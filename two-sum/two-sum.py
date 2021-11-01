class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        '''
        Brute Force - check each two combinations
        Time O(n^2)
        Space O(1)
        '''
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        #         else:
        #             return []
        '''
        For Array data structure, sometimes we can trade in space for time 
        '''
        
        '''
        Enumerate allows you to loop through a list, tuple, dictionary, string, and             gives the values along with the index.
        Enumerate: x = ('apple', 'banana', 'cherry')
                    y = enumerate(x)
                    print(list(y))
                    [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
        '''
        dict1 = {} #val:index
        for i in range(len(nums)):
            if nums[i] in dict1:
                return dict1[nums[i]], i 
            else:
                dict1[target - nums[i]] = i