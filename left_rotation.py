# def rotate_left(d:int, arr:list[int]):
    
#     i = 0
#     while i < d:
           
#         for j in range(len(arr)):
        
#             arr[j-1] = arr[j]
            
#         print(arr)
            
#         i += 1
        
#     return arr

def rotate_left(d:int, arr:list[int]):
    
    for i in range(d):
        
        arr.insert(0, arr.pop())
        
    return arr


test = [1,2,3,4,5]

print(rotate_left(2, test))
        
            