Arrays-WE6-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 40

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE6-P1

   .. parsonsprob:: parsons-Arrays-WE6-P1-40

      Put the following code in order to create a program that will declare and instantiate an array of 20 random values between 1 and 100 and then calculate and print the average of the first 10 numbers.
      -----
      import java.util.*;
      public class main{
         public static void main (String[] args) {
      =====
            Random r = new Random();
            int [] arr = new int[20];
      =====
            for (int i = 0; i < 20; i++) {
               arr[i] = r.nextInt(100) + 1;
               System.out.println("arr["+i+"] is " + arr[i]);
            }
      =====
            int sum = 0;
      =====
            for (int i = 0; i < 10; i++) {
      =====
               sum += arr[i];
      =====
            }
      =====
            System.out.println("Avg of first 10 is " + sum/10.0);
      =====
         }
      }
      
      
   .. parsonsprob:: parsons-Arrays-WE6-P1-41

      Put the following code in order to create a program that will declare and instantiate an array of 20 random values between 1 and 100 and then calculate and print the average of the last n numbers.
      -----
      import java.util.*;
      public class main{
         public static void main (String[] args) {
      =====
            Random r = new Random();
            int [] arr = new int[20];
      =====
            for (int i = 0; i < 20; i++) {
               arr[i] = r.nextInt(100) + 1;
               System.out.println("arr["+i+"] is " + arr[i]);
            }
      =====
            int sum = 0;
      =====
            for (int i = 20-n; i < 20; i++) {
      =====
               sum += arr[i];
      =====
            }
      =====
            if (n > 0)
      =====
               System.out.println("Avg of last n is " + (sum * 1.0)/n);
      =====
            else
      =====
               System.out.println("No numbers to average.")
      =====
         }
      }

.. activecode:: ac-Arrays-WE6-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }