Arrays-WE2-P3
----------------------

.. qnum::
   :prefix: Q
   :start: 20

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE2-P3

   Assume the following given declarations:

   .. code-block:: java

      int [] gamma;
      
   Give the contents of alpha after the execution of these statements.

   .. code-block:: java
   
      gamma = new int[6];
      gamma[0] = 50;
      for (int i = 1; i < 6; i++)
          gamma[i] = gamma[i-1] - 5;


   .. fillintheblank:: fill-Arrays-WE2-P3-20
      
      The value of gamma[0] is ``|blank|``.

      -   :50: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE2-P3-21
     
      The value of gamma[1] is ``|blank|``.

      -   :45: Correct.
          :x: Incorrect. Try again



   .. fillintheblank:: fill-Arrays-WE2-P3-22
     
      The value of gamma[2] is ``|blank|``.

      -   :40: Correct.
          :x: Incorrect. Try again



   .. fillintheblank:: fill-Arrays-WE2-P3-23
     
      The value of gamma[3] is ``|blank|``.

      -   :35: Correct.
          :x: Incorrect. Try again



   .. fillintheblank:: fill-Arrays-WE2-P3-24
     
      The value of gamma[4] is ``|blank|``.

      -   :30: Correct.
          :x: Incorrect. Try again


   .. fillintheblank:: fill-Arrays-WE2-P3-25
     
      The value of gamma[5] is ``|blank|``.

      -   :25: Correct.
          :x: Incorrect. Try again


.. activecode:: ac-Arrays-WE2-P3
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }