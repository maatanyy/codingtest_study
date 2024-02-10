def solution(nums):
    answer = 0
    length = len(nums)//2
    nums = set(nums)
    nums = list(nums)
    
    for _ in range(length):
        
        if len(nums) == 0:
            break
        nums.pop()
        answer+=1    
    
    return answer