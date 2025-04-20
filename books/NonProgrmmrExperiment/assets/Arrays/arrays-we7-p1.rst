Arrays-WE7-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 42

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE7-P1

   .. parsonsprob:: parsons-Arrays-WE7-P1-42

      Put the following code in order to create a method that will find the last occurrence of a target value and return the index of where that value is located.
      -----
      public static int find (int [] arr, int target) {
      =====
         int loc = -1;
      =====
         for (int i = 0; i < arr.length; i++) {
      =====
            if (arr[i] == target) 
      =====
               loc = i;  
      =====          
         }
      =====
         return loc;
      }

      
      
   .. parsonsprob:: parsons-Arrays-WE7-P1-43

      Put the following code in order to create a method that will find the first occurrence of a target value and return the index of where that value is located.
      -----
      public static int find (int [] arr, int target) {
      =====
         int loc = -1;
         boolean found = false;
      =====
         for (int i = 0; i < 20 && !found; i++) {
      =====
            if (arr[i] == target) {
      =====
               loc = i;
               found = true;
      =====
            }
         }
      =====
         return loc;
      }

      
      
   .. parsonsprob:: parsons-Arrays-WE7-P1-44

      Put the following code in order to create a method that will count the number of occurrences of a target value and return the count.
      -----
      public static int count (int [] arr, int target) {
      =====
         int num = 0;
      =====
         for (int i = 0; i < arr.length; i++) {
      =====
            if (arr[i] == target) 
      =====
               num++;
      =====
         }
      =====
         return num;
      }

      

.. activecode:: ac-Arrays-WE7-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }
