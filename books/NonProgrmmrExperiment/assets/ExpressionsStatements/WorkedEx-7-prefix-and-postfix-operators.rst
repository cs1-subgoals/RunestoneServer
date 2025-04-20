Worked Example: Prefix and Postfix Operators
======================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: VYWuuf08Vzs
   :divid: video-express-we7-postfix
   :align: center
   
Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta, gamma;
   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho; 

   lambda = ++beta / delta-- * alpha;


.. topic:: SG1 : Determine resultant data type of expression
    
    The *expression* is the right-hand-side (RHS) of the statement: ``++beta / delta-- * alpha``. At the beginning of the snippet, all of these variables were declared as ``int`` type, so all of the operations will also result in ``int`` values.


.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

   In this example, we see one pre-increment with ``++beta`` so we increment beta before we evalute the rest of the expression. The initial value of beta was 1, so a side-effect of this statement is to assign beta the new incremented value of 2.


.. topic:: SG3: Evaluate arithmetic expression according to operator precedence
    
   - The RHS may be easiest to conceptualize algebraically, by replacing the variables right away with their current values : ``2 / 3 * 2``. (Remember, beta had a pre-increment, so it is already 1 more than it was initialized.)
   - In the order of operations, division and multiplication have the same *precedence*, so we evaluate them left to right. First, 2/3 is 0 (Remember, integer division *truncates* or abandons the remainder.), and then 0 * 2 is 0.
    
    
.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``double``, and the RHS is type ``int``. This is valid, as the result of the expression will be *promoted* to a double.


.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   In this example, we see one pre-dencrement with ``delta--`` so we dencrement delta after we evalute the rest of the expression. The initial value of delta was 3, so a side-effect of this statement is to assign delta the new dencremented value of 2.
    
    
.. topic:: Questions to check and extend understanding

   Q1) What are the final values of alpha, beta, delta and lambda?

   Q2) What do you think will happen to x and y in the statements: ``int x=5; int y = ++x--;``

   Q3) Try this in the ActiveCode box below, and try changing the pre-increment to a post-increment: ``int i=0; while(i<4){System.out.print(++i);}``

   .. reveal:: ans-express-we7
      :showtitle: Show Answers

      Q1-Answer) alpha is 2; beta is 2; delta is 2; lambda is 0.0;

      Q2-Answer) If you attempt to run this, you will get a compilation error. You cannot do both an pre- and post- assignment on the same reference to a value.

      Q3-Answer) Initial output is 1234. After the change, output is 0123.
 

.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we7-p1.rst
      expressions-we7-p2.rst