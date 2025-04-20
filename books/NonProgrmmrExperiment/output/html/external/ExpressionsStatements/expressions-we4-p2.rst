Expressions-WE4-P2
-----------------------

.. qnum::
   :prefix: Q
   :start: 27

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, either give the new value of the assigned variable, or explain why the statement is invalid. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code). **If you must round a numeric answer, use 4 decimal places of precision.**
    
-----------------------------------------------

.. topic:: Expressions-WE4-P2

   **Given**

   .. code-block:: java

      int alpha = 2, beta = 1, delta = 3, eta, gamma;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 


   .. fillintheblank:: fill-Expr-WE4-P2-27

      lambda = alpha / kappa + delta;

      - :3.6667: Correct
        :x: Incorrect


   .. mchoice:: m-Expr-WE4-P2-28
      :answer_a: cannot assign a double to an int variable
      :answer_b: eta does not have a value
      :answer_c: eta is a constant
      :answer_d: cannot assign an int to a double variable
      :correct: a

      eta = alpha * beta + (omega – theta) * kappa;

      Why is this statement invalid?
      
      
   **Given**

   .. code-block:: java

      int r = 8;
      double volume;  
      
   .. mchoice:: m-Expr-WE4-P2-29
      :answer_a: volume = 4 / 3 * 3.14 * r * r * r;
      :answer_b: volume = 4 / 3 * 3.14159 * r * r * r;
      :answer_c: volume = 4.0 / 3 * 3.14 * r * r * r;
      :answer_d: An accurate result is not possible with these data types.
      :correct: c

      Which statement will calculate the volume of a sphere most accurately?

.. activecode:: ac-express-we4-p2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }