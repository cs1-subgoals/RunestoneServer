Loops-WE3-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 10

    
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

.. topic:: Loops-WE3-P1

   .. parsonsprob:: parsons-Loops-WE3-P1-10

      Put the code in the right order to create a program that will continue to generate integers between 1 and 100 (inclusive) until the value generated is less than 6 or greater than 95. Print the numbers generated.
      -----
      import java.util.*;
      public class main{
         public static void main(String[] args){
      =====
            Random r = new Random();
            int x;
      =====
            do {
      =====
               x = r.nextInt(100) + 1;
      =====
               System.out.println("value is " + x);
      =====
            } while (x >= 6 && x <= 95);
      =====
         }
      }


.. activecode:: ac-loops-we3-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }