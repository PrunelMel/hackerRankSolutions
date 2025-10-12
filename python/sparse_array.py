def matching_strings(strings:list[str], queries:list[str]) -> list[int]:
    
    answers:list[int] = []
    
    for i in range(len(queries)):
        
        answers.append(strings.count(queries[i]))
        
    return answers