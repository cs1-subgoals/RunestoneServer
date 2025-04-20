Worked Example: Complex Conditional
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

.. youtube:: 3rl4cisN3vw
   :divid: video-loops-we3
   :align: center

---------------------------------------------------------------------------------------------------------

Problem: Given the following code, what is the output if the user enters 50, 70, 80, 65, 90, 100, 0, 5, 102?

.. code-block:: java

   System.out.println("Enter a value. An invalid value will end input. ");
   int pass = 0, fail = 0;
   int value;
   System.out.print ("Score: ");
   Scanner get = new Scanner(System.in);
   value = get.nextInt();
   while (value >= 0 && value <= 100) 
   {
      if (value >= 70)
         pass++;
      else
         fail++;
      System.out.print("Score: ");
      value = get.nextInt();
   }
   System.out.println("Total number of scores: " + (pass + fail));
   System.out.println("Pass: " + pass + "    Fail: " + fail);

---------------------------------------------------------------------------------------------------------


.. topic:: SG1:  Diagram which statements go together.
    
   .. figure:: Figures/ComplexConditional.png
      :alt: Counter
      :scale: 50%

   
.. topic:: SG2: Define and initialize variables

   **Start:** 

   .. code-block:: java
     
      value = 50

   
   **End:** 

   .. code-block:: java
  
      value < 0 OR
      value > 100

   .. figure:: Figures/ComplexConditional.png
      :alt: Counter
      :scale: 50%

 


.. topic:: SG3: Trace the loop

   .. figure:: Figures/WL1CSlide6.png
      :alt: Counter
      :scale: 50%

 
Total number of scores: 8 
Pass: 4    Fail: 4

      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      loops-we3-p1.rst
