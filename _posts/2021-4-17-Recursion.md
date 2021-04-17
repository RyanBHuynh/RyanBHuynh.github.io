---
layout: post
title: Recursion
---

[Recursion](https://ryanbhuynh.github.io/Recursion/) solves large problems by breaking a large problem into smaller problems, then combining the solutions to the smaller problems into one big solution.

## How Recursion Works
Recursive algorithms have two steps:
1. The base case
2. The recursive step

The base case is the step that breaks out of a recursive loop. This step is a lot like the condition in a for loop or a while loop.

The recursive step is the part where the program solves a smaller version of the problem. 

## Factorial Example 
Suppose we want a program that returns the factorial of an integer.
We can implement this with or without recursion.

The program without recursion looks something like this:  

![_config.yml]({{ site.baseurl }}/images/Recursion/nonRecursiveFactorial.png)

Here, the factorial of n is calculated with a while loop. 
We initialize factorial to 1 so that we can multiply numbers to it inside the while loop.
n is decremented each time the while loop runs, up until n equals 1.

The program with recursion looks like this:

![_config.yml]({{ site.baseurl }}/images/Recursion/recursiveFactorial.png)

Here, the first two if statements are the base case. 
It's impossible to find the factorial of a negative number, so we want to make sure n is not negative.
Otherwise the function would go haywire.

The second if statement makes sure that the function returns 1 when n equals zero or n equals one, since \\(0!\\) and \\(1!\\) both equal one.

The recursive step is inside the else statement. It multiplies n by the number that comes before n, all the way up until n equals one.

We can tell this is a recursive function because the function calls itself inside the function with a smaller version of the same problem.

## More resources
Below are some more resources to learn about recursion:

[GeeksforGeeks - Recursion](https://www.geeksforgeeks.org/recursion/)

[YouTube - Recursion by HackerRank](https://www.youtube.com/watch?v=KEEKn7Me-ms)
