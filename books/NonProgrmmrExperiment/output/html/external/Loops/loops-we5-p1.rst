Loops-WE5-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 14

    
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

.. topic:: Loops-WE5-P1

   .. parsonsprob:: parsons-Loops-WE5-P1-14

      Put the code in the right order to create a program that will prompt a user to enter an integer which is NOT a negative mulitple of 5. If the user enters a negative multiple of 5, the program should ask for another value.
      -----
      import java.util.*;
      public class main{
         public static void main(String[] args){
      =====
            //declare variables
            int value;
            Scanner get = new Scanner(System.in);
      =====
            //prompt for and read input
            System.out.print("Enter a value. ");
            value = get.nextInt();
      =====
            //loop until valid value is entered
            for (int j = 0; value < 0 && value % 5 == 0; j++) {
      =====
               System.out.print("Invalid. Enter another value. ");
               value = get.nextInt(); 
      =====
            }
            System.out.println("Valid value entered " + value);
      =====
         }
      }


.. activecode:: ac-loops-we5-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }