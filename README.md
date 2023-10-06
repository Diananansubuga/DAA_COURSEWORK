# DAA_COURSEWORK
coursework for data structures<br>

**QUICK SORT**<br>
**What it is**:<br>
Quicksort is a divide and conquer algorithm which relies on a partition operation: to partition an array an element called a pivot is selected. All elements smaller than the pivot are moved before it and all greater elements are moved after it. This can be done efficiently in linear time and in-place. The lesser and greater sublists are then recursively sorted. Efficient implementations of quicksort (with in-place partitioning) are typically unstable sorts and somewhat complex, but are among the fastest sorting algorithms in practice. Together with its modest O(log n) space usage, quicksort is one of the most popular sorting algorithms and is available in many standard programming libraries. The most complex issue in quicksort is choosing a good pivot element; consistently poor choices of pivots can result in drastically slower O(n²) performance, if at each step the median is chosen as the pivot then the algorithm works in.<br>

**How it works**<br>
1. Choose a Pivot: Select a pivot element from the array. The choice of the pivot can greatly influence the algorithm's performance. Common strategies include selecting the first, last, middle, or a random element as the pivot.<br>

2. Partition the Array: Rearrange the elements in the array so that all elements less than the pivot are on the left side, and all elements greater than the pivot are on the right side. The pivot element is now in its sorted position.<br>

3. Recursively Sort Sub-arrays: Apply Quick Sort recursively to the sub-arrays on the left and right of the pivot until the base case is reached (one or zero elements).<br>

4. Combine Sub-arrays: No explicit combining step is needed, as the array is sorted in place by rearranging the elements during the partitioning step<br>

**Analysis**
1. Time Complexity: O(n log n) on average, O(n^2) in the worst case.<br>
2. Space Complexity: O(log n) auxiliary space for recursive calls.<br>

**HEAP SORT**
Heap Sort:<br>
**What it is**
Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to build a max-heap and then repeatedly extracts the maximum element from the heap and places it at the end of the sorted array. It combines the advantages of both the merge sort and insertion sort algorithms.<br>

**How it Works**<br>

1. Build Max-Heap: The first step of Heap Sort is to build a max-heap from the input array. A max-heap is a binary tree where the parent nodes are greater than or equal to their children. This heap is built bottom-up, starting from the last non-leaf node and repeatedly calling a function to maintain the max-heap property. The result is a heap where the maximum element (at the root) is in the correct position.<br>

2. Swap and Heapify: After building the max-heap, the maximum element (at the root) is swapped with the last element in the array. The heap size is reduced by 1, effectively excluding the last element from further consideration. The swap might violate the max-heap property, so the heapify operation is performed on the root to maintain the max-heap property. This process ensures that the largest element is at the end of the array.<br>

Repeat: Steps 2 are repeated for the remaining elements until the heap size is reduced to 1. At this point, the array is sorted in ascending order.<br>
**Analysis:**

1. Time Complexity: O(n log n) for the worst, average, and best cases.
2. Space Complexity: O(1) auxiliary space (in-place sorting).

**COUNTING SORT**
**What it is**

Counting Sort is a non-comparison-based sorting algorithm that operates by counting the number of occurrences of each element and using arithmetic to determine their positions in the output array. It is efficient for sorting integers within a specific range.

**How it works**

1. Counting Frequencies: The first step in Counting Sort is to count the occurrences of each unique element in the input array. This step creates a frequency array where the index represents the element, and the value represents how many times the element appears in the input.

2. Calculate Positions: Next, calculate the positions of elements in the sorted array. Iterate through the frequency array and accumulate the counts. This step determines where each element will be placed in the sorted output.

3. Build Sorted Array: Create a new array to store the sorted elements. Iterate through the input array in reverse, find the position of each element from the frequency array, and place it in the correct position in the output array. Decrement the count in the frequency array for each element placed in the output array.

**Analysis**
1. Time Complexity: O(n + k), where n is the number of elements in the input array and k is the range of the input.
2. Space Complexity: O(k) additional space for the counts array.

**LINK TO IMAGES AND EXPLANATION**
https://docs.google.com/document/d/1eyeVQ0Gt3A0e3jOJme4eg7iA2GumlxaBqCeYIjeF338/edit?usp=sharing








