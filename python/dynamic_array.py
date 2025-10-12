
def dynamic_array(n:int, queries:list[list[int]]) -> list:
    
    arr:list[list] = []
    
    answers:list = []
    
    last_answer:int = 0
        
    for i in range(n):
        arr.append([])
        
    for i in range(len(queries)):
        
        indx:int = (queries[i][1] ^ last_answer) % n
                
        if queries[i][0] == 1:
            
            arr[indx].append(queries[i][2])
        
        if queries[i][0] == 2:
            
            last_answer = arr[indx][queries[i][2] % len(arr[indx])]
            
            answers.append(last_answer)
            
    return answers

test = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]

print(dynamic_array(2, test))

# dynamic_array(2, test)