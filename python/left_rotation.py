
# def rotate_left(d:int, arr:list[int]):
    
#     res:list[int] = []
    
#     for i in range(d):
        
#         res = []
        
#         first:int = 0
        
#         for j in range(len(arr)):
            
#             if j == 0:
                
#                 first = arr[0]
            
#             else:
                
#                 res.append(arr[j])
                
#         res.append(first)
            
#         arr = res
                        
#     return arr
                
def rotate_left(d: int, arr: list[int]) -> list[int]:
    n = len(arr)
    d = d % n 
    return arr[d:] + arr[:d]

            

test = [1,2,3,4,5]

print(rotate_left(3, test))
        
            