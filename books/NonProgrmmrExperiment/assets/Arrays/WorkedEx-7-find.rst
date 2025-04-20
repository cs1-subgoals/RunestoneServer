Worked Example: Arrays - Find Value
=================================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: yiDELtNKP9U
   :divid: video-arrays-we7
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: Assume that the integer array ``alpha`` has been properly declared and is full of data values, and that the variable ``target`` is an int with a value in it. Evaluate these statements and determine the value of ``loc``. If any error occurs, give the reason.

.. code-block:: java
   
   int loc = -1;
   boolean found = false;
   for (int i = 0; i < alpha.length && !found; i++) {
      if (alpha[i] == target) 	{
         loc = i;  found = true;  
   }
   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Set up array from 0 to size-1

   .. figure:: Figures/we4-init.png
      :alt: Instantiated Array
      :scale: 50%   
   
   - alpha is an array of ints and has values, but we don’t know what those values are
   - however, we can still diagram a representation of this array
   - notice that the largest index is size - 1

   
.. topic:: SG2: Evaluate data type of statements against array

   References to the array are in the loop and selection statements:

   .. code-block:: java
 
      for (int i = 0; i < alpha.length && !found; i++) {
         if (alpha[i] == target) 	{
            loc = i;  found = true;  
      }

   - This loop has index i go from 0 to size - 1 (<length) by increments of 1.
   - Then the value at alpha[i] is compared to the int value of target.  
   - If the value at alpha[i] is equal to target, then the value i is copied into loc.
   - All indexes into the array are valid, and all assignments are valid.

.. topic:: SG3: Trace statements, updating slots as you go

   Let us trace with a sample array and assume the value of ``target`` is 15.
   
   .. figure:: Figures/we4-sample.png
      :alt: Sample Array
      :scale: 50%  

   The first statement, ``int loc = -1;`` gives ``loc`` a value that is not a valid index for any array.
   
   Then a for-loop is used to traverse the array and compare each element to ``target``. The chart below uses one line to represent the memory and comparisons during each iteration of the loop, starting when i has a value of zero.
   
   .. figure:: Figures/we7-trace.png
      :alt: Trace searching for target
      
   When we find the target value in the array, we store the index (location) of where it is in the array. 

   Some questions to consider:
   
   1. What would happen if the ``target`` value is not in the array? Then the selection statement is never true, and ``loc`` is never changed from its initial value of -1. 
   
   2. Why is -1 a good initial value for ``loc``? It is not a valid index for any array. You or another programmer using this algorithm could check the value of  ``loc`` to make a decision (selection!) for how the program will behave when the ``target`` value is found or not found at a valid array index.
   
   3. What would happen if there were 2 occurrences of the target value in the array? The loop does not end when the ``target`` value is found, so additional occurences would overwrite the value of ``loc`` with the **last** occurence.
   
   The more general answer to the original question is: "``loc`` contains the index of the last occurrence of ``target`` in the array ``alpha`` or -1 if ``target`` is not in the array."
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we7-p1.rst