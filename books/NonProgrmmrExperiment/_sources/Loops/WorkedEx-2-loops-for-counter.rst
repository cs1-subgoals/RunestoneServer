Worked Example: For Loops - Counter
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

.. youtube:: UqzVIuWjbXo
   :divid: video-loops-we2
   :align: center

---------------------------------------------------------------------------------------------------------

Problem: Given the following code, what is the output?

.. code-block:: java

   total = 0;
   for (int x = 5; x < 50; x++)
   {
     if (x % 5 == 0)
        total += x;
   }
   System.out.println(total);

---------------------------------------------------------------------------------------------------------


.. topic:: SG1:  Diagram which statements go together.
    
   .. figure:: Figures/WL1A-ForCounter.png
      :alt: Counter
      :scale: 50%

   
.. topic:: SG2: Define and initialize variables

   **Start:** 

   .. code-block:: java
     
      x = 0
      total = 0
   
   **End:** 

   .. code-block:: java
  
      x >= 50

   .. figure:: Figures/WL1A-ForCounter.png
      :alt: Counter
      :scale: 50%

 


.. topic:: SG3: Trace the loop

   .. figure:: Figures/WL1A-ForCounter.png
      :alt: Counter
      :scale: 50%

  

   .. figure:: Figures/WL1ASlide6.png
      :alt: Counter
      :scale: 50%


   X increments by 1 But only when it is evenly divisible by 5 is the value added to total



   .. figure:: Figures/WL1ASlide7.png
      :alt: Counter
      :scale: 50%



   .. figure:: Figures/WL1ASlide8.png
      :alt: Counter
      :scale: 50%

Output is 225
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      loops-we2-p1.rst