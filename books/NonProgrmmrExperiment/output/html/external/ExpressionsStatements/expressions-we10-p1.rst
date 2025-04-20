Expressions-WE10-P1
-----------------------

.. qnum::
   :prefix: Q
   :start: 75

   
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

   For the assignment statements below, give the new value of the indicated variable.
    
-----------------------------------------------

.. topic:: Expressions-WE10-P1

   **Given**

   .. code-block:: java

      int x,y,z;
      x = 42;
      y = 11;
      z = 5;
      x = z;
      y = x;
      z = y;


   .. fillintheblank:: fill-Expr-WE10-P1-75

      What is the final value of x?

      - :5: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE10-P1-76

      What is the final value of y?

      - :5: Correct
        :x: Incorrect


   .. fillintheblank:: fill-Expr-WE10-P1-77

      What is the final value of z?

      - :5: Correct
        :x: Incorrect


.. activecode:: ac-express-we10-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }