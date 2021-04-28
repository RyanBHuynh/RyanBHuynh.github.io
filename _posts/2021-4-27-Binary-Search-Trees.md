---
layout: post
title: Binary Search Trees
---

A binary search tree (BST) is a tree data structure set up to make binary search efficient.

## Example Binary Search Tree
Below is a picture of a BST:

![_config.yml]({{ site.baseurl }}/images/BinarySearchTrees/BST.png)

## Characteristics of Binary Search Trees
The root node of a binary search tree has all of the following:
- The left node is less than the root node.
- The right node is greater than the root node.
- Each subtree is a binary search tree.

Empty trees are also binary search trees.

## Binary Search Tree Functions
Below are a selection of possible binary search tree functions:  

### Search Function
Here is the algorithm to determine if a number is in a BST:  
1. If the root node is NULL, return False.
2. If the number is root node, return True.
3. If the number is less than the root node, search the left node.
4. If the number is greater than the root node, search the right node.

### Insert Node Function
Here is the algorithm to insert a number into a BST:
1. Pass the root node and the number to insert into the function.
2. If the node is NULL, return a new node that stores the number.
3. If the number is greater than the node, call the insert function on the right node.
4. If the number is less than the node, call the insert function on the left node.
5. Return the root node when all is said and done.

## Time Complexity
The time complexities for searching, inserting into, or deleting from a binary search tree are listed below:  
Average time complexity: \\(O(log \ n)\\)  
Worst-case time complexity: \\(O(n)\\)  

## More Resources
Below are some more resources to learn about binary search trees:

[Wikipedia - Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree)

[Programiz - Binary Search Tree](https://www.programiz.com/dsa/binary-search-tree)
