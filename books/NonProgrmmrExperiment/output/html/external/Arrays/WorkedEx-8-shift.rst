Worked Example: Arrays - Shift
=================================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: QtXbGVlU_ms
   :divid: video-arrays-we8
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: Assume that the integer array ``alpha`` has been properly declared, has a length greater than or equal to 1, and is full of data values. Evaluate these statements and determine the values in ``alpha``. If any error occurs, give the reason.

.. code-block:: java
   
   int start = alpha[0];
   for (int i = 0; i < alpha.length - 1; i++) {
      alpha[i] = alpha[i+1])
   }
   alpha[length - 1] = start;
   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Set up array from 0 to size-1

   .. figure:: Figures/we4-init.png
      :alt: Instantiated Array
      :scale: 50%  
   
.. topic:: SG2: Evaluate data type of statements against array

   All indexes into the array are valid, and all assignments are valid.

.. topic:: SG3: Trace statements, updating slots as you go

   Let us trace with a sample array.
   
   .. figure:: Figures/we4-sample.png
      :alt: Sample Array
      :scale: 50%  

   For this example, the first statement, ``int start = alpha[0];`` gives ``start`` a value of 12. We need to save this value to use at the end, so we do not lose it during the shift.
   
   Then a for-loop is used to traverse the array and copy the value at index i+1 into position at index i. The chart below shows the assignment for every iteration of the loop, as well as the state of the array after the loop is complete.
   
   .. figure:: Figures/we8-trace.png
      :alt: Trace loop as it shifts values
      
   The final statement, ``alpha[length - 1] = start;``, places the saved start value into position at the end of the array. The final array is shown below:
   
   .. figure:: Figures/we8-result.png
      :alt: Resulting Array
      :scale: 50%  
   
   The more general answer to the original question is: "``alpha`` contains the same values, but their positions have shifted down/left by 1 index each, with the value at index ``0`` now at index ``array.length - 1``."
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we8-p1.rst