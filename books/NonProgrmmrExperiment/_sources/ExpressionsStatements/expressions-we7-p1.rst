Expressions-WE7-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 42

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, either give the new value of the assigned variable, or explain why the statement is invalid. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code). **If you must round a numeric answer, use 4 decimal places of precision.**
    
-----------------------------------------------

.. topic:: Expressions-WE7-P1

   **Given**

   .. code-block:: java

      int alpha = 2, beta = 1, delta = 3, eta, gamma;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;



   .. fillintheblank:: fill-Expr-WE7-P1-42

      ``rho = ++delta / alpha-- * beta++;`` 
      
      What is the value of delta after execution?

      - :4: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE7-P1-43

      ``rho = ++delta / alpha-- * beta++;``	
      
      What is the value of alpha after execution? 

      - :1: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE7-P1-44

      ``rho = ++delta / alpha-- * beta++;``	
      
      What is the value of beta after execution?

      - :2: Correct
        :x: Incorrect       


   .. fillintheblank:: fill-Expr-WE7-P1-45

      ``rho = ++delta / alpha-- * beta++;``	
      
      What is the value of rho after execution?

      - :2.0: Correct
        :x: Incorrect


   


.. activecode:: ac-express-we7-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }