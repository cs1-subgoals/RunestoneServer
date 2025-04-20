Worked Example: Declaration and Initialization
==================================================

.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

You can watch this video or read through the content below it.

.. youtube:: Pv1TSkz-aBY
   :divid: video-express-we1-declareinit
   :align: center

Evaluate these statements. If invalid, give the reason. If valid, what are the values of the variables? 

.. code-block:: java
    
   int alpha, beta = 1, gamma;
   double omega = 2.5, theta, lambda; 
   alpha = 42;
   theta = 4;
   gamma = 0.0;

.. topic:: SG1: Determine resultant data type of expression

   - The code block can be broken into 2 kinds of statements. The first two lines are the *declaration* statements, followed by additional assignments.

   .. code-block:: java
       
      int alpha, beta = 1, gamma;
      double omega = 2.5, theta, lambda; 

   - In the first line, alpha, beta, and gamma are all declared as ``int`` type variables (short for integer). In the same line, beta is *initialized* with an assigned value of 1. 
   - Similarly, in the second line, omega, theta, and lambda are declared as ``double`` type variables (short for double-precision decimal), and in the same line, omega is initialized with an assigned value of 2.5.
   
   .. code-block:: java
   
      alpha = 42;
      theta = 4;
      gamma = 0.0;

   - ``alpha = 42;`` alpha is assigned the value of 42, which is an integer and valid.
   - ``theta = 4;`` theta is assigned the value of 4, which is an integer. However, the numeric value of any integer is not changed when converted to a decimal. The process of the computer adding the .0 to an ``int`` to convert it into a ``double`` is known as *promotion*, and is done automatically. This statement is valid.
   - ``gamma = 0.0;`` gamma is assigned the value of 0.0, which is a double. A double cannot be assigned to an integer variable and there is no automatic process to convert it. This results in a compilation error (incompatible types). If you copy the original code block into the runnable ActiveCode box below, you can see the exact compilation error.

   - What about lambda? What is it’s value? Because there is no assignment to the variable, its content is considered “unknown” or "garbage," and it must be assigned before you could use lambda in another expression. In the Java specification, certain values like array contents, class variables, and instance variables are given default values like 0 or 0.0, but in our example, lambda and the others are all local variables which must be given values before their use. Some compilers, for simplicity, will give local variables the same default initializations, but it would be unwise to rely on this behavior that does not match the Java specification.


.. topic:: SG2: Update variable for pre-increment or pre-decrement operators based on side effect

   NOT USED IN THIS EXAMPLE
  

.. topic:: SG3: Evaluate arithmetic expression according to operator precedence

   NOT USED IN THIS EXAMPLE
  

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
  
  See the above discussion.
  

.. topic:: SG5: Update variable for post-increment or post-decrement operators based on side effect

   NOT USED IN THIS EXAMPLE


.. reveal:: ans-express-we1
   :showtitle: Show Final Answer

   Answer:  
   alpha is 42, beta = 1, omega is 2.5, theta is 4.0, lambda is unknown;
   Since we cannot assign a double to the int variable gamma, 
   we have a compilation error on the final line.


.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we1-p1.rst
      expressions-we1-p2.rst