Worked Example: Nested If Statements
==============================================

.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   
You can watch this video or read through the content below it.

.. youtube:: peUN9AfMagE
   :divid: video-selection-we5-nestifstatements
   :align: center
   
   
Given the following declarations:

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;

   double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0; 


Evaluate these statements and determine the value of all variables used.

.. code-block:: java

   if (omega < kappa)
   {
       if (alpha < delta)
           eta = 5;
       if (alpha < eta) 
           gamma = 4;
   }
   rho = -1.0;
      
   
.. topic:: SG1: Diagram which statements go together.

   In this diagram, the first thing to note is the parent/outer if-statement highlighted in blue. 
   
   Inside the true branch of the parent/outer if-statement, there are two sequential if-statements. 
   
   The final single statement is highlighted in green, and it is not part of the nested if-statements, so it will always be executed.

   .. figure:: Figures/we5-nest-if-both.png
      :alt: Nested-If Diagram
     

.. topic:: SG2: For if statement, determine whether true or false
   
   Because there are 2 sequential if-statements, we start with the first one, and then repeat SG2 and SG3 for the other.
   
   First we evaluate (omega < kappa):
                                        
   ``(2.5 < 3.0)`` is TRUE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

   The true branch contains two sequential if-statements, so we must repeat the SG2 and SG3 for each of them.

   .. figure:: Figures/we5-nest-if-inner.png
      :alt: nested if true branch
   
   
.. topic:: SG2: For if statement, determine whether true or false
   
   Start with the first if-statement in the inner sequence.
   
   First we evaluate (alpha < delta):

   ``(2 < 3)`` is TRUE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   The condition is TRUE so we follow the true branch.

   eta = 5;
 
 
.. topic:: SG2: For if statement, determine whether true or false
   
   Now we do the second if-statement in the inner sequence.
   
   First we evaluate (alpha < eta):

   ``(2 < 5)`` is TRUE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   The condition is TRUE so we follow the true branch.
   
   gamma = 4;
 
   Next, the final sequential statement after the entire selection structure is always executed:

   rho = -1.0;


.. reveal:: reveal-selection-we5-NestIf
   :showtitle: Show answer

   Answer: 
   omega = 2.5, kappa = 3.0, alpha = 2, delta = 3, 
   eta = 5, gamma = 4, rho = -1.0
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we5-p1.rst