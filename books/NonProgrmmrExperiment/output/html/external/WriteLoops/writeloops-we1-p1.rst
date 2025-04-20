WriteLoops-WE5-P1
----------------------

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

.. topic:: WriteLoops-WE1-P1

   .. parsonsprob:: parsons-WrLoops-WE1-P1-1

      Put the code in the right order to create a program that will calculate and print the sum of 10 natural numbers.
      -----
      public class main{
         public static void main(String[] args){
      =====
            int sum = 0;
      =====
            for (int i = 0; i <= 10; i++) {
      =====
               sum += i; 
      =====
            }
            System.out.println(sum);
      =====
         }
      }
      
      
   .. fillintheblank:: fill-WrLoops-WE1-P1-2

      Fill in the blanks in the following code to create a program that will print the even numbers between 1 and 20.
      
      .. code-block:: java
      
         public class main{
            public static void main(String[] args){
               for (int i = ___A___; i <= ___B___; i++)
                  if (___C___ % ___D___ == ___E___)
                     System.out.println(i);
            }
         }
         
      | Blank A: |blank|
      | Blank B: |blank|
      | Blank C: |blank|
      | Blank D: |blank|
      | Blank E: |blank|
      
      - :1:  Correct
        :x:  Incorrect. 
      - :20: Correct
        :x:  Incorrect.
      - :i:  Correct
        :x:  Incorrect. 
      - :2:  Correct
        :x:  Incorrect.
      - :0:  Correct
        :x:  Incorrect.
        
        
   .. parsonsprob:: parsons-WrLoops-WE1-P1-3

      Put the code in the right order to create a program that will generate an integer between 0 and 10,000 (inclusive), print the number, calculate and print the number of digits in the number. 
      -----
      import java.util.*;
      public class main{
         public static void main(String[] args){
      =====
            Random r = new Random();
            int x = r.nextInt(10001);
      =====
            int digits = 0;
            int y = x;
      =====
            while (y > 0) {
      =====
               digits++;
               y = y/10;
      =====
            }
      =====
            System.out.println(x + " has " + digits + " digits.");

      =====
         }
      }
      
      
   .. parsonsprob:: parsons-WrLoops-WE1-P1-4

      Put the code in the right order to create a program that will print out all Armstrong numbers between 1 and 500. If the sum of the cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. For example, 153 = (1*1*1) + (5*5*5) + (3*3*3)

      -----
      import java.util.*;
      public class main{
         public static void main(String[] args){
      =====
            for (int i = 100; i <= 500; i++) {
      =====
                int dig1 = i/100;
                int dig2 = (i/10)%10;
                int dig3 = i%10;
      =====
                int total = Math.pow(dig1,3) + Math.pow(dig2,3) + Math.pow(dig3,3);
      =====
                if (total == i)
      =====
                    System.out.println(i + " Armstrong number.");
      =====
            } // end for
      =====
         }
      }


.. activecode:: ac-writeloops-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }