Loops-WE4-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 11

    
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

.. topic:: Loops-WE4-P1

   .. mchoice:: m-Loops-WE4-P1-11
      :answer_a: 27.0
      :answer_b: 27
      :answer_c: 22.5
      :answer_d: 22
      :answer_e: Compilation error
      :correct: a

      What is the output of the following loop if the user input is: 10, 20, 30, 35, 40, -1
      
      .. code-block:: java
      
         System.out.println("Enter a negative scroe to signal the end of the input.");
         int total = 0, count = 0;
         int score;
         System.out.println("Score: ");
         Scanner get = new Scanner(System.in);
         score= get.nextInt();
         while (score >= 0) {
            count++;
            total += score;
            System.out.print("Score: ");
            score = get.nextInt();
         }
         System.out.println( (total * 1.0) / count);
   
   
   .. mchoice:: m-Loops-WE4-P1-12
      :answer_a: 27.0
      :answer_b: 22.5
      :answer_c: 24.8
      :answer_d: 20.666667
      :answer_e: Compilation error
      :correct: c

      What is the output of the following loop if the user input is: 10, 20, 30, 35, 40, -1
      
      .. code-block:: java
      
         System.out.println("Enter a negative scroe to signal the end of the input.");
         int total = 0, count = 0;
         int score;
         System.out.println("Score: ");
         Scanner get = new Scanner(System.in);
         score= get.nextInt();
         while (score >= 0) {
            System.out.print("Score: ");
            score = get.nextInt();
            count++;
            total += score;
         }
         System.out.println( (total * 1.0) / count);
         
   .. mchoice:: m-Loops-WE4-P1-13
      :answer_a: 27.0
      :answer_b: 27
      :answer_c: 22.5
      :answer_d: 22
      :answer_e: Compilation error
      :correct: a

      What is the output of the following loop if the user input is: 10, 20, 30, 35, 40, -1
      
      .. code-block:: java
      
         System.out.println("Enter a negative scroe to signal the end of the input.");
         int total = 0, count = 0;
         int score;
         System.out.println("Score: ");
         Scanner get = new Scanner(System.in);
         score= get.nextInt();
         while (score >= 0) {
            total += score;
            System.out.print("Score: ");
            score = get.nextInt();
            count++;
         }
         System.out.println( (total * 1.0) / count);
      

.. activecode:: ac-loops-we4-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }