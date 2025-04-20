Selection-WE6-P1
---------------------

.. qnum::
   :prefix: Q
   :start: 16

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Select-WE6-P1

   .. clickablearea:: ca-Select-WE6-P1-16
      :question: Click on the if-statement that must be TRUE in order to execute the line ``e = 3;`` in the following code.
      :iscode:
      
      :click-incorrect:if (x > y):endclick:
      {
         :click-incorrect:if (a > b):endclick:
            e = 1;
         :click-incorrect:else:endclick:
            e = 2;
      }
      :click-incorrect:else:endclick:
         :click-correct:if (a < b):endclick:
            e = 3;
         :click-incorrect:else:endclick:
            e = 4;
            
            
   .. clickablearea:: ca-Select-WE6-P1-17
      :question: Click on the if-statement that must be FALSE in order to execute the line ``e = 2;`` in the following code.
      :iscode:
      
      :click-incorrect:if (x > y):endclick:
      {
         :click-correct:if (a > b):endclick:
            e = 1;
         :click-incorrect:else:endclick:
            e = 2;
      }
      :click-incorrect:else
         :click-incorrect:if (a < b):endclick:
            e = 3;
         :click-incorrect:else:endclick:
            e = 4;


   Use this given setup for each of the questions below.
   
   .. code-block:: java
      
      int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0;

   .. fillintheblank:: fill-Select-WE5-P1-18
   
      After executing the following code, the value in variable ``eta`` is |blank|.
   
      .. code-block:: java
      
         if (omega > kappa)
         {
            if (alpha > delta)
               eta = 5;
            else
               eta = 4;
         }
         else
            if (alpha < delta)
               eta = 3;
            else 
               eta = 2;

      - :3: Correct
        :x: Incorrect. 


   .. fillintheblank:: fill-Select-WE5-P1-19
   
      After executing the following code, the value in variable ``a`` is |blank| and the value in variable ``b`` is |blank|.
   
      .. code-block:: java
      
         int a = -5;
         int b = 5;
         if (a < 0)
            if (b > 0)
               a = b;
         else
            a = b + 10;
            b = b + 3;

      - :5: Correct
        :x: Incorrect. 
      - :8: Correct
        :x: Incorrect.
   
   
   .. fillintheblank:: fill-Select-WE5-P1-20
   
      After executing the following code, the value in variable ``x`` is |blank| and the value in variable ``y`` is |blank|.
   
      .. code-block:: java
      
         int x = -8;
         int y = 10;
         if (x < 0)
         {
            if (y < 0)
            x = y;
         }
         else
            x = y +10;
            y = x + y;

      - :-8: Correct
        :x: Incorrect. 
      - :2: Correct
        :x: Incorrect.


.. activecode:: ac-select-we6-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }