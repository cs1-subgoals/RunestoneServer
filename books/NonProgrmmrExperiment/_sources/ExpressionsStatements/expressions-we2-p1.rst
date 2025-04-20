Expressions-WE2-P1
-----------------------

.. qnum::
   :prefix: Q
   :start: 11

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For all given problems below indicate if the code is valid or invalid. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code).


-------------------------------------------------------------------------------------------------------------------------
         
.. topic:: Expressions-WE2-P1


   **Given**

   .. code-block:: java

      int alpha = 2, beta = 1, delta = 3, gamma;
      final int eta = 10;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;


   .. mchoice:: m-Expr-WE2-P1-11
      :answer_a: valid
      :answer_b: invalid
      :correct: b

      gamma = beta + theta;


   .. mchoice:: m-Expr-WE2-P1-12
      :answer_a: valid
      :answer_b: invalid
      :correct: b

      eta = 42;


   .. mchoice:: m-Expr-WE2-P1-13
      :answer_a: valid
      :answer_b: invalid
      :correct: a

      rho = delta;


.. activecode:: ac-express-we2-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }