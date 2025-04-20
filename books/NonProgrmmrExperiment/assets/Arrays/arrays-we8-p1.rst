Arrays-WE8-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 45

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE8-P1

   .. mchoice:: m-Arrays-WE8-P1-45
      :answer_a: {20, 30, 40, 50, 60, 70, 70}
      :answer_b: {20, 30, 40, 50, 60, 70, 10}
      :answer_c: {10, 20, 30, 40, 50, 60, 70}
      :answer_d: {10, 10, 20, 30, 40, 50, 60}
      :answer_e: {70, 10, 10, 10, 10, 10, 10}
      :correct: e

      What are the contents of array alpha after this code has been executed?
    
      .. code-block:: java
      
         int [] alpha = {10, 20, 30, 40, 50, 60, 70};
         int start = alpha[alpha.length-1];
         for (int i = 1; i < alpha.length; i++)  {
            alpha[i] = alpha[i-1];
         }
         alpha[0] = start;

      
   .. mchoice:: m-Arrays-WE8-P1-46
      :answer_a: {20, 30, 40, 50, 60, 70, 70}
      :answer_b: {20, 30, 40, 50, 60, 70, 10}
      :answer_c: {10, 20, 30, 40, 50, 60, 70}
      :answer_d: {10, 10, 20, 30, 40, 50, 60}
      :answer_e: {70, 10, 20, 30, 40, 50, 60}
      :correct: d

      What are the contents of array beta after this code has been executed?
    
      .. code-block:: java
      
         int [] beta = {10, 20, 30, 40, 50, 60, 70};
         for (int i = 1; i < beta.length; i++)  {
            beta[i] = beta[i-1])
         }


   .. mchoice:: m-Arrays-WE8-P1-47
      :answer_a: {20, 30, 40, 50, 60, 70, 70}
      :answer_b: {20, 30, 40, 50, 60, 70, 10}
      :answer_c: {10, 20, 30, 40, 50, 60, 70}
      :answer_d: {10, 10, 20, 30, 40, 50, 60}
      :answer_e: IndexOutOfBounds Exception
      :correct: e

      What are the contents of array gamma after this code has been executed?
    
      .. code-block:: java
      
         int [] gamma = {10, 20, 30, 40, 50, 60, 70};
         for (int i = 0; i < gamma.length; i++)  {
            gamma[i] = gamma[i+1])
         }


.. activecode:: ac-Arrays-WE8-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }