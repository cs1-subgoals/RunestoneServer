Assessment: Nested Loops
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

.. timed:: assess-loops-2
   :nofeedback:

   .. mchoice:: assess-loops-2-1
      :answer_a: 4
      :answer_b: 8
      :answer_c: 10
      :answer_d: 16
      :answer_e: 20
      :correct: c

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
      
         int count = 0;
         for (int x = 0; x < 4; x++) {
            for (int y = x; y < 4; y++)
               count++;
         }
         System.out.println(count);


   .. mchoice:: assess-loops-2-2
      :answer_a: 0
      :answer_b: 1
      :answer_c: 2
      :answer_d: n - 1
      :answer_e: n - 2
      :correct: a

      What is the minimum number of times “Hello” can be printed?
      
      .. code-block:: java
     
         int k = // a random number such that 1 <= k <= n ;
         for (int p = 2; p <= k; p++) {
            for (int r = 1; r < k; r++)
               System.out.println("Hello");
         }


   .. mchoice:: assess-loops-2-3
      :answer_a: See diagram for answer A
      :answer_b: See diagram for answer B
      :answer_c: See diagram for answer C
      :answer_d: See diagram for answer D
      :answer_e: See diagram for answer E
      :correct: a

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
     
         for (int r = 3; r > 0; r--) {
            int c;
            for (c = 1; c < r; c++)
               System.out.print("-");
            for (c = r; c <= 3; c++)
               System.out.print("*");
            System.out.println();
         }
         
      .. figure:: Figures/assess-loops-2-q3.png
         :alt: answers for Q3


   .. mchoice:: assess-loops-2-4
      :answer_a: 0  1  2  3
      :answer_b: 0  0  1  0  1  2
      :answer_c: 0  1  2  2  3  3  3
      :answer_d: 0  1  1  2  2  2  3  3  3  3
      :answer_e: 0  0  1  0  1  2  0  1  2  3
      :correct: d

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
     
         for (int outer = 0; outer < 4; outer++) {
            for (int inner = 0; inner <= outer; inner++)
               System.out.print(outer + "  ");
         }
    
    
   .. mchoice:: assess-loops-2-5
      :answer_a: 20
      :answer_b: 45
      :answer_c: 55
      :answer_d: 100
      :answer_e: 385
      :correct: c

      What is printed as a result of executing the following code segment?
      
      .. code-block:: java
     
         int s = 0;
         for (int outer = 1; outer <= 10; outer++) {
            for (int inner = outer; inner <= 10; inner++)
               s++;
         }
         System.out.println(s);
