Selection-WE4-P1
--------------------

.. qnum::
   :prefix: Q
   :start: 11

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Select-WE4-P1

   .. clickablearea:: ca-Select-WE4-P1-11
      :question: Click on the statements belonging to the else-branch in the following code
      :iscode:
      
      :click-incorrect:if (alpha < delta):endclick:
         :click-incorrect:gamma = alpha + 5;:endclick:
      :click-incorrect:else:endclick:
         :click-correct:gamma = beta + 5;:endclick:
         :click-incorrect:eta = beta + 2;:endclick:


   Use this given setup for each of the questions below.
   
   .. code-block:: java
      
      int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
      

   .. fillintheblank:: fill-Select-WE4-P1-12
   
      After executing the following code, the value in variable ``gamma`` is |blank| and the value in variable ``eta`` is |blank|.
   
      .. code-block:: java
      
         if (alpha < delta)
            gamma = alpha + 5;
         else
            gamma = beta + 5;
            eta = beta + 2;

      - :7: Correct
        :x: Incorrect. 
      - :3: Correct
        :x: Incorrect.  Remember, if there are no {}, only the next statement is included in the branch.


   .. fillintheblank:: fill-Select-WE4-P1-13
   
      After executing the following code, the value in variable ``gamma`` is |blank| and the value in variable ``eta`` is |blank|.
   
      .. code-block:: java
      
         if (alpha > beta)
         {
            eta = alpha + 2;
            gamma = alpha + 5;
         }
         else
         {
            eta = alpha - 1;
            gamma = beta - 1;
         }

      - :7: Correct
        :x: Incorrect. 
      - :4: Correct
        :x: Incorrect.


.. activecode:: ac-select-we4-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }