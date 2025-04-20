Arrays-WE3-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 31

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE3-P1

   .. fillintheblank:: fill-Arrays-WE3-P1-31
      
      Assume the following given declarations:
      
      .. code-block:: java
      
         int [] beta = {12, 24, 36, 48, 60};

      Evaluate these statements:

      .. code-block:: java
      
         beta[1] = beta[3] - beta[1] + 6;
         beta[3] = beta[beta[4] % beta[0]];
         beta[2] = beta[beta[4]/beta[0]-1];
         
      Give the contents of array ``beta`` after the execution of the above statements:
      
      beta[0] = |BLANK|
      
      beta[1] = |BLANK|
      
      beta[2] = |BLANK|
      
      beta[3] = |BLANK|
      
      beta[4] = |BLANK|

      -   :12: Correct.
          :x: Incorrect. Try again
      -   :30: Correct.
          :x: Incorrect. Try again
      -   :60: Correct.
          :x: Incorrect. Try again
      -   :12: Correct.
          :x: Incorrect. Try again
      -   :60: Correct.
          :x: Incorrect. Try again
      
   For questions 32-36, give the contents of alpha after the execution of these statements.

   .. code-block:: java

      int alpha = {2, 4, 6, 8, 10};
      for (int i = 8; i >= 0; i-=2)
         alpha[i/2] = i/2 + 1;


   .. fillintheblank:: fill-Arrays-WE3-P1-32
      
      Enter the values of alpha in the blanks.
     
      The value of alpha[0] is ``|blank|``.

      -   :1: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE3-P1-33
      
      Enter the values of alpha in the blanks.
     
      The value of alpha[1] is ``|blank|``.

      -   :2: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE3-P1-34
      
      Enter the values of alpha in the blanks.
     
      The value of alpha[2] is ``|blank|``.

      -   :3: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE3-P1-35
      
      Enter the values of alpha in the blanks.
     
      The value of alpha[3] is ``|blank|``.

      -   :4: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE3-P1-36
      
      Enter the values of alpha in the blanks.
     
      The value of alpha[4] is ``|blank|``.

      -   :5: Correct.
          :x: Incorrect. Try again


.. activecode:: ac-Arrays-WE3-P1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }