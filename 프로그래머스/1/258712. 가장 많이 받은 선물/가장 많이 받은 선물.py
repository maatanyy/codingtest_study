def solution(friends, gifts):
    
    graph =  [[0 for _ in range(len(friends)+1)] for _ in range(len(friends)+1)]
    graph2 = [[0 for _ in range(4)] for _ in range(len(friends)+1)]
    
    count = 1
    dict = {}
    
    for i in friends:
        
        dict[i] = count
        count+=1
        
    
    for i in range(len(friends)):
        graph[0][i+1] = friends[i]
        
    for i in range(len(friends)):
        graph[i+1][0] = friends[i]
        
    for i in range(len(friends)):
        graph2[i+1][0] = friends[i]
        
    
    key1 = -1
    key2 = -1
    for i in gifts:
        vals = i.split(' ')
        
        for k, v in dict.items():
            
            if vals[0] == k:
                key1 = v
            
            elif vals[1] == k:
                key2 = v
        
        graph[key1][key2] +=1
        graph2[key1][1] +=1
        graph2[key2][2] +=1
        
    for i in range(len(friends)):
        graph2[i+1][3] = graph2[i+1][1] - graph2[i+1][2]

    answer = -1
    
    for i in range(len(friends)):
        count = 0
        
        for t in range(len(friends)):
            
            if graph[i+1][t+1] > graph[t+1][i+1]:
                count +=1
            
            elif graph[i+1][t+1] == graph[t+1][i+1] and i!=t:
                if graph2[i+1][3] >graph2[t+1][3]:
                    count+=1
        
        answer = max(answer,count)
                
             
    return answer