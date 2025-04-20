Expressions-WE1-P2
-----------------------

.. qnum::
   :prefix: Q
   :start: 6

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, either give the new value of the assigned variable, or enter "invalid" if the statement would result in a compiler error or using an undefined value. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code).


-------------------------------------------------------------------------------------------------------------------------
         
.. topic:: Expressions-WE1-P2

   
   **Given**

   .. code-block:: java

      int alpha, beta = 1, gamma;
      double omega = 2.5, theta, lambda;


   .. fillintheblank:: fill-Expr-WE1-P2-6

      alpha = beta;	

      What is the value of alpha?

      - :1: Correct
        :x: Incorrect


   .. mchoice:: m-Expr-WE1-P2-7
      :answer_a: cannot assign a double to an int variable
      :answer_b: lambda does not have a value
      :answer_c: omega does not have a value
      :answer_d: cannot assign an int to a double variable
      :correct: a

      alpha = omega;


   .. fillintheblank:: fill-Expr-WE1-P2-8

      theta = 22;

      What is the value of theta?

      - :22.0: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE1-P2-9

      omega = beta;	

      What is the value of omega?

      - :1.0: Correct
        :x: Incorrect


   .. mchoice:: m-Expr-WE1-P2-10
      :answer_a: cannot assign a double to an int variable
      :answer_b: lambda does not have a value
      :answer_c: theta does not have a value
      :answer_d: cannot assign an int to a double variable
      :correct: b

      theta = lambda;

      Why is this statement invalid?
        
        
.. activecode:: ac-express-we1-p2
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }