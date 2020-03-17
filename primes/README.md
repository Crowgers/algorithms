Run using: '''python path/prime_solver.py'''

# Important to note a few things:

1. Fastest way to construct a list however each element references the same
 item in memory.
2. number_list slice starts at the square of the number because all non-prime
 numbers are eliminated by the previous loops (3*2, 4*3 etc.)
3. No endpoint specified due to assignment
4. Step size is n*2 to avoid even numbers
5. (n+2)*i - 1 - i*i is number of integers in n divisible by i
6. This is further divided by 2*i because half of these are even numbers and
 not prime