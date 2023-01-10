# 처음에 딕셔너리로 접근하려고 하였으나 실패하였고
# enumerate라는 개념을 알게되어 해결하고 replace에 대해서도 다시 생각하게 되었다
# 좋은 문제였던 것 같다.
# 순서로 접근할 떄 enumerate를 사용하면 좋을 것 같다.
def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, num in enumerate(nums):
        numbers = numbers.replace(num, str(i))
    answer = int(numbers)
    return answer