def solution(nums):
    answer = 0
    pokemons = dict()
    
    for i in nums:
        if i not in pokemons:
            pokemons[i] = 1
        else:
            pokemons[i] += 1
    
    count = len(nums)/2
    
    temp = len(pokemons.keys())
    if count <= temp:
        answer = count
    
    else:
        answer = temp
    
    return answer