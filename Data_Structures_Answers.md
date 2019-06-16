Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(n) - driven by the for-loop search for the oldest item

2. What is the space complexity of your ring buffer's `append` function?
O(1) - adds 1 item to the list each time

3. What is the runtime complexity of your ring buffer's `get` method?
O(n) - driven by the check of whether each item is a None or not

4. What is the space complexity of your ring buffer's `get` method?
O(n) - creates and returns a new filtered array with the list comprehension

5. What is the runtime complexity of the provided code in `names.py`?
O(n^2) - nested for-loops running simple O(1) comparison check

6. What is the space complexity of the provided code in `names.py`?
O(n) - up to O(n) if every name is a duplicate and has to be stored in the duplicates list

7. What is the runtime complexity of your optimized code in `names.py`?
O(n(log(n))) - driven by the runtime complexity of the in-built python sort function

8. What is the space complexity of your optimized code in `names.py`?
O(n) - up to O(n) if every name is a duplicate and has to be stored in the duplicates list