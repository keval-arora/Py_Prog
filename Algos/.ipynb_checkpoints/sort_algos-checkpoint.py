#Quick Sort: O(nlogn)

def quick_sort(lis):
    """Quick Sort Algorithm"""
    if len(lis)<2:
        return lis
    else:
        pivot = lis[-1]
        small, equal, large = [],[],[]
        for num in lis:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                equal.append(num)      
            else:
                large.append(num)
    return quick_sort(small) + equal + quick_sort(large)


#Merge_Sort
    
def merge_sorted(lis1, lis2):
    """Merges two sorted list(Left list and Right List)"""
    left_index, right_index = 0,0
    sorted_list = []    
    while left_index < len(lis1) and right_index < len(lis2):       
        if lis1[left_index] < lis2[right_index]:
            sorted_list.append(lis1[left_index])
            left_index += 1
        else:
            sorted_list.append(lis2[right_index])
            right_index += 1
    
    while left_index < len(lis1):
        sorted_list.append(lis1[left_index])
        left_index += 1
    while right_index < len(lis2):
        sorted_list.append(lis2[right_index])
        right_index += 1
 
    return sorted_list

def merge_sort(lis):
    """Divide the List into two halfs and pass it to merge"""
    if len(lis) < 2:
        return lis[:]
    else:
        mid = len(lis)//2
        l1 = merge_sort(lis[:mid])
        l2 = merge_sort(lis[mid:])
        return merge_sorted(l1, l2)

