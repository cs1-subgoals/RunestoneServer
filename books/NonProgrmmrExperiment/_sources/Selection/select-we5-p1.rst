Selection-WE5-P1
---------------------

.. qnum::
   :prefix: Q
   :start: 14

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Select-WE5-P1

   Use this given setup for each of the questions below.
   
   .. code-block:: java
      
      int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
      

   .. fillintheblank:: fill-Select-WE5-P1-14
   
      After executing the following code, the value in variable ``gamma`` is |blank|, the value in variable ``eta`` is |blank|, and the value in the variable ``beta`` is |blank|.
   
      .. code-block:: java
      
         if (alpha < delta)
         {
            gamma = alpha - 2;
            if (gamma == eta)
               eta = beta++;
            eta = beta + 2;
         }

      - :0: Correct
        :x: Incorrect. 
      - :4: Correct
        :x: Incorrect. 
      - :2: Correct
        :x: Incorrect. 


   .. fillintheblank:: fill-Select-WE5-P1-15
   
      After executing the following code, the value in variable ``gamma`` is |blank| and the value in variable ``eta`` is |blank|.
   
      .. code-block:: java
      
         if (alpha > beta)
         {
            if (delta > eta)
            {
               eta = alpha + 2;
            }
            gamma = alpha + 5;
            if (gamma == eta)
            {
               eta = beta + 2;
            }
         }

      - :7: Correct
        :x: Incorrect. 
      - :4: Correct
        :x: Incorrect.


.. activecode:: ac-select-we5-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }