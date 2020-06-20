Someone once said 'The Collatz Conjecture is a really infamous conjecture
which wastes both time and energy.'

So here is my contribution to this nonsense! I saw a news article about it and
decided to code this function for fun.

The function calculates the Collatz Conjecture steps and wasted computing
time and prints them.
    
The idea of the algorithm is shortly this:

  Check if input number is positive integer
  
  Repeat until you reach number 1:
  
    If the number is even:
      Divide by 2
      
    If the number is odd:
      Multiply by 3 and add 1
      
If the conjecture holds true, the result should be one for all positive integers.
