"""
1.NumPy is a powerful library in Python used for numerical computations,
 especially when dealing with arrays and matrices.
2.In Python, there isn’t a native “real” array type like in some other languages.
 However, NumPy arrays provide an efficient and convenient way to work with large datasets.
3.The performance gains with NumPy are significant. You can achieve up to 50 times faster execution
 compared to standard Python lists when performing numerical operations.
4.While NumPy is implemented in Python, many of its crucial operations are actually 
executed in C and C++, which contributes to its efficiency.
"""

"""
1. everything is an object in python.
2. pyhthon: list stores reference to integer object

In Python, **lists** indeed store **references to objects**. Let me explain this concept further:

1. When you create a list, it acts as a container for holding references to other objects 
   (such as integers, strings, or custom objects).
2. Each element in the list points to the memory location where the actual object resides.
3. list stores the reference or pointer , this ref pointing to given value or object .
3. This means that when you modify an element in the list, you are actually modifying the object it refers to.

For example:
```python
# Create a list with some elements
my_list = [1, 2, 3]

# Modify an element in the list
my_list[0] = 42

# Now, my_list[0] points to a different object (42) in memory
```

4.every reference is 8 byte
5.this is why storing a lot of items in lists has huge memory complexity
6.Remember that Python lists are dynamic and can hold elements of different types.
"""
"""
Contiguous Memory Layout:
NumPy arrays are designed to store data in a contiguous or continuous block of memory.
Unlike Python lists, where elements can be scattered across different memory locations, NumPy ensures that its array elements are stored consecutively.
This contiguous layout allows for efficient access and manipulation of array elements.
    
Homogeneous Data Types:
NumPy arrays are homogeneous, meaning all elements within an array have the same data type (e.g., integers, floats, etc.).
This uniformity enables efficient memory allocation and alignment.
Single Data Type:
When you create a NumPy array, you specify a single data type for its elements.
For example, if you create an array of integers, all elements will be stored as integers. 
"""

"""
List:
Certainly! Let's explore how **lists** in Python store references or pointers to objects, along with an example:

1. **References in Lists**:
   - In Python, a **list** is an ordered collection of elements.
   - Each element in a list is a **reference** to an object (such as an integer, string, or custom class instance).
   - When you add an item to a list, you're actually adding a reference to that item.

2. **Example**:
   ```python
   # Create a list with some elements
   my_list = [10, "hello", [1, 2, 3]]

   # Each element in the list is a reference
   # my_list[0] refers to the integer 10
   # my_list[1] refers to the string "hello"
   # my_list[2] refers to another list [1, 2, 3]

   # Modify an element in the list
   my_list[0] = 42
   # Now, my_list[0] points to a different object (42) in memory

   # Append a new element to the list
   my_list.append("world")
   # The list now contains: [42, "hello", [1, 2, 3], "world"]

   # Nested lists share references
   nested_list = my_list[2]
   nested_list[0] = 100
   # Now, my_list[2] has changed to [100, 2, 3]

   # Deleting an element from the list
   del my_list[1]
   # The list becomes: [42, [100, 2, 3], "world"]
   ```

3. **Important Points**:
   - When you modify an element in the list, you're modifying the object it refers to.
   - Lists can hold elements of different types, and each element is a reference.
   - Understanding references is crucial for memory management and avoiding unexpected behavior.

Remember that Python lists are flexible and versatile due to their reference-based nature! 🐍🔗
"""