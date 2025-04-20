Worked Example: Sequential If-Else Statements
=================================================

.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   
You can watch this video or read through the content below it.

.. youtube:: RYt8PMr8Xzk
   :divid: video-selection-we4-seqifelsestatements
   :align: center
   
   
Given the following declarations:

.. code-block:: java

   int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;


Evaluate these statements and determine the value of all variables used.

.. code-block:: java

   if (alpha > beta)
   {
      eta = alpha + 2;
      gamma = alpha + 5;
   }
   else
   {
      eta = alpha  - 1;
      gamma = beta - 1;
   }
   if (alpha > delta)
      gamma = alpha + 5;
   else
      gamma = beta + 5;
   eta = beta + 2;
      
   
.. topic:: SG1: Diagram which statements go together.

   Take note of the three parts of the sequence. 
   
   The first if-else (with the curly braces) is highlighted in blue in the figure below. 
   
   The second if-else (with no curly braces) is highlighted in yellow. 
   
   The final single statement is highlighted in green, and it is not part of the sequential if-else statements, so it will always be executed.

   .. figure:: Figures/we4-seq-ifelse-both.png
      :alt: Sequential If Diagram of two separate if-statements
     

.. topic:: SG2: For if statement, determine whether true or false
   
   Because there are 2 sequential if-statements, we start with the first one, and then repeat SG2 and SG3 for the other.
   
   First we evaluate (alpha > beta):
   
   ``(2 > 1)`` is TRUE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

   eta = alpha + 2 = 2 + 2 = 4

   gamma = alpha + 5 = 2 + 5 = 7

   .. figure:: Figures/we4-seq-ifelse-1.png
      :alt: sequential if-else part 1
   
   
.. topic:: SG2: For if statement, determine whether true or false
   
   Because there are 2 sequential if-statements, we need to repeat SG2 and SG3 for the second if-statement in the sequence.
   
   First we evaluate (alpha > delta):

   ``(2 > 3)`` is FALSE


.. topic:: SG3: If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).
   
   The condition is FALSE so we follow the else branch.
   
   gamma = beta + 5 = 1 + 5 = 6
 
   Next sequential statement is always executed:

   eta = beta + 2 = 1 + 2 = 3
   
   .. figure:: Figures/we4-seq-ifelse-2.png
      :alt: sequential if-else part 2


.. reveal:: reveal-selection-we4-SeqIfElse
   :showtitle: Show answer

   Answer: alpha = 2, beta = 1, delta = 3, eta = 3, gamma = 6
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we4-p1.rst