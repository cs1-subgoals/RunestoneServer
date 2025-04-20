Worked Example: Nested If-Else Statements
==============================================

.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   
You can watch this video or read through the content below it.

.. youtube:: vZBb026og
   :divid: video-selection-we6-nestifelsestatements
   :align: center
   
   
Given the following declarations:

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;

   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0; 


Evaluate these statements and determine the value of all variables used.

.. code-block:: java

   if (omega > kappa)
   {
       if (alpha < delta)
           eta = 5;
       else 
           eta = 4;
   }
   else
      if (alpha > delta)
         eta = 3;
      else
         eta = 2;
      
   
.. topic:: SG1: Diagram which statements go together.

   In this diagram, the first thing to note is the parent/outer if-else statement highlighted in blue. 
   
   The true branch of the parent/outer statment contains an inner if-else. 
   
   Likewise, the else branch of the parent/outer statement contains an inner if-else.

   .. figure:: Figures/we6-nest-ifelse.png
      :alt: Nested If-Else Diagram
     

.. topic:: SG2: For if statement, determine whether true or false
   
   Because there are 2 sequential if-statements, we start with the first one, and then repeat SG2 and SG3 for the other.
   
   First we evaluate (omega > kappa):
                                        
   ``(2.5 > 3.0)`` is FALSE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

   The else branch contains another if-else statement, so we must repeat the SG2 and SG3.

   .. figure:: Figures/we6-nest-ifelse-inner.png
      :alt: nested if true branch
   
   
.. topic:: SG2: For if statement, determine whether true or false
   
   Start with the first if-statement in the inner sequence.
   
   First we evaluate (alpha > delta):

   ``(2 > 3)`` is FALSE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   The condition is FALSE so we follow the else branch.

   eta = 2;


.. reveal:: reveal-selection-we6-NestIfElse
   :showtitle: Show answer

   Answer: omega = 2.5, kappa = 3.0, alpha = 2, beta = 1, delta = 3, eta = 2
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we6-p1.rst