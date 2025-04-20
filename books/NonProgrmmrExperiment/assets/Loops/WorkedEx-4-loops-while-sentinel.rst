Worked Example: While Loops - Sentinel
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

.. youtube:: BoCo03mSEO8
   :divid: video-loops-we4
   :align: center

---------------------------------------------------------------------------------------------------------

Problem: Given the following code, what is the output if the user enters the values:  10, 15, 20, 25, 30, 35, -1?

.. code-block:: java

   System.out.println("Enter a negative score to signal the end of input.");
   int gdScores = 0;
   int score;
   System.out.print("Score: ");
   Scanner get = new Scanner(System.in);
   score = get.nextInt();
   while (score >= 0) 
   {
	if (score >= 20)
	    gdScores++;
	System.out.print("Score: ");
	score = get.nextInt();
    }
   System.out.println("Number of good scores: " + gdScores);

---------------------------------------------------------------------------------------------------------


.. topic:: SG1:  Diagram which statements go together.
    
   .. figure:: Figures/WhileSentinel.png
      :alt: Counter
      :scale: 50%

   
.. topic:: SG2: Define and initialize variables

   **Start:** 

   .. code-block:: java
     
      score = 10;

   
   **End:** 

   .. code-block:: java
  
      score < 0

   .. figure:: Figures/WhileSentinel.png
      :alt: Counter
      :scale: 50%

 


.. topic:: SG3: Trace the loop

   .. figure:: Figures/WL2Slide6.png
      :alt: Counter
      :scale: 50%

 
Number of good scores: 4

      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      loops-we4-p1.rst