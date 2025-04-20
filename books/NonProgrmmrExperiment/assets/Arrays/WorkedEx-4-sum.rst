Worked Example: Arrays - Sum
=================================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: 66cpxYpQUyE
   :divid: video-arrays-we4
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: Assume that the integer array ``alpha`` has been properly declared and is full of data values. Evaluate these statements and determine the value of ``sum``. If any error occurs, give the reason.

.. code-block:: java
   
   int sum = 0;

   for (int i = 0; i < alpha.length; i++) {
      sum += alpha[i];
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

   .. code-block:: java
 
      for (int i = 0; i < alpha.length; i++) {
         sum += alpha[i];
      }

   - This loop has index i go from 0 to size - 1 (<length) by increments of 1.
   - Then the value at alpha[i] is added to sum.  
   - All indexes into the array are valid, and all assignments are valid.

.. topic:: SG3: Trace statements, updating slots as you go

   Let us trace with a sample array.
   
   .. figure:: Figures/we4-sample.png
      :alt: Sample Array
      :scale: 50%  

   The first line of the code sample initializes ``sum`` to a have a value of zero, and then a for-loop is used to traverse the array. The chart below uses one line to represent the memory and calculations during each iteration of the loop, starting when i has a value of zero.
   
   .. figure:: Figures/we4-trace.png
      :alt: Trace the loop
      
   The final value of ``sum`` is 59, which s the sum of all values in the array.
   
   The more general answer to the original question is: "``sum`` contains the sum of all the values in the array ``alpha``."
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we4-p1.rst