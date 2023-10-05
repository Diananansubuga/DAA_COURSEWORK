# DAA_COURSEWORK
coursework for data structures<br>

**QUICK SORT**<br>
**What it is**:<br>
Quick Sort is a sorting algorithm based on the divide-and-conquer strategy. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.<br>
**How it works**<br>
1. Choose a Pivot: Select a pivot element from the array. The choice of the pivot can greatly influence the algorithm's performance. Common strategies include selecting the first, last, middle, or a random element as the pivot.<br>

2. Partition the Array: Rearrange the elements in the array so that all elements less than the pivot are on the left side, and all elements greater than the pivot are on the right side. The pivot element is now in its sorted position.<br>

3. Recursively Sort Sub-arrays: Apply Quick Sort recursively to the sub-arrays on the left and right of the pivot until the base case is reached (one or zero elements).<br>

4. Combine Sub-arrays: No explicit combining step is needed, as the array is sorted in place by rearranging the elements during the partitioning step<br>


**Sample Code**<br>

```

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    pivot = arr[len(arr) // 2]  # Choose pivot (middle element)
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    
    return quick_sort(left) + middle + quick_sort(right)  # Recur on sub-arrays and combine

# Example usage
input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quick_sort(input_array)
print("Sorted Array:", sorted_array)

```
#explanation of code:

1. The function quick_sort takes an input list arr.<br>
2. If the length of arr is 1 or less, it's already sorted, so the function returns arr as it is the base case.<br>
3. The pivot element is chosen as the middle element of the input array.<br>
4. The list comprehension is used to create three sub-arrays: left, middle, and right, which contain elements less than, equal to, and greater than the pivot, respectively.<br>
5. The function recursively calls itself on the left and right sub-arrays and concatenates the sorted sub-arrays with the middle array.<br>
6. The sorted array is returned.<br>

**Analysis**
1. Time Complexity: O(n log n) on average, O(n^2) in the worst case.<br>
2. Space Complexity: O(log n) auxiliary space for recursive calls.<br>







