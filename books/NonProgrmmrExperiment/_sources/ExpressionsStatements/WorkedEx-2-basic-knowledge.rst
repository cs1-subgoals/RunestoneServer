Worked Example: Basic Knowledge
====================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: R04ND63xURM
   :divid: video-express-we2-arithmetic
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2,
      beta = 1, 
      delta = 3, 
      eta, 
      gamma;
   double omega = 2.5, 
      theta = -1.3, 
      kappa = 3.0, 
      lambda, 
      rho; 
   
   lambda=alpha + delta;
   


.. topic:: SG1 : Determine resultant data type of expression
   
   The *expression* is the right-hand-side (RHS) of the statement: ``alpha + delta``. 
   In the first two lines, these variables were declared to be ``int`` type.
   Their sum will also be an ``int`` value.

.. topic:: SG2: Update variable for pre-increment or pre-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: SG3: Evaluate arithmetic expression according to operator precedence

   In the declarations, alpha was initialized with a value of 2, 
   and delta was initialized with a value of 3.

   The RHS of the statement is ``alpha + delta``, 
   so we replace those variable names with their actual values ``2 + 3``,
   which results in a sum of ``5``.

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``double``, and the RHS is type ``int``.
   This is valid, as Java automatically *promotes* an ``int`` value when we assign it to a ``double``.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: Questions to check understanding

   Q1) Is the left-hand-side (LHS) of the statement a variable? What type?

   Q2) What is the resulting type after evaluating the right-hand-side (RHS)?

   Q3) Can the type of the RHS result be assigned to the LHS variable?
        
   .. reveal:: ans-express-we2
      :showtitle: Show Answers

      Q1-Answer) Yes, lambda is declared as a double   

      Q2-Answer) On the RHS, alpha + delta is evaluated as int + int which is int

      Q3-Answer) Yes, an int can be assigned to a double (automatic promotion by adding .0)


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we2-p1.rst
      expressions-we2-p2.rst