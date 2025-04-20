Worked Example: Operation Precedence
===========================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: 0dcABatbiKg
   :divid: video-express-we4-precedence2
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta, gamma;
   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 

   gamma = delta / (alpha + beta) % alpha;


.. topic:: SG1 : Determine resultant data type of expression
   
   The *expression* is the right-hand-side (RHS) of the statement: ``delta / (alpha + beta) % alpha``. At the beginning of the snippet, all of these variables were declared as ``int`` type, so all of the operations will also result in ``int`` values. 
    
   If the expression had included any ``double`` values, the operations dealing with any ``double`` values would *promote* any ``int`` value on the other side of the operator to a ``double`` value, and the result would be a ``double``, but that is not the case here.

.. topic:: SG2: Update variable for pre-increment or pre-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: SG3: Evaluate arithmetic expression according to operator precedence
    
   - The RHS may be easiest to conceptualize algebraically, by replacing the variables right away with their initialized values from the declarations above: ``3 / (2 + 1) % 2``.
   - In the order of operations, parentheses have highest *precedence*, so we evaluate the addition within the parentheses first, resulting in a new expression: 3 / 3 % 2.
   - Division and modulus have the same precedence, so we evaluate them left to right: 3 / 3 is 1,  then 1 % 2 is 1. (Remember, the mod % operation returns the *remainder* after integer division.)
    

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``int``, and the RHS is type ``int``. This is valid.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: Questions to check understanding

   Q1) Is the left-hand-side (LHS) of the statement a variable? What type?

   Q2) What is the resulting type after evaluating the right-hand-side (RHS)?

   Q3) Can the type of the RHS result be assigned to the LHS variable?

   .. reveal:: ans-express-we4
      :showtitle: Show Answers

      Q1-Answer) Yes, gamma is declared as an int   

      Q2-Answer) On the RHS, all of the values are int, so the result is also int

      Q3-Answer) Yes, an int can be assigned to an int 


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we4-p1.rst
      expressions-we4-p2.rst