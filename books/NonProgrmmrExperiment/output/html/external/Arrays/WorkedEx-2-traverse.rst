Worked Example: Arrays - Traverse
==================================================

.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
      

You can watch this video or read through the content below it.

.. youtube:: LY1an0QTD-Q
   :divid: video-arrays-we2
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem: 

Given the initialized array:

.. code-block:: java

   int [] alpha;


Evaluate these statements and determine the value of all variables. If any error occurs, give the reason.

.. code-block:: java
   
   alpha = new int[10];
   for (int i = 0; i < 10; i++)
      alpha[i] = i * 1;
   
   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Set up array from 0 to size-1


   .. code-block:: java

      alpha = new int[10];

   .. figure:: Figures/we2-init.png
      :alt: Instantiated Array
      :scale: 50%   
   
   - alpha is declared as an array of int
   - This statement allocates 10 slots for integers (first line are values, second line are indexes)
   - Notice that the largest index is 9 (size of 10 minus 1).

   
.. topic:: SG2: Evaluate data type of statements against array

   .. code-block:: java
 
      for (int i = 0; i < 10; i++)
         alpha[i] = i * 1;

   - This loop has index i go from 0 to 9 (< 10) by increments of 1. 
   - Then the value i * 10 is placed into the position alpha[i].  
   - All of the array indexes are within the bounds of the array (0 – 9) and all values being assigned (10-90) are valid integers and can be stored in an integer array.
   

.. topic:: SG3: Trace statements, updating slots as you go

   We will evaluate the first two statements:

   .. code-block:: java
     
      for (int i = 0; i < 10; i++)
         alpha[i] = i * 1;
      
   The resulting array is:

   .. figure:: Figures/we2-result.png
      :alt: Filled Array
   
   
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      arrays-we2-p1.rst
      arrays-we2-p2.rst
      arrays-we2-p3.rst
      arrays-we2-p4.rst