def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    first = 0
    last = len(people)-1
    while first<last:
        if people[first]==limit or people[first]+people[last]>limit:
            answer+=1
            first+=1

        else:
            answer+=1
            first+=1
            last-=1
        
        if first == last:
            answer+=1
            break
        
    return answer