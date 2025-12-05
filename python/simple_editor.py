""" notes: To get the last k elements of the string, we can use the slice notation s[-k:]
    To remove the last k elements of the string, we can use the slice notation s[:-k]
"""

# def rm_last_k(tab:list[any], k:int) -> None:
    
#     step:int = 0

#     for i in range(len(tab) - 1, -1, -1):
        
#         step += 1      
        
        
#         if step > k:
#             break
            
#         else:
#             tab.pop(i)

def simple_editor(q:list[str]):
    
    s:str = ""
    
    ops:list[str] = []
    
    for req in q:
        
        # print(f"req is {req}")
        
        # print(f"s before is {s}")
        
        if req.startswith('1'):
            
            s += req.split(' ')[-1]
            
            ops.append(req)
        
        elif req.startswith('2'):
            
            k = int(req.split(' ')[-1])
            
            ops.append(f"2 {s[-k:]}")
            
            s = s[:-k]
                    
        elif req.startswith('3'):
            
            val:int = int(req.split(' ')[-1])
            
            print(s[val - 1])
            
        elif req.startswith('4'):
            
            last_op:str = ops[-1]
            
            # print(f"last_op is {last_op}")
            
            if ops[-1   ].startswith('1'):
                
                k = int(len(last_op.split(' ')[-1]))
                
                s = s[:-k]
                
                ops.pop()
                
            elif ops[-1].startswith('2'):
                
                removed:str = ops[-1].split(' ')[-1]
                
                s += removed
                
                ops.pop()

        # print("s after is ",s)
            
            
# n_operation:int = int(input("Enter the number of operations").strip())

# q:list[str] = []

# for i in range(n_operation):
    
#     q.append(input("Enter the operation").strip())
    
        
                
simple_editor(['1 abc', '3 3', '2 3', '1 xy', '3 2', '4', '4', '3 1'])   