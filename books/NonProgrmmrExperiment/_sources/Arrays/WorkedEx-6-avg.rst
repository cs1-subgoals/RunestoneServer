Worked Example: Arrays - Average
=================================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: CzzQ5mxMPOo
   :divid: video-arrays-we6
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: Assume that the integer array ``alpha`` has been properly declared and is full of data values. Evaluate these statements and determine the value of ``avg``. If any error occurs, give the reason.

.. code-block:: java
   
   int sum = 0;
   double avg = 0.0; 
   for (int i = 0; i < alpha.length; i++)
      sum = sum + alpha[i];
   if (alpha.length != 0)
      avg = (sum * 1.0)  / alpha.length;
   
   
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
 
      for (int i = 0; i < alpha.length; i++)
         sum = sum + alpha[i];
      if (alpha.length != 0)
         avg = (sum * 1.0) / alpha.length;


   - This loop has index i go from 0 to size - 1 (<length) by increments of 1.
   - Then the value at alpha[i] is added to sum, an int.  
   - If the size of the array is not 0, then it is divided by the number of values in alpha.
   - All indexes into the array are valid, and all assignments are valid.

.. topic:: SG3: Trace statements, updating slots as you go

   Let us trace with a sample array.
   
   .. figure:: Figures/we4-sample.png
      :alt: Sample Array
      :scale: 50%  

   First, ``sum`` and ``avg`` are both initialized to zero values, and then a for-loop is used to traverse the array to calculate the sum. The chart below uses one line to represent the memory and calculations during each iteration of the loop, starting when i has a value of zero.
   
   .. figure:: Figures/we6-trace.png
      :alt: Trace calculation of sum
      
   Next we look at the selection statement:
   
   .. code-block:: java
   
      if (alpha.length != 0)
         avg = (sum * 1.0) / alpha.length;
         
   In our sample, ``alpha.length`` is 5, and 60 divided by 5 is 12, for a final value of 12 in ``avg``. 
         
   Why have the selection statement? What if the array has been declared, but has no values? Then its size is 0 – and we would be dividing by 0! An exception!  So we guard against this by checking the length.

   Why do we need to multiply sum by 1.0? Remember, an int divided by an int is always an int! Our sample did not have any remainder or decimal value, but that might not always be the case. So we need to make sure that either the divisor or dividend is a double; and one way to do this without affecting the value is to multiply it by 1.0.  Another way would be to add 0.0 to the value. Still another way would be to **cast** the value as a double.
   
   The more general answer to the original question is: "``avg`` contains the average of the values in the array ``alpha`` or 0 if ``alpha`` is empty."
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we6-p1.rst