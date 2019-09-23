Solutions to problems sent by dailycodingproblem.com

---

**Problem 1**

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

[Solution](problem_1.py)

---

**Problem 2**

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

[Solution](daily_coding_problem/problem_2)

---

**Problem 3**

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

[Solution](daily_coding_problem/problem_3)

---

**Problem 4**

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

[Solution](daily_coding_problem/problem_4)

---

**Problem 5**

---

**Problem 6**

---

**Problem 7**

---

**Problem 8**

---

**Problem 9**

---

**Problem 10**

---

**Problem 11**

---

**Problem 12**

---

**Problem 13**

---

**Problem 14**

---

**Problem 15**

---

**Problem 16**

---

**Problem 17**

---

**Problem 18**

---

**Problem 19**

---

**Problem 20**

---

**Problem 21**

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

[Solution](problem_20.py)
