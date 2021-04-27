---
layout: post
title: Linked Lists
---

A linked list is a data structure that implements a list using nodes that point to successive members of a list. Below is a picture of a linked list with four nodes.

![_config.yml]({{ site.baseurl }}/images/LinkedList/fourNodeLinkedList.png)

## Characteristics of a Linked List
Each node consists of two parts: the data and a pointer to the next node. Each linked list has a starting node called the head. 
The head has an **item** and a **next pointer** pointing to the next node in the linked list. 
That node has an item and a next pointer pointing to another node, and so on.

This happens up until the last node. The last node has an item and a next pointer pointing to NULL.
The last node can also be called the tail node.

## Linked List Functions
Once we create our linked list, we can create various functions that let users interact with the linked list.
Some functions that we can create include:
* A function that adds an item at a certain index.
* A function that deletes an item at a certain index.
* A function that can search for an item, either by index or directly for the item itself.
* A function that deletes a specific item.
* A function that returns the size of the linked list. 

#### A function that adds an item at a certain index
Assume we want the function to insert the letter B at index 1.
To implement a function like this, we need it to do the following steps:
1. Create a node and store B in the node.
2. Assign the new node's next pointer to the node at index 1.
3. Reassign the next pointer of the node at index 0 so that it points to the new node.


![_config.yml]({{ site.baseurl }}/images/LinkedList/beforeInsertingAtIndex1.png)

![_config.yml]({{ site.baseurl }}/images/LinkedList/InsertingItemAtIndex1.png)

![_config.yml]({{ site.baseurl }}/images/LinkedList/AfterInsertingAtIndex1.png)

To insert an item at index 0 (also known as the head):
1. Create the new node and store the item in the node.
2. Assign the new node's next pointer to the head node.
3. Reset the head of the linked list to the new node.

To insert an item at the tail:
1. Check whether the index is in a valid range. The index can't be negative or larger than the size of the linked list.
2. Check if the index is at the tail. If we start indexing at 0, then the tail should be the size of the linked list.
3. Create the new node and store the item in the node.
4. Assign the new node's next pointer to NULL, since it becomes the new tail node in the linked list.
5. Set the old tail's next pointer to the new tail node.

#### A function that deletes an item at a certain index
Make sure the function checks whether the index is at the head or at the tail

To delete an item at index 0:
1. Set the head to the node after the head node.
2. Free the head node.

To delete an item at the tail:
1. Create a node that traverses the linked list up to the node that points to the tail node.
2. Set the next pointer of that node to NULL.
3. Free the tail node.

To delete an item somewhere in the middle:
1. Create a node that traverses the linked list up to the node that points to the node to delete.
2. Reassign that node's next pointer to point to the node after the node to delete.
3. Free the deleted node.

![_config.yml]({{ site.baseurl }}/images/LinkedList/DeletingAtIndex2.png)

## Advantages of a linked list
Linked lists have a number of advantages over a traditional array:
* Linked lists don't have a defined size. This means you can easily change the size of a linked list by adding or removing items. You can't change the size of an array.
* Linked lists are not stored in one contiguous block of memory, but arrays are.
* Adding or removing items from a linked list is much faster than with a normal array. You don't have to shift items as you do with arrays.

## Disadvantages of a linked list
However, linked lists do have some disadvantages:
* Searching by index is slower with a linked list than an array. You have to traverse through the linked list until you reach your desired index.
* A pointer has to be stored with each item in a linked list. In arrays, you only need to store the item itself. This means that a linked list uses more storage than an array of the same size.

## More Resources

Below are some more resources to learn about linked lists:

[Linked List Data Structure by GeeksForGeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)

[YouTube - Data Structures: Linked Lists by HackerRank](https://www.youtube.com/watch?v=njTh_OwMljA)

[Linked Lists on Learn-C.org](https://www.learn-c.org/en/Linked_lists)

