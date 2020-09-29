def solution(nums):
    if nums:
        nums.sort()
        return nums
    else:
        return []
solution([1,2,10,5])