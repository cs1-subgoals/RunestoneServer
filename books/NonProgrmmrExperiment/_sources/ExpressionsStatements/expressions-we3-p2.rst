Expressions-WE3-P2
-------------------------

.. qnum::
   :prefix: Q
   :start: 21

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, either give the new value of the assigned variable, or explain why the statement is invalid. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code).


-------------------------------------------------------------------------------------------------------------------------

.. topic:: Expressions-WE3-P2

   **Given**

   .. code-block:: java

      int alpha = 2, beta = 1, delta = 3, eta, gamma; 
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;


   .. fillintheblank:: fill-Expr-WE3-P2-21

      lambda = beta * theta;

      What is the value of lambda?

      - :-1.3: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE3-P2-22

      eta = alpha * beta;

      What is the value of eta?
      
      - :2: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE3-P2-23

      alpha = beta + delta;

      What is the value of alpha?

      - :4: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE3-P2-24

      beta = beta * alpha;

      What is the value of beta?

      - :2: Correct
        :x: Incorrect


.. activecode:: ac-express-we3-p2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }