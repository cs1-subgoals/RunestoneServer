Worked Example: While Loops - Counter
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

.. youtube:: eGSfkfodY8g
   :divid: video-loops-we1
   :align: center

---------------------------------------------------------------------------------------------------------

Problem: Given the following code, what is the output?

.. code-block:: java

    int counter = 0;
    int total = 0;

    while (counter < 50)
    {
	if (counter % 5 == 0)
		total += counter;
	counter++;
     }

     System.out.println(total);

---------------------------------------------------------------------------------------------------------


.. topic:: SG1:  Diagram which statements go together.
    
   .. figure:: Figures/WL1Counter.png
      :alt: Counter
      :scale: 50%

   
.. topic:: SG2: Define and initialize variables

   **Start:** 

   .. code-block:: java
     
      counter = 0;
      total = 0;

   
   **End:** 

   .. code-block:: java
  
      counter >= 50

   .. figure:: Figures/WL1Counter.png
      :alt: Counter
      :scale: 50%

 


.. topic:: SG3: Trace the loop

   .. figure:: Figures/WL1Counter.png
      :alt: Counter
      :scale: 50%


   System.out.println(total);

   .. figure:: Figures/Slide6.png
      :alt: Counter
      :scale: 50%
   

   A. For every iteration of loop, write down values

   Counter increments by 1
   But only when it is evenly divisible by 5 is the value added to total

   .. figure:: Figures/WL1Whlie-Slide7.png
      :alt: Counter
      :scale: 50%


   .. figure:: Figures/WL1While-Slide8.png
      :alt: Counter
      :scale: 50%

 
   Output is 225 
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      loops-we1-p1.rst

