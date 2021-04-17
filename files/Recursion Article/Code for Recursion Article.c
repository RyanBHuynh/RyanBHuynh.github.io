#include <stdio.h>

unsigned int nonRecursiveFactorial(int n) //Calculates n! without using recursion
{
    if(n < 0)
    {
        return 0;
    }
    
    int factorial = 1;
    while(n >= 1)
    {
        factorial = factorial*n;
        n--;
    }

    return factorial;
}

unsigned int recursiveFactorial(int n)
{
    if(n < 0) //Base case
    {
        return 0;
    }

    else if (n == 0 || n == 1) //Base case
    {
        return 1;
    }

    else //Recursive step
    {
        return n*recursiveFactorial(n-1); 
    }
}

int main(void)
{
    int num = 10;
    printf("recursiveFactorial(num) = %d\n",recursiveFactorial(num));
    printf("nonRecursiveFactorial(num) = %d\n",nonRecursiveFactorial(num));
}