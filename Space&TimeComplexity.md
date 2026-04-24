Time complexity measures how the running time of an algorithm increases as the size of the input grows. It helps predict how fast an algorithm will run for large inputs. For example, if an algorithm has O(n) time complexity, its running time increases linearly with the input size.Usually expressed with asymptotic notation (Big O for worst-case, Θ for tight bound, Ω for best-case)

Space complexity measures how much extra memory an algorithm needs as the input size grows. It helps predict how much memory will be used for large inputs. For example, O(1) space complexity means the algorithm uses a constant amount of extra memory, regardless of input size.

O(1): No loops or recursion; constant operations.
O(log n): Problem size is halved or reduced exponentially (e.g., binary search).
O(n): Single loop iterating over the input.
O(n log n): Divide-and-conquer algorithms (e.g., Merge Sort, Quick Sort).
O(n²): Nested loops iterating over the input.
O(2ⁿ): Recursive algorithms exploring all possibilities.
O(n!): Algorithms generating all permutations or combinations.


Space complexity measures the amount of memory an algorithm uses as a function of the input size n. It includes both:

Auxiliary Space: Extra memory used by the algorithm (e.g., variables, data structures, recursion stack).
Input Space: Memory required to store the input data.
