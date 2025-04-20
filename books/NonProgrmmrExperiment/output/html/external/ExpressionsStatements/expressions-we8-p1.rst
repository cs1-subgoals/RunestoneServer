Expressions-WE8-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 52

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, give the new value of the assigned variable. Each problem is independent of the others (e.g. Question 2 does not depend on Question 1, only the "Given" code).
    
-----------------------------------------------

.. topic:: Expressions-WE8-P1

   **Given**

   .. code-block:: java

      int  x = 4, y = 6;
      boolean result;
      
   What is the value of ``result`` after each of the following?


   .. mchoice:: m-Expr-WE8-P1-52
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = x < y;


   .. mchoice:: m-Expr-WE8-P1-53
      :answer_a: true
      :answer_b: false
      :correct: b

      result  = x + 2 < y;


   .. mchoice:: m-Expr-WE8-P1-54
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = x != y;


   .. mchoice:: m-Expr-WE8-P1-55
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = x + 3 >= y; 


   .. mchoice:: m-Expr-WE8-P1-56
      :answer_a: true
      :answer_b: false
      :correct: b

      result  = y == x;


   .. mchoice:: m-Expr-WE8-P1-57
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = y == x+2;


   .. mchoice:: m-Expr-WE8-P1-58
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = 7 == 7; 


   .. mchoice:: m-Expr-WE8-P1-59
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = 13 < 100;


   .. mchoice:: m-Expr-WE8-P1-60
      :answer_a: true
      :answer_b: false
      :correct: b

      result  = -17.32 != -17.32;


   .. mchoice:: m-Expr-WE8-P1-61
      :answer_a: true
      :answer_b: false
      :correct: b

      result  = -3.0 == 0.0;


   .. mchoice:: m-Expr-WE8-P1-62
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = 13 <= 100; 


   .. mchoice:: m-Expr-WE8-P1-63
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = -18 < -15; 


   .. mchoice:: m-Expr-WE8-P1-64
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = 4.2  > 3.7;


   .. mchoice:: m-Expr-WE8-P1-65
      :answer_a: true
      :answer_b: false
      :correct: a

      result  = 13 <= 13;


   .. mchoice:: m-Expr-WE8-P1-66
      :answer_a: true
      :answer_b: false
      :correct: b

      result  = 0.012 > 0.013;



.. activecode:: ac-express-we8-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }