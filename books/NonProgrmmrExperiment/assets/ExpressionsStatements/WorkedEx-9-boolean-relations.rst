Worked Example: Boolean Relations
======================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable?

.. code-block:: java

   int alpha = 42, beta = 1, gamma = 5;
   boolean result;

   result = beta <= gamma && gamma <= alpha;


.. topic:: SG1 : Determine resultant data type of expression
    
   First, note that ``alpha``, ``beta``, and ``gamma`` are all integers. 

   In the final statement, the ``<=`` operator is valid to compare primitive types, and produces boolean results, which are then used with the ``&&`` operator to produce one final boolean.
   
   (You may wish to keep a precedence and associativity reference handy, until you have memorized the order of operations for boolean operators.) 
 
 
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

   NOT USED IN THIS EXAMPLE
    
    
.. topic:: SG3: Evaluate arithmetic expression according to operator precedence
    
   Substitute the values for the variables on the RHS and evaluate according to the order of operations.
   
   ``beta <= gamma && gamma <= alpha``
   
   ``1 <= 5 && 5 <= 42``
   
   ``true && true``
   
   ``true``
   

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``boolean``, and the RHS is type ``boolean``. This is valid.
   

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we9-p1.rst