Arrays-WE2-P2
----------------------

.. qnum::
   :prefix: Q
   :start: 14

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE2-P2

   Assume the following given declarations:

   .. code-block:: java

      int [] beta;
      
   Give the contents of alpha after the execution of these statements.

   .. code-block:: java
   
      beta = new int[6];
      beta[0] = 50;
      for (int i = 1; i < 6; i++)
           beta[i] = beta[i-1];


   .. fillintheblank:: fill-Arrays-WE2-P2-14
     
      The value of beta[0] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE2-P2-15
     
      The value of beta[1] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE2-P2-16
     
      The value of beta[2] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE2-P2-17
     
      The value of beta[3] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE2-P2-18
     
      The value of beta[4] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again

   .. fillintheblank:: fill-Arrays-WE2-P2-19
     
      The value of beta[5] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again
   

.. activecode:: ac-Arrays-WE2-P2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }