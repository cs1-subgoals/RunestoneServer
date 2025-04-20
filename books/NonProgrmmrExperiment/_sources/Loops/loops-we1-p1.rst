Loops-WE1-P1
----------------------

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

.. topic:: Loops-WE1-P1

   .. mchoice:: m-Loops-WE1-P1-1
      :answer_a: See diagram for answer A
      :answer_b: See diagram for answer B
      :answer_c: See diagram for answer C
      :answer_d: See diagram for answer D
      :answer_e: See diagram for answer E
      :correct: c

      What is the output of the following loop?
      
      .. code-block:: java
      
         int i = 0;
         while (i < 3) {
            System.out.println("hi");
            i++;
         }
         
      .. figure:: Figures/LoopsQ1.png
         :alt: A is hi; B is hi0 h1 h2 (multiline); C is hi hi hi (multiline); D is hi hi hi single line); E is hi hi hi hi (multiline)
      

   .. mchoice:: m-Loops-WE1-P1-2
      :answer_a: 10 9 8 7 6 5 4 3 2 1
      :answer_b: 9 8 7 6 5 4 3 2 1
      :answer_c: 9 8 7 6 5 4 3 2
      :answer_d: 10 9 8 7 6 5 4 3 2
      :answer_e: compiler error
      :correct: d

      What is the output of the following loop?
      
      .. code-block:: java
      
         int i = 10;
         while (i > 1) {
            System.out.println(i + " ");
            i--;
         }
   
   
   .. mchoice:: m-Loops-WE1-P1-3
      :answer_a: 10 11 12 13 14 15 16
      :answer_b: 10 9 8 7 6 5 4 3 2
      :answer_c: 10 9 8 7 6 5 4 3 2 1
      :answer_d: 1 2 3 4 5 6 7 8 9 10
      :answer_e: infinite loop
      :correct: e

      What is the output of the following loop?
      
      .. code-block:: java
      
         int i = 10;
         while (i > 1) {
            System.out.println(i + " ");
            i++;
         }
   
   
   .. mchoice:: m-Loops-WE1-P1-4
      :answer_a: 0 5 10 15 20 25 30 35 40 45 50
      :answer_b: 0 5 10 15 20 25 30 35 40 45
      :answer_c: 5 10 15 20 25 30 35 40 45 50
      :answer_d: 5 10 15 20 25 30 35 40 45
      :answer_e: 55
      :correct: e

      What is the output of the following loop?
      
      .. code-block:: java
      
         int i = 0;
         int total = 0;
         while (i <= 50) {
            total += i;
            i += 5;
         }
         System.out.println(i);
   
   
   .. mchoice:: m-Loops-WE1-P1-5
      :answer_a: 0
      :answer_b: 1
      :answer_c: 99
      :answer_d: 100
      :answer_e: 101
      :correct: b

      What is the value of ``counter`` after the execution of the folowing code?
      
      .. code-block:: java
      
         int counter = 0;
         while (counter > 100) {
            if (counter % 2 == 1)
               System.out.println(counter + " is odd.");
            else
               System.out.println(counter + " is even.");
         }
         counter++;
         System.out.println(counter);


.. activecode:: ac-loops-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }