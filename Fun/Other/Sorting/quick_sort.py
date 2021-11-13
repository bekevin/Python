import sys

def quick_sort(x: list)->list:
    if len(x) <= 1:
        return x
    else:
        low = []
        high = []
        length = len(x)
        pivot, index = best_choice(x, length)
        x.pop(index)
    for i in x:
        if i < pivot:
            low.append(i)
        else:
            high.append(i)
    
    return quick_sort(low) + [pivot] + quick_sort(high)

def best_choice(x: list, length: int) -> tuple[int, int]:
    #increase or decrease the number of picks based on list size (decrease speed from O(1) ->O(log n))
    #need to test if increasing picks based on list size increases speed or not on average. big vs small lists
    #right now we are picking 3 from begginning middle and end but we need to pick 3 if <1000 items and 4 if 1000 items and 5 if 10000 items etc.
    sort = sorted([x[0], x[length-1], x[int(length/2)]])
    #need to find index faster then the list.index() function (O(n) -> O(log(n)))
    return sort[1], x.index(sort[1]) 
    
print(quick_sort([-2,-2,-2,4,2,1,89,34,24,56,-3,2.2,5,-34,34,23,56,23,156,1,14]))
