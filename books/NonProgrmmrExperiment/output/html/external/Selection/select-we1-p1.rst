Selection-WE1-P1
--------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Select-WE1-P1

   Each question below is independent, but they all use this given setup
   
   .. code-block:: java
      
      int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0;
   

   .. fillintheblank:: fill-Select-WE1-P1-1
   
      .. code-block:: java
      
         if (theta > omega)
            rho = kappa + 2;

      What is the value of rho?

      - :0: Correct
        :x: Incorrect
        
        
   .. fillintheblank:: fill-Select-WE1-P1-2
   
      .. code-block:: java
      
         if (beta < alpha)
            eta = 42;

      What is the value of eta?

      - :42: Correct
        :x: Incorrect
        
        
   .. fillintheblank:: fill-Select-WE1-P1-3
   
      After executing the following code, the value in variable ``eta`` is |blank| and the value in variable ``beta`` is |blank|.
   
      .. code-block:: java
      
         if (kappa < delta)
            eta = 42;
            beta = 22;

      - :0: Correct
        :x: Incorrect. 
      - :22: Correct
        :x: Incorrect. Remember, if there are no {}, only the next statement is included in the branch.


   .. fillintheblank:: fill-Select-WE1-P1-4
   
      After executing the following code, the value in variable ``eta`` is |blank| and the value in variable ``beta`` is |blank|.
   
      .. code-block:: java
      
         if (gamma < kappa)
         {
            beta = 22;
         }
         eta = 42;

      - :42: Correct
        :x: Incorrect. 
      - :22: Correct
        :x: Incorrect.
        
        
   .. clickablearea:: ca-Select-WE1-P1-5
      :question: Click on the statements belonging to the if-branch in the following code
      :iscode:
      
      :click-incorrect:if (kappa < delta):endclick:
         :click-correct:eta = 42;:endclick:
         :click-incorrect:beta = 22;:endclick:
      

.. activecode:: ac-select-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }