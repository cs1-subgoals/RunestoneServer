Worked Example: If Statements
==============================================

.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   
You can watch this video or read through the content below it.

.. youtube:: Y7P5JjOEDr8
   :divid: video-selection-we1-ifstatements
   :align: center
   
   
Given the following declarations:

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;

   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0;


Evaluate these statements and determine the value of all variables used.

.. code-block:: java

   if (kappa > omega)
      rho = kappa + 2;
      
   
.. topic:: SG1: Diagram which statements go together.

   If no { } are present, then by default all if and else branches have only a single statement:

   .. code-block:: java
      
      if (kappa > omega)
         rho = kappa + 2;
     

.. topic:: SG2: For if statement, determine whether true or false
   
   First we evaluate (kappa > omega):

   ``(3.0 > 2.5)`` is TRUE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

   The condition is TRUE so we execute the true branch:

   rho = kappa + 2 
   
   = 3.0 + 2 
   
   = 5.0
   

.. reveal:: reveal-selection-we1-If
   :showtitle: Show answer

   Answer: omega = 2.5, kappa = 3.0, rho = 5.0;
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we1-p1.rst