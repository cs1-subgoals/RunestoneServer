Arrays-WE9-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 48

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE9-P1

   .. mchoice:: m-Arrays-WE9-P1-48
      :answer_a: Inserts a new value into the first position of the array
      :answer_b: Inserts a new value into the middle position of the array
      :answer_c: Inserts a new value into the last position of the array
      :answer_d: deletes a value from a specific position of the array
      :answer_e: finds and deletes a value from the array
      :correct: c

      What does the following code do?
         
      .. code-block:: java
      
         int [] alpha = {10, 20, 30, 40, 50};
         int [] beta = new int[alpha.length+1];
         for (int i = 0; i < alpha.length; i++)
            beta[i] = alpha[i];
         beta[beta.length-1] = 42;
         alpha = beta;
      
      
   .. mchoice:: m-Arrays-WE9-P1-49
      :answer_a: Inserts a new value into the first position of the array
      :answer_b: Inserts a new value into the middle position of the array
      :answer_c: Inserts a new value into the last position of the array
      :answer_d: deletes a value from a specific position of the array
      :answer_e: finds and deletes a value from the array
      :correct: e
      
      What does the following code do?
         
      .. code-block:: java
      
         int target = /*  some value */ ;
         int [] delta = {10, 20, 30, 40, 50, 60, 70, 80, 90};
         boolean found = false;
         int i, j;
         for (i = 0; i < delta.length && !found; i++)
            if (delta[i] == target)
               found = true;
         if (found) {
            for (j = i-1; j < delta.length-1; j++)
               delta[j] = delta[j+1];
            delta[delta.length-1] = -999;       
         }
         
   
   .. mchoice:: m-Arrays-WE9-P1-50
      :answer_a: Inserts a new value into the first position of the array
      :answer_b: Inserts a new value into the middle position of the array
      :answer_c: Inserts a new value into the last position of the array
      :answer_d: deletes a value from a specific position of the array
      :answer_e: finds and deletes a value from the array
      :correct: a
      
      What does the following code do?
      
      .. code-block:: java
      
         int [] alpha = {10, 20, 30, 40, 50};
         int [] beta = new int[alpha.length+1];
         for (int i = 0; i < alpha.length; i++)
            beta[i] = alpha[i];
         beta[0] = 99;
         alpha = beta; 
         
         
   .. mchoice:: m-Arrays-WE9-P1-51
      :answer_a: Inserts a new value into the first position of the array
      :answer_b: Inserts a new value into the middle position of the array
      :answer_c: Inserts a new value into the last position of the array
      :answer_d: deletes a value from a specific position of the array
      :answer_e: finds and deletes a value from the array
      :correct: d
      
      What does the following code do?
      
      .. code-block:: java
      
         int pos = /* some value */;
         int [] rho = {10, 20, 30, 40, 50, 60, 70, 80, 90};
         for (int m = pos; m < rho.length-1; m++)
            rho[m] = rho[m+1];
         rho[rho.length-1] = -999;
         
         
   .. mchoice:: m-Arrays-WE9-P1-52
      :answer_a: Inserts a new value into the first position of the array
      :answer_b: Inserts a new value into the middle position of the array
      :answer_c: Inserts a new value into the last position of the array
      :answer_d: deletes a value from a specific position of the array
      :answer_e: finds and deletes a value from the array
      :correct: b
      
      What does the following code do?
      
      .. code-block:: java
         
         int [] alpha = {10, 20, 30, 40, 50};
         int [] gamma = new int[alpha.length+1];
         for (int i = 0; i < alpha.length; i++)
            gamma[i] = alpha[i];
         gamma[gamma.length/2] = 11;
         alpha = gamma;

      
.. activecode:: ac-Arrays-WE9-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }