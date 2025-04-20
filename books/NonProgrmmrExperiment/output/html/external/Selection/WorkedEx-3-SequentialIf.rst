Worked Example: Sequential If Statements
==============================================

.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   
You can watch this video or read through the content below it.

.. youtube:: DULQb12L6LU
   :divid: video-selection-we3-seqifstatements
   :align: center
   
   
Given the following declarations:

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;


Evaluate these statements and determine the value of all variables used.

.. code-block:: java

   if (alpha > beta)
      eta = alpha + 2;
   if (alpha > delta)
      gamma = alpha + 5;
      
   
.. topic:: SG1: Diagram which statements go together.

   If no { } are present, then by default all if and else branches have only a single statement:

   .. figure:: Figures/we3-seq-if-both.png
      :alt: Sequential If Diagram of two separate if-statements
     

.. topic:: SG2: For if statement, determine whether true or false
   
   Because there are 2 sequential if-statements, we start with the first one, and then repeat SG2 and SG3 for the other.
   
   First we evaluate (alpha > beta):
   
   ``(2 > 1)`` is TRUE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

   The condition is TRUE so we execute the true branch:

   eta = alpha + 2 

   = 2 + 2 

   = 4

   .. figure:: Figures/we3-seq-if-1.png
      :alt: sequential if part 1
   
   
.. topic:: SG2: For if statement, determine whether true or false
   
   Because there are 2 sequential if-statements, we need to repeat SG2 and SG3 for the second if-statement in the sequence.
   
   First we evaluate (alpha > delta):

   ``(2 > 3)`` is FALSE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   The condition is FALSE and there is no else branch, so we do nothing.
   
   .. figure:: Figures/we3-seq-if-2.png
      :alt: sequential if part 2


.. reveal:: reveal-selection-we3-SeqIf
   :showtitle: Show answer

   Answer: alpha = 2, beta = 1, delta = 3, eta = 4, gamma = 0
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we3-p1.rst