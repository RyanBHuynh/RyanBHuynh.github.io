---
layout: post
title: Vectors and ArrayLists
---

Vectors and ArrayLists are arrays without a preset size. 
This allows the vector to automatically adjust to the number of elements it currently stores.

## Basics of Vectors
Vectors in C++ are called ArrayLists in Java. 
Vectors operate much like arrays do. 
In C++, to access a vector element, use the index operator the same way you would with an array.
Vectors can only store one data type.

Whenever a vector is full and another element is added, the size of the vector goes up. 
The vector will usually double in size to minimize how often the vector is resized.

## Creating Vectors
If you are using C++, be sure to compile with C++11 or later.
Also remember to include the vector library.

Below is a picture of a vector being created in C++. 
Like arrays, elements can be initialized on the same line as the vector itself.

![_config.yml]({{ site.baseurl }}/images/VectorsAndArrayLists/InitializedVector.png)

In the example above, an integer vector called intVector is created and stores the integers 1,2, and 3.
The vector's data type goes inside the angle brackets.

## Vector Methods
Below are a list of handy vector methods in C++:
- size: Returns the size of the vector
- push_back: Takes in a value as a parameter and adds it to the end of the vector
- pop_back: Deletes the last element in the vector
- empty: Checks if the vector is empty
- front: Returns the first element in the vector
- back: Returns the last element in the vector

## Time Complexity
Worst-case time complexity for inserting or deleting at the end of the vector only happens when the size of vector itself is changed. 
This does not happen most of the time.

Access time complexity: \\(O(1)\\)

Insert or delete at the end of vector worst-case time complexity: \\(O(n)\\)

Insert or delete at the end of vector average time complexity: \\(O(1)\\)

## More Resources
Below are some more resources to learn about Vectors and ArrayLists:

[GeeksforGeeks - Vector in C++ STL](https://www.geeksforgeeks.org/vector-in-cpp-stl/)
[W3Schools - Java ArrayList](https://www.w3schools.com/java/java_arraylist.asp)