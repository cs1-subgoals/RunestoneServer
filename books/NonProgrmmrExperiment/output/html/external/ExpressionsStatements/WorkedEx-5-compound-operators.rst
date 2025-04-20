Worked Example: Compound Operators
======================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: MmK4CxnaEKI
   :divid: video-express-we5-compoundops
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2, beta = 5,  delta = 7,  eta,  gamma = 5;
   double omega = 2.5,  theta = -1.3,  kappa = 3.0,  lambda,  rho; 

   gamma += delta / alpha + beta % alpha; 
   

.. topic:: SG1 : Determine resultant data type of expression

   - The *expression* is usually the right-hand-side (RHS) of the statement, but compound assignment operators are a special shorthand than includes the compounded operation with the left-hand-side (LHS). A much simpler example could be ``gamma += 1;``, which would be a shorthand for ``gamma = gamma + 1;``
   - Thus, the entire *expression* for this example is ``gamma + delta / alpha + beta % alpha;``, which will be assigned back into gamma.
   - At the beginning of the snippet, all of these variables were declared as ``int`` type, so all of the operations will also result in ``int`` values. 


.. topic:: SG2: Update variable for pre-increment or pre-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: SG3: Evaluate arithmetic expression according to operator precedence

   - The expression may be easiest to conceptualize algebraically, by replacing the variables right away with their initialized values from the declarations above: ``5 + 7 / 2 + 5 % 2``.
   - Division and modulus both have higher *precedence* than addition, so we evaluate them first, resulting in a new expression of ``5 + 3 + 1``. 
   - In the division, both variables are type ``int``, so the result is also an ``int`` value, with the remainder truncated (i.e. abandoned, i.e. thrown away).
   - Also remember, the mod % operation returns the *remainder* after integer division.
   - Finally, we evaluate the additions left-to-right, 5+3 is 8, and 8+1 is 9.


.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS of the assignment is a variable of type ``int``, and the expression result is type ``int``. This is valid.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: Questions to check understanding

   Q1) Is the left-hand-side (LHS) of the statement a variable? What type?

   Q2) What is the resulting type after evaluating the right-hand-side (RHS)?

   Q3) Can the type of the RHS result be assigned to the LHS variable?

   .. reveal:: ans-express-we5
      :showtitle: Show Answers

      Q1-Answer) Yes, gamma is declared as an int   

      Q2-Answer) On the RHS, all of the values are int, so the result is also int

      Q3-Answer) Yes, an int can be assigned to an int 


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we5-p1.rst
      expressions-we5-p2.rst