---
layout: post
title: Linked Lists
---

A linked list is a data structure that implements a list using nodes that point to successive members of a list. Below is a picture of a linked list with four nodes.

![_config.yml]({{ site.baseurl }}/images/fourNodeLinkedList.png)

## Characteristics of a linked list
Each node consists of two parts: the data and a pointer to the next node. Each linked list has a starting node called the head. 
The head has an **item** and a **next pointer** pointing to the next node in the linked list. 
That node has an item and a next pointer pointing to another node, and so on.

This happens up until the last node. The last node has an item and a next pointer pointing to NULL.
The last node can also be called the tail node.

## Linked list functions
Once we create our linked list, we can create various functions that let users interact with the linked list.
Some functions that we can create include:
* A function that adds an item at a certain index.
* A function that deletes an item at a certain index.
* A function that can search for an item, either by index or directly for the item itself.
* A function that deletes a specific item.
* A function that prints the entire linked list, regardless of how big the linked list is. 

## Advantages of a linked list
Linked lists have a number of advantages over a traditional array:
* Linked lists don't have a defined size. This means you can easily change the size of a linked list by adding or removing items. You can't change the size of an array.
* Linked lists are not stored in one contiguous block of memory, but arrays have to be.
* Adding or removing items from a linked list is much faster than with a normal array. You don't have to shift items as you do with arrays.

## Disadvantages of a linked list
* Searching by index is slower with a linked list than an array. You have to traverse through the linked list until you reach your desired index.
* A pointer has to be stored with each item in a linked list. In arrays, you only need to store the item itself. This means that a linked list uses more storage than an array of the same size.

## More resources

Below are some more resources to learn about linked lists:

[Linked List Data Structure by GeeksForGeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)

[YouTube - Data Structures: Linked Lists by HackerRank](https://www.youtube.com/watch?v=njTh_OwMljA)

[Linked Lists on Learn-C.org](https://www.learn-c.org/en/Linked_lists)

