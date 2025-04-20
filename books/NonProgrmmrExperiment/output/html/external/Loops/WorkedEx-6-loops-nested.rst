Worked Example: Nested Loops
==================================================

.. topic:: Subgoals for Evaluating a Loop

   1. Diagram which statements go together.

   2. Define and initialize variables
      
      a. Determine the start condition.
      b. Determine the update condition.
      c. Determine the termination condition.
      d. Determine body that is repeated.
      
   3. Trace the loop.

      a. For every iteration of the loop, write down the values.
      

You can watch this video or read through the content below it.

.. youtube:: gXQnUAwJmfI
   :divid: video-loops-we6
   :align: center

---------------------------------------------------------------------------------------------------------

Problem: Given the following code, what is the output?

.. code-block:: java

   int i = 0, j = 0, m = 8, n = 5;
   while (i < n)
   {
     j = 0;
     while (j < m)
     {
	   System.out.print("*");
	   j++;
     }
     System.out.println();
     i++;
   }

---------------------------------------------------------------------------------------------------------


.. topic:: SG1:  Diagram which statements go together.
    
   .. figure:: Figures/we6-code-diagram.png
      :alt: nested loops code diagram
      :scale: 50%

   
.. topic:: SG2: Define and initialize variables

   For now, we begin with the variables that control the outer loop.

   **Start:** 

   .. code-block:: java
     
      i = 0, n = 5

   
   **End:** 

   .. code-block:: java
  
      i >= 5


.. topic:: SG3: Trace the loop

   Think of an analog clock:

   Second hand goes completely around before minute hand moves

   Just like inner loop:

   Inner loop must finish before outer loop increments once

   .. figure:: Figures/AnalogClock.png
      :alt: Clock
      :scale: 50%


   Looking at ONLY the outer loop: <NL> is a new line
 
   .. figure:: Figures/WL3Slide7.png
      :alt: Counter
      :scale: 50%


``Now Repeat for inner loop``


.. topic:: SG1:  Diagram which statements go together.

   .. figure:: Figures/we6-code-diagram.png
      :alt: Counter
      :scale: 50%
      
      
.. topic:: SG2: Define and initialize variables

   **Start:** 

   .. code-block:: java
     
      j = 0, m = 8

   
   **End:** 

   .. code-block:: java
  
      j >= 8
      
.. topic:: SG3: Trace the loop

   Looking at Only the inner loop: 

   .. figure:: Figures/WL3Slide11.png
      :alt: Counter
      :scale: 50%   
      
   Remember, this was just for the first iteration of the outer loop, while i is still value 0.

   .. figure:: Figures/WL3Slide12.png
      :alt: Counter
      :scale: 50%   

   Continuing to the next iteration of the outer loop, i is 1 and j is re-started at value 0:

   .. figure:: Figures/WL3Slide13.png
      :alt: Counter
      :scale: 50%   

   Again, increment i to 2, and j is re-started at 0:

   .. figure:: Figures/WL3Slide14.png
      :alt: Counter
      :scale: 50% 

   Note that outer loop goes 5 times,

   Inner loop goes 8 times (for each outer loop)

   .. figure:: Figures/WL3Slide15.png
      :alt: Counter
      :scale: 50% 

The final output will be 5 lines of 8 asterisks (*).
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      loops-we6-p1.rst