Expressions-WE11-P2
-------------------------

.. qnum::
   :prefix: Q
   :start: 80

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, either give the new value of the assigned variable, or explain why the statement is invalid. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code). **If you must round a numeric answer, use 4 decimal places of precision.**
    
-----------------------------------------------

.. topic:: Expressions-WE11-P2

   **Given**

   .. code-block:: java

      int alpha = 2, beta = 1, delta = 3, eta, gamma;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;



   .. fillintheblank:: fill-Expr-WE11-P2-80

      lambda = alpha * Math.abs(theta);

      What is the value of lambda?

      - :2.6: Correct
        :x: Incorrect


   .. mchoice:: m-Expr-WE11-P2-81
      :answer_a: cannot assign a double to an int variable
      :answer_b: gamma does not have a value
      :answer_c: Math.sqrt is illegal
      :answer_d: cannot assign an int to a double variable
      :correct: a

      gamma = Math.sqrt(25);

      Why is this statement invalid?


.. activecode:: ac-express-we11-p2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }