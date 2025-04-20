Loops-WE6-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 15

    
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

.. topic:: Loops-WE6-P1

   .. mchoice:: m-Loops-WE6-P1-15
      :answer_a: 5 lines of ###
      :answer_b: 3 lines of #####
      :answer_c: 4 lines of ######
      :answer_d: 5 lines of ####
      :answer_e: Compilation error
      :correct: c

      What is the output of the following loop?
      
      .. code-block:: java
      
         for (int m = 0; m < 4; m++)
         {
            for (int n = 5; n >= 0; n--)
            {
               System.out.print("#");
            }
            System.out.println();
         }
   
   .. mchoice:: m-Loops-WE6-P1-16
      :answer_a: See diagram for answer A
      :answer_b: See diagram for answer B
      :answer_c: See diagram for answer C
      :answer_d: See diagram for answer D
      :answer_e: See diagram for answer E
      :correct: a

      What is the output of the following loop?
      
      .. code-block:: java
      
         for (int m = 0; m < 4; m++)
         {
            for (int n = 0; n <= m; n++)
            {
               System.out.print("$");
            }
            System.out.println();
         }
   
      .. figure:: Figures/LoopsQ16.png
         :alt: answer choices A through E 
   
   
   .. mchoice:: m-Loops-WE6-P1-17
      :answer_a: See diagram for answer A
      :answer_b: See diagram for answer B
      :answer_c: See diagram for answer C
      :answer_d: See diagram for answer D
      :answer_e: See diagram for answer E
      :correct: a

      What is the output of the following loop?
      
      .. code-block:: java
      
         for (int m = 1; m < 5; m++)
         {
            for (int n = 1; n <= m; n++)
            {
               System.out.print(" ");
            }
            System.out.println("$");
         }
   
      .. figure:: Figures/LoopsQ17.png
         :alt: answer choices A through E 
   

.. activecode:: ac-loops-we6-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }