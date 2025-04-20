Worked Example: Arrays - Initializer List and Reverse Traverse
=================================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: 4ZCUguwJ_qw
   :divid: video-arrays-we3
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: Evaluate these statements and determine their output

.. code-block:: java
   
   int [] alpha = {15, 24, 7, 6, -4, 0, 13};
   System.out.println(alpha.length);
   for (int i = alpha.length-1; i >= 0; i--)
       alpha[i] = alpha[i] + 1;
   for (int i = alpha.length-1; i >= 0; i--)
       System.out.print(alpha[i]+ " ");
   
   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Set up array from 0 to size-1


   .. code-block:: java

      int [] alpha = {15, 24, 7, 6, -4, 0, 13};

   .. figure:: Figures/we3-init.png
      :alt: Instantiated Array
      :scale: 50%   
   
   - alpha is declared as an array of ints
   - This statement allocates 7 slots for integers because there are 7 literal values given in the initialization list.

   
.. topic:: SG2: Evaluate data type of statements against array

   The statement ``System.out.println(alpha.length);`` will print an output String. Then, 

   .. code-block:: java
 
      for (int i = alpha.length-1; i >= 0; i--)
           alpha[i] = alpha[i] + 1;

   - This loop has index i go from 6 to 0 by decrements of 1. 
   - All of the array indexes are within the bounds of the array (6 – 0) and the value of 1 is added to the current value at position i in the array.
   - All values being assigned are valid integers and can be stored in an integer array.
   
   The final for-loop will also print output strings.

.. topic:: SG3: Trace statements, updating slots as you go

   The statement ``System.out.println(alpha.length);`` will print the value 7 and then a newline return, so that the next output will begin on a new line. Then, the first for-loop will update the array values (without printing them quite yet!) 

   .. code-block:: java
 
      for (int i = alpha.length-1; i >= 0; i--)
           alpha[i] = alpha[i] + 1;
           
   The resulting array is: 
   
   .. figure:: Figures/we3-result.png
      :alt: Resulting Array
      :scale: 50%  
      
   The final for-loop will print: 14    1    -3    7    8    25    16
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we3-p1.rst