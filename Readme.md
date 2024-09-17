**Prove the time complexity of the algorithms.**
In the original Fibonacci implementation, each call to fib(n) results in two additional recursive calls, leading to a branching tree structure. At each level of the recursion, there are two child nodes, representing the two recursive calls made at that level. This binary tree-like structure results in an exponential growth of function calls.

The number of function calls at each level follows a power of 2 pattern. Specifically, there are 2^n function calls at level n. Therefore, the total number of function calls in the recursive tree is proportional to 2^n.

Expressed in big-O notation, the time complexity is O(2^n), indicating that the time required by the algorithm grows exponentially with the input size n. This exponential growth leads to inefficiency for larger values of n due to the vast number of redundant calculations.

**Comment on way's you could improve your implementation.**
The original recursive Fibonacci implementation is inefficient for large values of n due to its exponential time complexity, resulting in many redundant calculations.

To improve efficiency, techniques like memoization and dynamic programming can be used. Memoization stores previously computed Fibonacci values in a cache (such as an array or dictionary) to avoid recalculating them. Dynamic programming builds the solution iteratively from the ground up.

By employing these methods, the time complexity can be reduced from exponential to linear O(n), making the algorithm much more efficient and suitable for larger inputs.

