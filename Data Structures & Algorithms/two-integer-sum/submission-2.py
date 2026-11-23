class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Verify that we never sum the two same indices
        # No case where a valid i and j don't exist in nums
        # Exactly one valid i and j
        # nums is not sorted

        # Brute Force
        # - Two pointers and use two loops
        # - O(n^2) ;-;

        # [3,2,1,8,9] target = 10
        # 
        # 1st loop:
        # -> add all nums to a hash set (0(1) access time)
        # 
        # 2nd loop:
        # -> for all elements in hashmap
        #   -> diff = target - element
        #   -> if diff in set add it to result break out

        num_map = {}
        indices = []

        # Add all nums to hash set
        for i, num in enumerate(nums):
            if num in num_map:
                num_map[num].append(i)
            else:
                num_map[num] = [i]

        print(num_map)

        # Find the difference between target and current
        for num in num_map.keys():
            diff = target - num
            if diff in num_map and not (diff == num and len(num_map[diff]) < 2):
                print(len(num_map[diff]))
                if len(num_map[diff]) > 1 and num_map[diff] == num_map[num]:
                    indices.extend(num_map[diff])
                        
                else:
                    indices.append(num_map[diff][0])
                    indices.append(num_map[num][0])

                break
        
        indices.sort()

        # Return the answer with the smaller index
        return indices