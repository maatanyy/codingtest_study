def solution(nums):
    dic = {}
    answer = 0
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    count = int(len(nums)/2)

    if len(dic.keys()) >= count:
        answer = count

    else:
        answer = len(dic.keys())

    return answer

print(solution([3,3,3,2,2,4]))
