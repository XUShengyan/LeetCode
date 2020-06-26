'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
'''

'''
Idea : 
1 find most freq occur num
2 find the left and right position of num
Problem:
Work but slow
'''
class Solution:
    def findShortestSubArray(self, nums:list) -> int:
        min_length = 1 # when input is [1] ,output is 1
        max_count =0 # max frequency

        for i in range(len(nums)):
            left_element = nums[i]
            if left_element>=0: # judge if the value is already test
                count =1

                for j in range(i+1,len(nums)):
                    right_element = nums[j]
                    if left_element == right_element:
                        nums[j] = -1 # set the same value into invalid
                        current_length = j - i +1
                        count = count +1

                if count > 1:
                    if count > max_count:
                        max_count = count
                        min_length = current_length
                    elif count == max_count:
                        if current_length < min_length:
                            min_length = current_length

        return min_length

test = Solution()
test_data = [1, 2, 2, 3, 1]
print(test.findShortestSubArray(test_data))

test_data = [1,2,2,3,1,4,2]
print(test.findShortestSubArray(test_data))

test_data = [1,2,2,3,1,4,2,4,4]
print(test.findShortestSubArray(test_data))

test_data = [1]
print(test.findShortestSubArray(test_data))

test_data = [1,1]
print(test.findShortestSubArray(test_data))
print('end of test ')


class Solution2(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans

test = Solution2()
test_data = [1, 2, 2, 3, 1]
print(test.findShortestSubArray(test_data))

test_data = [1,2,2,3,1,4,2]
print(test.findShortestSubArray(test_data))

test_data = [1,2,2,3,1,4,2,4,4]
print(test.findShortestSubArray(test_data))

test_data = [1]
print(test.findShortestSubArray(test_data))

test_data = [1,1]
print(test.findShortestSubArray(test_data))