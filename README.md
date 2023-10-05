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

**COUNTING SORT**








