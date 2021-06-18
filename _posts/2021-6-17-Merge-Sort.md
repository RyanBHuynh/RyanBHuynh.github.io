---
layout: post
title: Merge Sort
---

Merge sort is a recursive sorting algorithm that works by dividing an array into chunks, sorting them, and combining the chunks together in sorted order.

This algorithm keeps dividing an array into halves until each chunk only has one element. 
Then, the merge function puts the chunks back together in sorted order.

## Functions
There are two important functions related to merge sort:
- Merge: This function sorts two arrays by combining them in order.
- Merge sort: This function creates the two halves to merge together with the merge function. 
It also calls itself on the left and right halves in order to sort them.

![_config.yml]({{ site.baseurl }}/images/MergeSort/MergeSort.png)

## Steps
Steps for the merge sort function:
1. Find the index of the midpoint of the array.
2. Using the midpoint index, create two new arrays, dividing the array into a left half and a right half.
3. Call merge sort on the left array.
4. Call merge sort on the right array.
5. Call the merge function to combine the left and right halves in sorted order.
6. Continue until each half has a size of 1. This is the base case.


Merge function steps:
1. Pass in the original array, the left array, and the right array. We assume the left and right arrays are sorted.
2. Add the smallest element from either the left or the right array to the original array, starting at index 0.
This will write over the original array elements.
3. Repeat step 2 until one of the halves are empty.
4. Add the remaining elements from the leftover array.

## Time Complexity
Best-case, average, and worst-case time complexity: \\(O (n \ log \ n)\\)

## More Resources
Below are some more resources to learn about merge sort:

[GeeksforGeeks - Merge Sort](https://www.geeksforgeeks.org/merge-sort/)

[YouTube - Merge Sort by HackerRank](https://www.youtube.com/watch?v=KF2j-9iSf4Q)