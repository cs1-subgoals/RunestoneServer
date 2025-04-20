Worked Example: Writing Loops
==================================================

.. topic:: Subgoals for Writing a Loop

   1. Determine purpose of loop

      a. Pick a loop structure (while, for, do_while)

   2. Define and initialize variables

   3. Determine termination condition
      
      a. Invert termination condition to continuation condition

   4. Write the loop body

      a. Update Loop Control Variable to reach termination
      

You can watch this video or read through the content below it.

.. youtube:: xjomZCUPwcU
   :divid: video-writeloops-we1
   :align: center



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem 1: Write a loop that will prompt the user to continue to enter numbers until a sentinel value is entered and find the maximum value entered.

   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1:  Determine purpose of loop

   Generally, while-loops are a good choice for sentinel loops.
    

.. topic:: SG2: Define and initialize variables
   
   We will need variables to store the most recent input value, as well as the maximum value so far.
   
   We will also need a Scanner to accept user input, as well as a priming read.
   
   .. code-block:: java

      Scanner get = new Scanner(System.in);
      int value;
      int maxSoFar;
      System.out.println("Enter a value, enter -1 to end");
      value = get.nextInt();
      while (                ) 
      {
         
      }


 
.. topic:: SG3: Define termination condition invert to continuation condition

   .. code-block :: java
        
      Scanner get = new Scanner(System.in);
      int value;
      int maxSoFar;
      System.out.println("Enter a value, enter -1 to end");
      value = get.nextInt();
      while ( value != -1  ) 
      {
   
      }
      

.. topic:: SG4a: Update condition (LCV) to reach termination
   
   .. code-block:: java

      Scanner get = new Scanner(System.in);
      int value;
      int maxSoFar;
      System.out.println("Enter a value, enter -1 to end");
      value = get.nextInt();

      while ( value != -1  ) 
      {
         System.out.println("Enter a value, enter -1 to end");
         value = get.nextInt();
      }

.. topic:: SG4: Write loop body


   .. code-block:: java

      Scanner get = new Scanner(System.in);
      int value;
      int maxSoFar = -1;
      System.out.println("Enter a value, enter -1 to end");
      value = get.nextInt();

      while ( value != -1  ) 
      {
          if (value > maxSoFar)
  	      maxSoFar = value;
          System.out.println("Enter a value, enter -1 to end");
          value = get.nextInt();
      }
      if (maxSoFar > -1) 
          System.out.println("The maximum is " + maxSoFar);
      else 
          System.out.println("No values entered");


   
   
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Problem 2: Write a loop that will add up 1 + 1/2 + 1/4 + 1/8 + 1/16 + ... + 1/1024

   
---------------------------------------------------------------------------------------------------------

.. topic:: SG1:  Determine purpose of loop

   Because we know the number of iterations, we *could* choose a for-loop, but for this exercise we will go with the general purpose while-loop.



.. topic:: SG2: Define and initialize variables

   .. code-block:: java

      double sum = 0;
      double term = 1.0;
      while (        )
      {
         
      }
      System.out.println(sum);


 
.. topic:: SG3: Define termination condition invert to continuation condition

   The denominators are increasing powers of 2. The first denominator, if you think of 1 as 1/1, is 2 raised to the power of 0. The final denominator, 1024, is 2 raised to the power of 10, so we will iterate from zero to ten.

   .. code-block :: java
        
      double sum = 0;
      double term = 1.0;
      int i = 0;
      while ( i <= 10 )
      {
         
      }
      System.out.println(sum);
         
 
.. topic:: SG4: Write loop body
   
   .. code-block:: java

      double sum = 0;
      double term = 1.0;
      int i = 0;

      while ( i <= 10 )
      {
         sum = sum + term;
         term = 0.5 * term; //same as divide term in half
         i++;
      }
      System.out.println(sum);


      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      writeloops-we1-p1.rst