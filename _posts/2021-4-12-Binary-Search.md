---
layout: post
title: Binary Search
---

Binary search looks up an item in a sorted array by dividing the search space by 2 until the item is found.

## How Binary Search Works
Binary search has a few steps. Here's how it works:

First, before you start, make sure you are using a sorted array. 
Binary search needs the array to be sorted for it to work effectively.

Steps:  
1. Find the lowest index and highest index in the array.
2. Find the middle element's index using this formula: \\(mid = \frac{low index + high index}{2}\\)
3. If the middle index points to the number we're looking for, return the middle index.
4. If the number at the middle index is larger than the number we're looking for, set the high index using this formula: \\(high = mid - 1\\) 
We only want to search through the numbers less than the middle index.
5. If the number at the middle index is smaller than the number we're looking for, set the low index using this formula: \\(low = mid + 1\\)
This way we only search through numbers larger than the number in the middle.
6. Repeat steps 2 through 5 until the middle index points to the number we're looking for.

## Example
Here's a sorted array:

![_config.yml]({{ site.baseurl }}/images/BinarySearch/StartingArray.png)

Let's find the number 8 using binary search.
1. Find the low, high, and middle index.

![_config.yml]({{ site.baseurl }}/images/BinarySearch/ArrayWithIndexes.png)

2. Because \\(8 > 6\\), we move the low index up so that it points to 7.

![_config.yml]({{ site.baseurl }}/images/BinarySearch/LowIndexMovedUp.png)

3. Then we check what the middle index points to, and it points to 8.  
The index we are looking for is 5.

## Runtime of Binary Search
The best case time complexity for binary search is \\(O(1)\\). 
This happens when the number we're looking for lands directly in the middle of the array.  
Otherwise, the average and worst case time complexity is \\(O(log n)\\).

## More resources
Below are some more resources to learn about Binary Search:

[GeeksforGeeks - Binary Search](https://www.geeksforgeeks.org/binary-search/)
[YouTube - Binary Search by HackerRank](https://www.youtube.com/watch?v=P3YID7liBug)
