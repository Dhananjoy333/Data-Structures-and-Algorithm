## Arrays / List

In python list is created using []. 

### Important DSA Patterns related to List 

1. Two Pointders :
    - Use two indices that move toward each other or in the same direction.

    ```py
    left = 0
    right = len(arr) - 1
    while left < right:
        # process
        left += 1
        right -= 1
    ```
    - Problems:

        - Reverse array
        - Two Sum (sorted)
        - Container With Most Water
        - Remove duplicates from sorted array
        - 3Sum
    - Time: Usually O(n)

2. Sliding Window :
    - Maintain a window of elements.
    ```py
    left = 0
    for right in range(len(arr)):
    # expand window
        while condition:
            # shrink window
            left += 1
    ```
    - Problems:

        - Maximum sum subarray of size k
        - Longest substring without repeating characters
        - Minimum size subarray sum

    - Time: O(n)

3. Prefix Sum:
    - Precompute cumulative sums.
    ```py
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] + num)

    # Sum from l to r
    sum_lr = prefix[r + 1] - prefix[l]
    ```
    - Problems:

        - Range sum queries
        - Subarray sum equals k
        - Equilibrium index

    - Time: O(n)
    
### Common array methods in Python

| Method             | Description                              | Example                |
| ------------------ | ---------------------------------------- | ---------------------- |
| `append(x)`        | Adds an element to the end               | `arr.append(5)`        |
| `extend(iterable)` | Adds multiple elements                   | `arr.extend([4,5])`    |
| `insert(i, x)`     | Inserts at index `i`                     | `arr.insert(1, 10)`    |
| `remove(x)`        | Removes first occurrence of `x`          | `arr.remove(3)`        |
| `pop([i])`         | Removes and returns element at index `i` | `arr.pop()`            |
| `clear()`          | Removes all elements                     | `arr.clear()`          |
| `index(x)`         | Returns index of first occurrence        | `arr.index(5)`         |
| `count(x)`         | Counts occurrences of `x`                | `arr.count(2)`         |
| `sort()`           | Sorts the list in ascending order        | `arr.sort()`           |
| `reverse()`        | Reverses the list in place               | `arr.reverse()`        |
| `copy()`           | Creates a shallow copy                   | `new_arr = arr.copy()` |

