Assessment: Writing Loops
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Writing a Loop

   1. Determine purpose of loop

      a. Pick a loop structure (while, for, do_while)

   2. Define and initialize variables

   3. Determine termination condition
      
      a. Invert termination condition to continuation condition

   4. Write the loop body

      a. Update Loop Control Variable to reach termination

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-wrloops-1
   :nofeedback:

   .. mchoice:: assess-wrloops-1-1
      :answer_a: I only
      :answer_b: II only
      :answer_c: I and II only
      :answer_d: I and III only
      :answer_e: I, II and III
      :correct: e

      Given the following code segment:
      
      .. code-block:: java

         int x = 1;
         while ( /* condition */ ) {
            if (x % 2 == 0) {
               System.out.print(x + "  ");
            }
            x = x + 2;
         }
   
      Consider the following conditions to replace ``/* condition */``  in the code segment:
      
      I. x < 0
      II. x <= 1
      III. x < 10

      For which of the conditions will nothing be printed?


   .. mchoice:: assess-wrloops-1-2
      :answer_a: inputVal % k == 0
      :answer_b: k % inputVal == 0
      :answer_c: inputVal % k != 0
      :answer_d: inputVal / k == 0
      :answer_e: k / inputVal > 0
      :correct: a

      Given the following code segment which is intended to print the number of integers that evenly divide the integer inputVal. (You may assume that inputVal > 0.)
      
      .. code-block:: java
       
         int count = 0;
         int inputVal = /* user entered value */
         for (int k = 1; k <= inputVal; k++) {
            if ( /* condition */ ) {
               count++;
            }
         } // end for
         System.out.println(count);
   
         Which of the following can be used to replace /* condition */ so that numDivisors will work as intended? 


   .. mchoice:: assess-wrloops-1-3
      :answer_a: I only
      :answer_b: II only
      :answer_c: I and II only
      :answer_d: I and III only
      :answer_e: I, II and III
      :correct: e

      Which of the following code segments will produce the output:
      
      1   4   7   10   13   16   19
      
      I.
      
      .. code-block:: java
      
         int k = 1;
         while (k < 20) {
            if (k % 3 == 1)
               System.out.print(k + "  ");
            k = k + 3;
         }
      
      II.
      
      .. code-block:: java
      
         for (int k = 1; k < 20; k++) {
            if (k % 3 == 1)
               System.out.print(k + "  ");
         }
      
      III.
      
      .. code-block:: java

         for (int k = 1; k < 20; k = k + 3) {
            System.out.print(k + "  ");
         }


   .. mchoice:: assess-wrloops-1-4
      :answer_a: 2
      :answer_b: n - 1
      :answer_c: n - 2
      :answer_d: (n - 1) * (n - 1)
      :answer_e: n * n
      :correct: d

      What is the maximum number of times "Hello" can be printed?
      
      .. code-block:: java
    
         int k = // a random number such that 1 <= k <= n ;
         for (int p = 2; p <= k; p++) {
            for (int r = 1; r < k; r++)
               System.out.println("Hello");
         }