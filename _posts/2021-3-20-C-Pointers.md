---
layout: post
title: Pointers in C
---

In computers, memory stores information that the computer needs right now. 
This is different from storage, which is used to hold information over long periods of time.   
In C, pointers are variables that store memory addresses. Memory addresses point to locations in memory, much like how a house address points to someone's house. 

Variables are stored in memory, so we can use pointers to access those variables.
Pointers can be of a specific data type, like an integer pointer or a character pointer. They can also be of any data type, like a void pointer.

### Declaring and initializing pointers
Here is how you declare an integer pointer in C:  
<span style="Courier New">
int* intPtr;
</span>

As you can see, we have the data type int followed by an asterisk. The asterisk indicates that the variable is a pointer.

Below, we have an integer variable called foo which has the value 3.
Here is an example of assigning a memory address to a pointer:  
<span style="Courier New">
int foo = 3;  
int* intPtr;  

intPtr = &foo;  '
</span>

The "&" in front of <span style="Courier New">foo</span> means "the memory address of". So <span style="Courier New">&foo</span> is the address of <span style="Courier New">foo</span>.
Putting all of this together, <span style= "Courier New">intPtr = &foo</span> says "assign the memory address of <span style="Courier New">foo</span> to the pointer <span style="Courier New">intPtr</span>".
Now, <span style="Courier New">intPtr</span>  points to the address of <span style="Courier New">foo</span>. What if we want to use the pointer to find out the value of <span style="Courier New">foo</span>? To do that, we need to dereference the pointer.

### Dereferencing pointers
Pointers are references to variables. So if we want to access the variable itself, we dereference the pointer to that variable.
To dereference means to access the value at the address that a pointer points to.
So if the pointer <span style="Courier New">intPtr</span>  points to <span style="Courier New">foo</span>, dereferencing<span style="Courier New">intPtr</span> would give the value of <span style="Courier New">foo</span>.

To dereference a pointer, we would type this: <span style="Courier New">*intPtr</span>
Because <span style="Courier New">intPtr<\span> points to <span style="Courier New">foo</span>, if we print both <span style="Courier New">*intPtr</span> and <span style="Courier New">foo</span> out, we would get the same values.
That is, if we ran the following code, the number 3 would be printed on both lines:  
<span style="Courier New">
printf("%d\n",foo);  
printf("%d\n",*intPtr);  
</span>

![_config.yml]({{ site.baseurl }}/images/LinkedList/fourNodeLinkedList.png)

### Uses for pointers
Why use pointers in the first place? We can use pointers to do things only possible with pointers
* Dynamic memory allocation
* Implementing data structures
* Letting functions change the variable values (pass by reference)
* They work as arrays and strings

## More resources
Below are some more resources to learn about pointers in C:

[Pointers in C and C++ by GeeksForGeeks](https://www.geeksforgeeks.org/data-structures/linked-list/)

[Pointers on Learn-C.org](https://www.learn-c.org/en/Pointers)

