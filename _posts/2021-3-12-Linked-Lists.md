---
layout: post
title: Linked Lists
---

### What are linked lists?

A linked list is a data structure that implements a list using nodes that point to successive members of a list. Below is a picture of a linked list.

![_config.yml]({{ site.baseurl }}/images/threeNodeLinkedList.png)

Each node consists of two parts: the data and a pointer to the next node. Each linked list has a starting node called the head. 
The head has the an **item** and a **next pointer** pointing to the next node in the linked list. 
That node has an item and a next pointer pointing to another node, and so on.
This happens up until the last node. The last node has an item and a next pointer pointing to NULL.

### Advantages of a linked list
Linked lists have a number of advantages over a traditional array
* Linked lists don't have a set size. This means you can easily change the size of a linked list by adding or removing items. You can't change the size of an array.
* Linked lists are not stored in one contiguous block of memory, but arrays have to be.
* Adding or removing items from a linked list is much faster than with a normal array. You don't have to shift items like with arrays.

### Disadvantages of a linked list
* Searching by index is slower with a linked list than an array. You have to traverse through the linked list until you reach your desired index.
* A pointer has to be stored with each item in a linked list. In arrays, you only need to store the item itself.
