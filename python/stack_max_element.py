
# def getMax(operations:list[str]) -> list[int]:
    
#     stack:list[int] = []
    
#     for operation in operations:
        
#         if operation[0] == '1':
            
#             stack.append(int(operation[2:]))
            
#             # print(int(operation[2:]))
            
#         elif operation[0] == '2':
            
#             stack.pop()
            
#         elif operation[0] == '3':
            
#             print(max(stack))
                        
#     return stack
            

def getMax(operations:list[str]) -> list[int]:
    
    stack:list[int] = []
        
    answers:list[int] = []
    
    max_stack: list[int] = []
    
    for operation in operations:
        
        if operation.startswith('1'):
            
            
            val = int(operation[2:])
            
            stack.append(val)
            
            current_max = val if not max_stack else max(val, max_stack[-1])
            
            max_stack.append(current_max)
            
        else:
            
            if operation == '2':
                
                stack.pop()
                
                max_stack.pop() 
            
            else:
                answers.append(max_stack[-1])
                
    return answers
            
print(getMax(['1 97', '2', '1 20', '2', '1 26', '1 20', '2', '3', '1 92221', '3']))