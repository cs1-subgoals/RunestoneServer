Worked Example: If-Else Statements
==============================================

.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   
You can watch this video or read through the content below it.

.. youtube:: M1s4KBNS4M0
   :divid: video-selection-we2-ifelsestatements
   :align: center
   
   
Given the following declarations:

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;

   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0;


Evaluate these statements and determine the value of all variables used.

.. code-block:: java

   if (alpha > delta)
       eta = alpha + 2;
   else
       gamma = alpha + 5;
      
   
.. topic:: SG1: Diagram which statements go together.

   If no { } are present, then by default all if and else branches have only a single statement:

   .. code-block:: java
      
      if (alpha > delta)
         eta = alpha +2;
      else
         gamma = alpha + 5;
     

.. topic:: SG2: For if statement, determine whether true or false
   
   First we evaluate (alpha > delta):

   ``(2 > 3)`` is FALSE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

   The condition is FALSE so we execute the else branch:

   gamma = alpha + 5 

   = 2 + 5 	= 7 
   

.. reveal:: reveal-selection-we2-IfElse
   :showtitle: Show answer

   Answer: alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 7
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we2-p1.rst