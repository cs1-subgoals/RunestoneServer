Arrays-WE4-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 37

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE4-P1

   .. fillintheblank:: fill-Arrays-WE4-P1-37
      
      Given the following code, what is the value in sum after execution?
      
      .. code-block:: java
      
         int [] alpha = {2, 4, 6, 8, 10, 12, 14};
         int sum = 0;
         for (int k = 0; k < alpha.length; k+=2)
            sum = sum + alpha[k];

      -   :32: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE4-P1-38
      
      Given the following code, what is the value in sum after execution?
      
      .. code-block:: java
     
         int [] beta = new int [5];
         int sum = 0;
         for (int k = 0; k < beta.length; k++)
             beta[k] = 2 * k + 1;
         int x = 3;
         for (int k = 1; k < beta.length; k++) {
            sum += beta[k];

      -   :24: Correct.
          :x: Incorrect. Try again


.. activecode:: ac-Arrays-WE4-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }