Worked Example: Prefix Operators
======================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: mzqxvrMSLQQ
   :divid: video-express-we6-prefix
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta, gamma;
   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 

   eta = beta + delta % ++alpha;


.. topic:: SG1 : Determine resultant data type of expression
    
    The *expression* is the right-hand-side (RHS) of the statement: ``beta + delta % ++alpha``. At the beginning of the snippet, all of these variables were declared as ``int`` type, so all of the operations will also result in ``int`` values. 
    
 
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

   The ``++`` and ``--`` syntax indicates pre- or post- *side effect assignments* upon variables within an expression. 

   An *increment* is an increase of 1, while a *decrement* is a decrease of 1. Generally, we only want to perform these operations on int values, but it is valid to perform them on double values.

   It is important to note that these assignments may be *side effects* in other expressions, but they can also be statements all on their own. For example, the simple statement ``++delta;`` would be a valid line of Java code all on its own, adding 1 to the value of delta and assigning back into the delta variable.

   In this case, ``++alpha`` is a pre-increment operation, so we increment alpha, 
   and the new assigned value of alpha is 3 (it was initialized to 2).
   

.. topic:: SG3: Evaluate arithmetic expression according to operator precedence

   - The RHS may be easiest to conceptualize algebraically, by replacing the variables right away with their current values : ``1 + 3 % 3``. (Remember, alpha had a pre-increment, so it is already 1 more than it was initialized.)
   - In the order of operations, modulus has higher *precedence* than addition, so we evaluate the mod first: 3 % 3 is 0. (Remember, the mod % operation returns the *remainder* after integer division.)
   - Finally, we evaluate the addition: 1 + 0 is 1.


.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``int``, and the RHS is type ``int``. This is valid.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   It is wise to double-check whether the ``++`` or ``--`` were on the left or right of the variables, to be sure whether we perform a *pre* or *post* side effect assignment. In this case, the only increment was a *pre-increment*, so we do not need to peform any *post* side effect assignments.


.. topic:: Questions to check and extend understanding

   Q1) What are the final values of alpha, beta, delta and eta?

   Q2) Try this in the ActiveCode box below: ``double x=-2.1; System.out.print(++x);``

   Q3) Try this in the ActiveCode box below, and try other values instead of 4: ``int i=0; while(i<4){System.out.print(++i);}``

   .. reveal:: ans-express-we6
      :showtitle: Show Answers

      Q1-Answer) alpha is 3; beta is 1; delta is 3; eta is 1;

      Q2-Answer) -1.1

      Q3-Answer) Initial output is 1234.
    

.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we6-p1.rst