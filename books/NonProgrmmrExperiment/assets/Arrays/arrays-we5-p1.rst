Arrays-WE5-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 39

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE5-P1

   .. parsonsprob:: parsons-Arrays-WE5-P1-39

      Put the following code in order to create a program that will declare and instantiate an array of 10 random values between 1 and 100 and then find the maximum value in the array.
      -----
      import java.util.*;
      public class main{
         public static void main (String[] args) {
      =====
            Random r = new Random();
            int [] arr = new int[10];
      =====
            for (int i = 0; i < 10; i++) {
               arr[i] = r.nextInt(100) + 1;
               System.out.println("arr["+i+"] is " + arr[i]);
            }
      =====
            int max = arr[0];
      =====
            for (int i = 1; i < 10; i++) {
      =====
               if (arr[i] > max)
      =====
                  max = arr[i];
      =====
            }
      =====
            System.out.println("Maximum value is " + max);
      =====
         }
      }

.. activecode:: ac-Arrays-WE5-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }