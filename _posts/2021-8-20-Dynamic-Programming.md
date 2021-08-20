---
layout: post
title: Dynamic Programming
---

Dynamic programming (DP) optimizes solutions to [recursive problems](https://ryanbhuynh.github.io/Recursion/) by combining previously computed solutions to subproblems.
DP minimizes repeated calls with the same inputs because results to prior calls are stored for later use.

## Top-Down/Memoized Approach
The top-down approach breaks down the original value into small values, solving subproblems with the small values, and then using their results to get the solution to the original value. The results are stored in case they are needed later on.

This method is also called memoization. *Memoization* is **NOT** the same as *memorization*. It's very easy to get the two mixed up.

## Bottom-Up/Tabulation Approach
The bottom-up approach starts with a base case and builds off of it until a solution is found to the original problem.
We start off by solving subproblems with small values and build up from that to solve the original problem.

This method is also called tabulation.

## Fibonacci Example
[Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) are calculated as the sum of the previous two numbers, starting with 1 and 1.
The sequence starts as \\(1,1,2,3,5, ...\\) and so on.

We can use recursion to find the nth Fibonacci number. 
In C, a recursive function to find the nth Fibonacci number looks like this:

<img src="/images/DP/FibonacciNaive.png" alt="A recursive formula finding the nth Fibonacci number" width="600"/>

Looks pretty simple, right? 
The problem is, the function has \\(O(n^2)\\) time complexity. 

This is because the function recalculates smaller Fibonacci numbers each time the function is called, even if they were already calculated. We can improve the function by caching values that have already been computed.

### Top-Down Approach
In this function, we use a memoized array and recursively call the Fibonacci function to get the result. 
We start off with \\(n\\), break it down into smaller numbers, store the results for smaller Fibonacci numbers, and use that to find our result.

Steps:
1. In your main function, create an integer array of size \\(n+1\\). This memo array will store calculated Fibonacci numbers so that we don't have to recalculate them. 
2. Create a Fibonacci function that takes in \\(n\\) and the memo array.
3. In the function, if \\(n\\) already has a value in the memo array, return its Fibonacci number.
4. If \\(n\\) is 1 or 2, set \\(memo[n]\\) to 1 and return 1.
5. Otherwise, call the Fibonacci function on \\(n-1\\) and \\(n-2\\), add up their values, and store the sum in \\(memo[n]\\).
6. Return \\(memo[n]\\).

### Bottom-Up Approach
This function works by starting at the first and second Fibonacci numbers and building up until the nth Fibonacci number is reached.
We store the calculated values in a tabulation array.

1. Create a Fibonacci function that takes in \\(n\\).
2. In the function, create a tabulation array of size \\(n+1\\).
3. Set \\(tab[1]\\) and \\(tab[2]\\) to 1.
4. Create a for loop where \\(i\\) goes from 3 to \\(n+1\\). The for loop stops after \\(i\\) reaches \\(n\\).
    5. Set \\(tab[i]\\) to the sum of \\(tab[i-1] + tab[i-2]\\).
6. Return \\(tab[n]\\).

## Time Complexity
Original function time complexity: \\(O(n^2)\\)

Top-down function and bottom-up function time complexity: \\(O(n)\\)

## More Resources
Below are some more resources to learn about dynamic programming and memoization:

[GeeksforGeeks - Dynamic Programming](https://www.geeksforgeeks.org/dynamic-programming/)

[GeeksforGeeks - Memoization (1D, 2D and 3D)](https://www.geeksforgeeks.org/memoization-1d-2d-and-3d/)

[YouTube - Memoization and Dynamic Programming by HackerRank](https://www.youtube.com/watch?v=P8Xa2BitN3I)