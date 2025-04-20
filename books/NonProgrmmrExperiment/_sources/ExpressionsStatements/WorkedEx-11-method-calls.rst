Worked Example: Method Calls
======================================================

.. topic:: Subgoals for evaluating an assignment statement

    1. Determine resultant data type of expression
    2. Update variable for pre-increment or pre-decrement operators (side effect)
    3. Evaluate arithmetic expression according to operator precedence
    4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
    5. Update variable for post-increment or post-decrement operators (side effect)

.. youtube:: wGQcAlzY3R8
   :divid: video-express-we10-methodcalls
   :align: center

Given the following code snippet, evaluate the final statement (the last line). If invalid, give the reason. If valid, what value is assigned to the variable? Note any possible side effects.

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta, gamma;
   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda, rho;

   rho = beta + Math.pow(delta, alpha);
    
    
.. topic:: SG1 : Determine resultant data type of expression
    
   The *expression* is the right-hand-side (RHS) of the statement: ``beta + Math.pow(delta, alpha)``. Despite beta, delta, and alpha all being defined as ``int`` variables, we must check the API documentation for Math.pow to see what it returns. 
    
   .. figure:: Figures/math-pow-api-doc.png
      :alt: Math.pow documentation online from Oracle

   In this official documentation, directly from Oracle, the left-hand column includes the return type, specified here as ``double``.

   Since beta is an ``int``, it will be promoted when it is added to the ``double`` value returned by Math.pow, and the final result is a ``double`` value.

.. topic:: SG2: Update variables for any pre-increment or pre-decrement operators (side effects)

   NOT USED IN THIS EXAMPLE
    
.. topic:: SG3: Evaluate arithmetic expression according to operator precedence
    
   In Java, operands must be evaluated before operators, so Math.pow is called and returns before trying to add it to beta.

   So, we start with ``Math.pow(3, 2)``, and we must again check the documentation to be sure we know which argument is which. The API doc says, "Returns the value of the first argument raised to the power of the second argument." Thus, we use base 3 to the power of 2, which is 9. Since the API doc indicates a return type ``double``, we should think of this value as 9.0.

   Then we can add beta, so 1 + 9.0 gives us the final return value 10.0

.. topic:: SG4: If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.

   The LHS is a variable of type ``double``, and the RHS is type ``double``. This is valid.

   If we had tried to assign this value to an ``int`` variable, believing that all of the ``int`` operands would give us an ``int`` result, we would have had a compilation error for incompatible types. Ensuring compatible types is a common reason to check the API documentation for return types.

.. topic:: SG5: Update variable for post-increment or post-decrement operators (side effect)

   NOT USED IN THIS EXAMPLE

.. activecode:: ac-express-we10
    :language: java

    public class main{
        public static void main(String args[]){   
            
        }
    }
    
    
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      expressions-we11-p1.rst
      expressions-we11-p2.rst