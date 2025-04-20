Loops-WE2-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 6

    
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

.. topic:: Loops-WE2-P1

   .. mchoice:: m-Loops-WE2-P1-6
      :answer_a: 50
      :answer_b: 0
      :answer_c: 5
      :answer_d: 270
      :answer_e: 275
      :correct: e

      What is the value of ``total`` after the execution of the folowing code?
      
      .. code-block:: java
      
         int total = 0;
         for (int x = 50; x >= 0; x -= 5) {
            total += x;
         }


   .. mchoice:: m-Loops-WE2-P1-7
      :answer_a: 0 1 4 9 16 25 36 49 64 81
      :answer_b: 1 4 9 16 25 36 49 64 81
      :answer_c: 1 4 9 16 25 36 49 64
      :answer_d: 0 1 2 3 4 5 6 7 8 9 10
      :answer_e: 1 2 3 4 5 6 7 8 9 10
      :correct: a

      What is the output of the following loop?
      
      .. code-block:: java
      
         for (int y = 0; y < 10; y++) {
            System.out.print(y * y + " ");
         }
   
   
   .. mchoice:: m-Loops-WE2-P1-8
      :answer_a: 100
      :answer_b: 10
      :answer_c: 100 90 80 70 60 50 40 30 20
      :answer_d: 100 90 80 70 60 50 40 30 20 10
      :answer_e: no output produced
      :correct: e

      What is the output of the following loop?
      
      .. code-block:: java
      
         for (int y = 100; y < 10; y--) {
            System.out.println(y);
         }
   
   
   .. fillintheblank:: fill-Loops-WE2-P1-9

      What are the values of ``a`` and ``b`` after the folowing code executes?
      
      .. code-block:: java
      
         int a = 0, b = 0;
         for (int x = 1; x <= 15; x++) {
            if (x % 2 == 0) 
               a += x;
            else
               b += x;
         }
         System.out.println("a is " + a);
         System.out.println("b is " + b);
         
      The value of ``a`` is |blank| and the value of ``b`` is |blank|.
      
      - :56: Correct
        :x: Incorrect. 
      - :64: Correct
        :x: Incorrect.


.. activecode:: ac-loops-we2-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }