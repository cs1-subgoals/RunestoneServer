Expressions-WE1-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)
    
   For all given problems below indicate if the code is valid or invalid. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code).


-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Expressions-WE1-P1

   **Given**

   .. code-block:: java

      int alpha, beta = 1, gamma;
      double omega = 2.5, theta, lambda;



   .. mchoice:: m-Expr-WE1-P1-1
      :answer_a: valid
      :answer_b: invalid
      :correct: a

      alpha = beta;


   .. mchoice:: m-Expr-WE1-P1-2
      :answer_a: valid
      :answer_b: invalid
      :correct: b

      alpha = omega;


   .. mchoice:: m-Expr-WE1-P1-3
      :answer_a: valid
      :answer_b: invalid
      :correct: a

      theta = 22;


   .. mchoice:: m-Expr-WE1-P1-4
      :answer_a: valid
      :answer_b: invalid
      :correct: b

      omega = gamma;


   .. mchoice:: m-Expr-WE1-P1-5
      :answer_a: valid
      :answer_b: invalid
      :correct: b

      theta = lambda;


.. activecode:: ac-express-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }