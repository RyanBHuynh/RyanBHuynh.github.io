---
layout: post
title: Stacks and Queues
---

This article covers stacks and queues and the functions associated with each abstract data type.

## Stacks
Stacks are a special kind of list ADT where items can only be added to and removed from the "top".
Stacks support two main functions: pushing and popping. With stacks, you add and remove items by using push and pop functions.

### Stack Functions
Pushing to a stack means adding an item to the top of a stack.
Popping from a stack means removing an item from the top and returning it back to the calling function.

![_config.yml]({{ site.baseurl }}/images/StacksAndQueues/PushingAndPoppingStacks.png)

These two functions make stacks a last-in-first-out (LIFO) data structure. This means the last item pushed onto a stack will be the first item popped from the stack.

## Queues
Queues are a special List ADT where items are added to the back and removed from the front.
Like stacks, queues have two main functions to add and delete items.

### Queue Functions
Enqueuing adds an item to the back of a queue, while dequeuing removes an item from the front of the queue and returns it to the calling function.

![_config.yml]({{ site.baseurl }}/images/StacksAndQueues/EnqueuingAndDequeuing.png)

These functions make queues a first-in-first-out (FIFO) data structure. The first item put into the queue will be the first item removed from the queue.

## More Resources
Below are some more resources to learn about stacks and queues:

[YouTube - CS50: Stacks](https://www.youtube.com/watch?v=hVsNqhEthOk)

[YouTube - CS50: Queues](https://www.youtube.com/watch?v=3TmUv1uS92s)

