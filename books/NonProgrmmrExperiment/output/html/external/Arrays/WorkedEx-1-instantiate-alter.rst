Worked Example: Arrays - Instantiate and Alter
==================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: zpL1OCRMWA0
   :divid: video-arrays-we1
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: 

Given the initialized array:

.. code-block:: java

   int [] alpha;


Evaluate these statements and determine the value of all variables. If any error occurs, give the reason.

.. code-block:: java
   
   alpha = new int[5];
   alpha[4] = 22;
   alpha[0] = 10;
   alpha[1] = alpha[4] - alpha[0];
   alpha[2] = alpha[1] - alpha[0];
   alpha[3] = alpha[alpha[2] - 1];
   alpha[4] = alpha[alpha[3]];
   
   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Set up array from 0 to size-1


   .. code-block:: java

      alpha = new int[5];

   .. figure:: Figures/we1-init.png
      :alt: Arrays
      :scale: 50%   
   
   - ``alpha`` is declared as an array of ints
   - This statement allocates 5 slots for integers (first line are indexes, second line are values/content):
   - Notice that the largest index is 4 (size of 5 minus 1).

   
.. topic:: SG2: Evaluate data type of statements against array

   .. code-block:: java
 
      alpha[4] = 22;
      alpha[0] = 10;
      alpha[1] = alpha[4] - alpha[0];
      alpha[2] = alpha[1] - alpha[0];
      alpha[3] = alpha[alpha[2] - 1];
      alpha[4] = alpha[alpha[3]];

   - Each of these statements only involve integers. 
   - Notice that for every [ ] in the statements the result will be an integer because we have an integer array.  
   - All of the array indexes on the left hand side of the assignment statements are within the bounds of the array (0 – 4). 
   - We can see that some of the index values on the right hand side of the array are within bounds, but we will need to evaluate them all to see if all are valid. 
   

.. topic:: SG3: Trace statements, updating slots as you go

   We will evaluate the first two statements:

   .. code-block:: java
     
      alpha[4] = 22;
      alpha[0] = 10;
      
   The resulting array is:

   .. figure:: Figures/we1-trace-1-2.png
      :alt: Arrays
      
   The next statement is:

   .. code-block:: java
     
      alpha[1] = alpha[4] - alpha[0];

   .. figure:: Figures/we1-trace-3.png
      :alt: Arrays

   Next: 
   
   .. code-block:: java
   
      alpha[2] = alpha[1] - alpha[0];
      
   .. figure:: Figures/we1-trace-4.png
      :alt: Arrays 

   For the next statement, ``alpha[3] = alpha[alpha[2] - 1];``, first determine the value of alpha[2] which is 2. 
   Then look at  alpha[2 - 1] which is alpha[1], or 12

   .. figure:: Figures/we1-trace-5.png
      :alt: Arrays

   Finally, there is a problem with the last statement: ``alpha[4] = alpha[alpha[3]];`` First determine the value of alpha[3] which is 12. 
   When we try to get alpha[12], it is out of bounds, and an ``IndexOutOfBounds`` exception occurs with this statement.
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we1-p1.rst
