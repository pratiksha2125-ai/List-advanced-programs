📘 Python Lists – Advanced Programs README
📌 Overview

Python lists are one of the most commonly used data structures. They allow storing multiple values in a single variable and support many operations like sorting, searching, merging, inserting, deleting, and more.

This README covers advanced list programs that are commonly asked in interviews, college practicals, and coding competitions.

📚 Topics Covered
Bubble Sort
Selection Sort
Insertion Sort
Merge Two Lists
Merge Sorted Lists
Remove Duplicates
Find Largest and Smallest Element
Find Second Largest Element
Reverse a List
Rotate List
Linear Search
Binary Search
Count Frequency of Elements
Split List into Even and Odd
Find Common Elements
Find Missing Number
Flatten Nested List
Remove Empty Lists
List Comprehension
Matrix Operations using Lists
1. Bubble Sort
Definition

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

Algorithm
Compare adjacent elements.
Swap if left element is greater.
Repeat until list becomes sorted.
Time Complexity
Best	Average	Worst
O(n)	O(n²)	O(n²)
Example

Before

[5,2,4,1,3]

After

[1,2,3,4,5]
2. Selection Sort
Definition

Selection Sort repeatedly selects the smallest element and places it at the correct position.

Algorithm
Find minimum element.
Swap with first unsorted element.
Repeat.
Time Complexity
Best	Average	Worst
O(n²)	O(n²)	O(n²)

Example

[7,5,3,8,2]

↓

[2,3,5,7,8]
3. Insertion Sort
Definition

Builds the sorted list one element at a time by inserting each element into its correct position.

Time Complexity
Best	Average	Worst
O(n)	O(n²)	O(n²)

Example

Before
[9,4,7,2]

After

[2,4,7,9]
4. Merge Two Lists
Definition

Combines two lists into one list.

Example

list1=[1,2,3]
list2=[4,5,6]

Output

[1,2,3,4,5,6]

Methods

extend()
append()
unpacking (*)
5. Merge Two Sorted Lists

Example

List1=[1,3,5]
List2=[2,4,6]

Output

[1,2,3,4,5,6]

Used in Merge Sort.

6. Remove Duplicate Elements

Example

Before

[2,5,2,1,3,5,7]

After

[2,5,1,3,7]

Methods

set()
Loop
Dictionary
7. Find Largest and Smallest Element

Example

numbers=[12,45,7,89,22]

Output

Largest = 89
Smallest = 7

Methods

max()
min()
Loop
8. Find Second Largest Number

Example

[5,8,3,9,1]

Output

Second Largest = 8

Methods

Sorting
Loop
9. Reverse a List

Methods

reverse()
Slicing
Loop

Example

Before

[1,2,3,4]

After

[4,3,2,1]
10. Rotate List

Left Rotation

[1,2,3,4,5]

↓

[2,3,4,5,1]

Right Rotation

[1,2,3,4,5]

↓

[5,1,2,3,4]
11. Linear Search

Checks every element one by one.

Example

Search 8

Output

Element Found

Time Complexity

O(n)
12. Binary Search

Works only on sorted lists.

Example

[2,4,6,8,10]

Search

8

Output

Found

Time Complexity

O(log n)
13. Count Frequency

Example

[2,3,2,5,3,2]

Output

2 -> 3 Times

3 -> 2 Times

5 -> 1 Time

Methods

count()
Dictionary
14. Split Even and Odd

Input

[2,5,6,9,8]

Output

Even

[2,6,8]

Odd

[5,9]
15. Find Common Elements

Input

A=[1,2,3,4]

B=[3,4,5,6]

Output

[3,4]

Methods

Loop
Set Intersection
16. Find Missing Number

Example

[1,2,3,5]

Output

4

Methods

Formula
XOR
Loop
17. Flatten Nested List

Input

[[1,2],[3,4],[5]]

Output

[1,2,3,4,5]

Methods

Nested Loop
List Comprehension
18. Remove Empty Lists

Input

[[],[1,2],[],[3]]

Output

[[1,2],[3]]
19. List Comprehension

Creates lists in one line.

Example

numbers=[1,2,3,4,5]

Output

Squares

[1,4,9,16,25]

Advantages

Short code
Faster
Easy to read
20. Matrix Operations using Lists

Operations

Matrix Addition
Matrix Multiplication
Matrix Transpose
Identity Matrix
Diagonal Sum

Example

A

1 2
3 4

B

5 6
7 8

Addition

6 8
10 12
📊 Comparison of Sorting Algorithms
Algorithm	Best	Average	Worst	Stable
Bubble Sort	O(n)	O(n²)	O(n²)	✅ Yes
Selection Sort	O(n²)	O(n²)	O(n²)	❌ No
Insertion Sort	O(n)	O(n²)	O(n²)	✅ Yes
Merge Sort	O(n log n)	O(n log n)	O(n log n)	✅ Yes
🎯 Learning Outcomes

After completing these programs, you will understand:

List operations
Sorting algorithms
Searching algorithms
Merging lists
Removing duplicates
Matrix operations
List comprehension
Time complexity (Big O)
Problem-solving using lists
Interview-level list programming
📂 Suggested Project Structure
Python-List-Programs/
│
├── BubbleSort.py
├── SelectionSort.py
├── InsertionSort.py
├── MergeLists.py
├── MergeSortedLists.py
├── ReverseList.py
├── RemoveDuplicates.py
├── BinarySearch.py
├── LinearSearch.py
├── RotateList.py
├── MatrixOperations.py
├── FlattenList.py
├── FrequencyCount.py
└── README.md
