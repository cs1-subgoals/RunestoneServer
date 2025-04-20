Assessment: While and For Loops
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Evaluating a Loop

   1. Diagram which statements go together.

   2. Define and initialize variables
      
      a. Determine the start condition.
      b. Determine the update condition.
      c. Determine the termination condition.
      d. Determine body that is repeated.
      
   3. Trace the loop.

      a. For every iteration of the loop, write down the values.

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-loops-1
   :nofeedback:

   .. mchoice:: assess-loops-1-1
      :answer_a: 0 2 1 0 2
      :answer_b: 0 2 0 2 0 2
      :answer_c: 0 2 1 0 2 1 0
      :answer_d: 0 2 0 2 0 2 0
      :answer_e: 0 1 2 1 2 1 2
      :correct: d

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
      
         int k = 0;
         while (k < 10) {
            System.out.print((k % 3) + " ");
            if ((k % 3) == 0)
               k = k + 2;
            else
               k++;
         }

   .. mchoice:: assess-loops-1-2
      :answer_a: First: 15; Last: 27
      :answer_b: First: 15; Last: 28
      :answer_c: First: 16; Last: 27
      :answer_d: First: 16; Last: 28
      :answer_e: First: 16; Last: 29
      :correct: a

      What are the first and last numbers printed by the following code segment?
      
      .. code-block:: java
     
         int number = 15;
         while (number < 28) {
            System.out.println(number);
            number++;
         }

   .. mchoice:: assess-loops-1-3
      :answer_a: 0
      :answer_b: 6
      :answer_c: 12
      :answer_d: 24
      :answer_e: 30
      :correct: b

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
     
         int alpha = 24;
         int beta = 30;
         while (beta != 0) {
            int rho = alpha % beta;
            alpha = beta;
            beta = rho;
         }
         System.out.println(alpha);


   .. mchoice:: assess-loops-1-4
      :answer_a: Prints the value in num
      :answer_b: Prints the sum of all the integers between 1 and num, inclusive
      :answer_c: Prints the sum of all even integers between 1 and num, inclusive
      :answer_d: Prints the sum of all odd integers between 1 and num, inclusive
      :answer_e: Nothing is printed, it is an infinite loop
      :correct: d

      Considering the following code, which best describes what the code does?
      
      .. code-block:: java
      
         int var = 0;
         int num = 50;
         for (int x = 1; x <= 50; x += 2) {
            var = var + x;
         }
         System.out.println(var);
    
    
   .. mchoice:: assess-loops-1-5
      :answer_a: 5 20 5
      :answer_b: 5 20 10
      :answer_c: 5 25 5
      :answer_d: 5 25 10
      :answer_e: 30 25 10
      :correct: d

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
     
         int typeA = 0;
         int typeB = 0;
         int typeC = 0;
         for (int k = 1; k <= 50; k++) {
            if (k % 2 == 0 && k % 5 == 0)
               typeA++;
            if (k % 2 == 0)
               typeB++;
            if (k % 5 == 0)
               typeC++;
         }
         System.out.printf("%d %d %d", typeA, typeB, typeC);