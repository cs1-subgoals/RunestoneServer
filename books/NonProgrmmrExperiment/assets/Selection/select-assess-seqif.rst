Assessment: Sequential If-Statements
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-select-seqif
   :nofeedback:

   .. mchoice:: assess-select-seqif-1
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: I and III
      :answer_e: II and III
      :correct: a

      A game has a series of three levels, but you only get the bonus points if you pass all three levels on the first try. Assume the following declarations:
      
      ``boolean level1, level2, level3;``
      
      The variables indicate whether the level was passed on the first try (``true`` indicates yes, ``false`` indicates no).
      
      Which of the following code segments will properly update the ``points`` variable?
      
      I.    .. code-block:: java 
      
               if (level1 && level2 && level3)
                  points += 5;  
               
      II.   .. code-block:: java 
      
               if (level1 || level2 || level3)
                  points += 5; 
               
      III.  .. code-block:: java 
      
               if (level1)       
                  points += 5;                   
               if (level2)     
                  points += 5;                   
               if (level3) 
                  points += 5; 
        
   .. mchoice:: assess-select-seqif-2
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: I and III
      :answer_e: II and III
      :correct: b

      A company offers a discount depending on the number of units of the product that are ordered:
      
      +-------------------------------+----------+
      | Number of Units               | Discount |
      +===============================+==========+
      | 1 up to but not including 10  | 0        |
      +-------------------------------+----------+
      | 10 up to but not including 50 | 10%      |
      +-------------------------------+----------+
      | 50 or more                    | 20%      |
      +-------------------------------+----------+
      
      Assume that the variables ``numUnits, discount`` have been declared and have values.
      
      Which of the following code segments will work as intended?
      
      I.    .. code-block:: java 
      
               if (numUnits >= 50)
                  discount = 0.2;  
               if (numUnits >= 10)
                  discount = 0.1; 
               if (numUnits > 0) 
                  discount = 0;
      
      II.   .. code-block:: java 
      
               if (numUnits >= 50)
                  discount = 0.2;
               else if (numUnits >=10)
                  discount = 0.1; 
               else         
                  discount = 0; 
                  
      III.  .. code-block:: java
      
               if (numUnits > 0)
                  discount = 0;  
               if (numUnits > 10) 
                  discount = 0.1; 
               if (numUnits > 50)  
                  discount = 0.2;