Worked Example: Assigning Booleans
======================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: i135iKWr4uM
   :divid: video-express-we8-boolean
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 42, beta = 1, gamma = 5;
   boolean result;

   result = beta <= alpha;


.. topic:: SG1 : Determine resultant data type of expression
    
   The *expression* is the right-hand-side (RHS) of the statement: ``beta <= alpha``. The operator is one of the boolean relational operators, so the result will be **boolean**. 

   The statement above would be an acceptable, complete response for this subgoal. However, for the sake of thoroughness, here is some more information about working with different data types and boolean operators. 

   The relational operators are:

   - ``<=`` Less than or equal (i.e. "at most")
   - ``>=`` Greater than or equal (i.e. "at least")
   - ``<`` Strictly less than
   - ``>`` Strictly greater than
   - ``==`` Equal 
   - ``!=`` Not equal 
    
   There are a few important details to note about using these operators.

   - They all work as you might expect for ``int`` values. The bulk of your first lessons in boolean operators will involve only integer values.
   - Be careful with equality for ``float`` or ``double`` values. Because of how these values are stored in memory, computed values may be slighty different than expected, and it is a good practice to use a range of acceptable values for comparing equality. This behavior of floating-point values, as well as the methods to program against it, is a bit beyond the scope of this lesson. If you run into this problem try searching for "comparing doubles in java" on the web.
   - Using equality operators ``==`` or ``!=`` on objects (such as Strings) only compares the memory reference; that is, two objects are only "equal" according to this operator if they are in fact the same object. If you wish to compare the values of object properties, the class definition must implement the ``.equals()`` method. 
   - Often, the notion of an object being "less than" or "greater than" another is nonsensical. However, sometimes we do wish to sort or rank objects by one of their properties (e.g. ``Car`` objects by their ``price`` property). In such cases, Java provides the Comparable and Comparator interfaces, but those are quite beyond the scope of this lesson.
 
.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

   NOT USED IN THIS EXAMPLE
    
.. topic:: SG3: Evaluate arithmetic expression according to operator precedence
    
   The RHS may be easiest to conceptualize as an algebraic inequality, by replacing the variables right away with their current values : ``1 <= 42``. Logically, this is a true statement, so the returned value is boolean ``true``.

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``boolean``, and the RHS is type ``boolean``. This is valid.

   If you have experience in other programming languages, you may have seen boolean true and false values interchanged with 1 and 0 integer values, or even compared with non-numeric values in a "truthy" expression. This is NOT the case in Java. In Java, the ``boolean`` data type only allows the ``true`` and ``false`` keywords.

   Data modeling may require more nuanced discussion of the semantic meanings for the values false, null, 0, empty, and/or undefined, but that is a bit beyond the scope of this lesson.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we8-p1.rst