---
layout: post
title: Big O Notation
---

Big O (big-oh) notation gives computer scientists a way to show how complex an algorithm is.

## Basics of Big O
Big O notation can be used to show how much time it takes to run a program as the input size increases.
You can use Big O to compare a program's efficiency no matter what programming language it was written in or what machine the program runs on.

## Finding a program's big O complexity
To find a program's big O complexity, we need to accomplish the following tasks:
1. Find the big O complexity of each line and add them all up.
2. Ignore any constants and any terms that aren't dominant.
3. Assume the worst-case scenario, which is the longest possible time it takes for the program to run.

For example, look at the following two lines of C code:

![_config.yml]({{ site.baseurl }}/images/BigONotation/FooAndBar.png)

1. Assigning values to variables takes constant time. This means that no matter how large the value is, assigning it to a variable takes the same amount of time.
In Big O terms, constant time is \\((O(1)\\) (pronounced big-oh of one). Because both lines are O(1), adding \\(O(1) + O(1) = O(2)\\). 
2. We can actually simplify \\(O(2)\\) by treating 2 as a constant: \\(O(2) = O(2 \bullet 1)\\). Because we remove the constant, this simplifies down to \\(O(1)\\).
We only have one term, so there is no need to worry about non-dominant terms.
3. Luckily for the above lines of code, the best-case, average-case, and worst-case scenario are all the same.

After following these steps, we find that the Big O complexity is \\(O(1)\\).

### Example Complexities
Below is a list of example runtimes:


| Runtime        | Big O Notation  | Example Algorithm             |
|----------------|-----------------|-------------------------------|
| Constant time  | \\(O(1)\\)      | Accessing an array element    |
| Linear time    | \\(O(n)\\)      | Finding the sum of an array   |
| Quadratic time | \\(O(n^2)\\)    | Finding the sum of a 2D array |


| Column 1 Header | Column 2 Header | Column 3 Header |
| --------------- | --------------- | --------------- |
| Row 1 Column 1 | Row 1 Column 2 | Row 1 Column 3 |
| Row 2 Column 1 | Row 2 Column 2 | Row 2 Column 3 |
| Row 3 Column 1 | Row 3 Column 2 | Row 3 Column 3 |

$$ E = m\cdot c^2 \label{eq:mc2}$$

## More resources
Below are some more resources to learn about Big O Notation:

[Big O Cheat Sheet](https://www.bigocheatsheet.com/)

