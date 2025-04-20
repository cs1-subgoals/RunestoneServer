Worked Example: Basic Operation Precedence
================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: FnTz-KyUwfg
   :divid: video-express-we3-precedence1
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2, beta = 1,  delta = 3,  eta,  gamma;
   double omega = 2.5,  theta = -1.3,  kappa = 3.0,  lambda,  rho; 

   lambda = alpha / kappa + delta;
   


.. topic:: SG1 : Determine resultant data type of expression
   
   The *expression* is the right-hand-side (RHS) of the statement: ``alpha / kappa + delta``. 
   At the beginning of the snippet, alpha and delta were declared to be ``int`` type, 
   while kappa was declared to be ``double`` type.
   Division has *higher precedence* that summation, 
   and a division that involves a double will have a double result.
   Then the sum will also be a double, as the value of delta will be 
   *promoted* for a valid summation with the result of alpha / kappa.

.. topic:: SG2: Update variable for pre-increment or pre-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: SG3: Evaluate arithmetic expression according to operator precedence

   In the declarations, alpha was initialized with a value of 2, 
   delta was initialized with a value of 3,
   and kappa was initilized with a value of 3.0.

   The RHS of the statement is ``alpha / kappa + delta``, 
   so we replace those variable names with their actual values ``2 / 3.0 + 3``.
   Division has higher precedence than summation, so we first evaluate 2 / 3.0 as
   0.6667 (we are rounding to 4 decimals for convenience -- a complete study of
   floating-point precision in Java is out of the scope of this lesson).
   After the division, we can now add 0.6667 + 3 for a total of 3.6667.
    

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``double``, and the RHS is type ``double``. This is valid.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: Questions to check understanding

   Q1) Is the left-hand-side (LHS) of the statement a variable? What type?

   Q2) What is the resulting type after evaluating the right-hand-side (RHS)?

   Q3) Can the type of the RHS result be assigned to the LHS variable?

   .. reveal:: ans-express-we3
      :showtitle: Show Answers

      Q1-Answer) Yes, lambda is declared as a double   

      Q2-Answer) On the RHS, alpha / kappa + delta is evaluated as int / double + int which is double

      Q3-Answer) Yes, a double can be assigned to a double 


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we3-p1.rst
      expressions-we3-p2.rst