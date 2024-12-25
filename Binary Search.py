def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        mid_value = sorted_list[mid]
        
        if mid_value == target:
            return mid  
        elif mid_value < target:
            low = mid + 1  
        else:
            high = mid - 1 
    
    return -1 

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

index = binary_search(sorted_list, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")
