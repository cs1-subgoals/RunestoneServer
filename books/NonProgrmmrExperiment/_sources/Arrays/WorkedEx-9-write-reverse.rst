Worked Example: Arrays - Write a Reversing Algorithm
=================================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: oBC4TfcD0o0
   :divid: video-arrays-we9
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: Write the code to "reverse" the elements of an array.

There are several different approaches you might take. We will examine two options here.
   
---------------------------------------------------------------------------------------------------------

.. topic:: Solution 1 -- copy to new array with reverse traverse

   We will begin with a sample array called ``original``, and another array of the same size called ``copy``.

   .. code-block:: java
      
      int [] original = {2, 4, 6, 8, 10};
      int [] copy = new int [original.length];
   
   Then we loop in reverse for the original array, copying the elements in order and placing them starting at the beginning of the new array. The variable ``place`` helps us with traversing the new array in the opposite direction of our reversed traversal of the original.
   
   .. code-block:: java
   
      int place = 0;
      for (int i = original.length - 1; i >= 0; i++)
         copy[place++] = original[i];
         
.. topic:: Solution 2 -- same array with swaps

   In this solution, we do not need the whole extra array in memory. The loop only traverses **half** of the array, swapping the value at ``i`` with the value at the mirrored/reflected position ``array.length - i - 1``.
   
   .. code-block:: java
   
      for (int i=0; i<array.length/2; i++)  {
         int temp = array[i]; 
         array[i] = array[array.length - i - 1]; 
         array[array.length - i - 1] = temp; 
      }
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we9-p1.rst