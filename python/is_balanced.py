#source:https://mmzeynalli.dev/posts/dsa/hackerrank/balanced-brackets/

# def is_balanced(s:str):
    
#     p:list[str] = []
    
#     s = s.replace("{}", "")
    
#     s = s.replace("[]", "")
    
#     s = s.replace("()", "")
    
#     print(f"remaining is {s}")
    
#     if s.startswith(('}', ')', ']')):
        
#         return "NO"
#     else:
#         for i, s_ in enumerate(s):
            
#             s = s.replace("{}", "")
    
#             s = s.replace("[]", "")
            
#             s = s.replace("()", "")
            
#             if '})]'.__contains__(s_):
                
#                 print("s_ is ", s_)
            
#                 if (s_ == '}' and p[-1] == '{' or s_ == ')' and p[-1] == '(' or s_ == ']' and p[-1] == '[') and i >= len(s) / 2:
            
#                     p.pop()
                
#                 else:
                    
#                     return "NO"
            
#             else:              
                
#                 p.append(s_)
            
#             print(p)
            
#         if p == []:
            
#             return "YES"
        
#         else:
            
#             return "NO"
            



def is_balanced(s:str):
    
    stack:list[str] = []
    
    for i, s_ in enumerate(s):        
        print(stack)
        
        print("s_ is ", s_)
        
        if s_ == '[' or s_ == '(' or s_ == '{':
            
            stack.append(s_)
        
        else:
            
            if len(stack) != 0 and (s_ == '}' and stack[-1] == '{' or s_ == ')' and stack[-1] == '(' or s_ == ']' and stack[-1] == '['):
                
                print(f"{s_} match {stack[-1]} is about to be removed\n")
                
                stack.pop()
                
                print("Removed\n")
            
            else:
                
                return "NO"
            
    return "YES" if len(stack) == 0 else "NO"
                
print(is_balanced("{[()]}"))
        
        
        
       