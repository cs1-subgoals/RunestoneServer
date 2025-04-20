Assessment: Operation Precedence
---------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for evaluating an assignment statement

   1. Determine resultant data type of expression
   2. Update variable for pre-increment or pre-decrement operators (side effect)
   3. Evaluate arithmetic expression according to operator precedence
   4. If an assignment statement (=), is Left Hand Side (LHS) a variable? Check data type of value against data type of variable.
   5. Update variable for post-increment or post-decrement operators (side effect)

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-expr-precedence
   :nofeedback:

   .. fillintheblank:: assess-exp-op-1

      Given the following, what value is stored in variable alpha?
      
      ``int alpha = 0, x = 5, y = 6, z = 2;``
      
      ``alpha = x + y * z - 1``

      - :16: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-op-2

      Given the following, what value is stored in variable beta?
      
      ``int beta = 0, x = 5, y = 6, z = 2;``
      
      ``beta = (y + 3) * (x / 3) - z;``

      - :7: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-op-3

      Given the following, what value is stored in variable gamma?
      
      ``int x = 5, y = 6;``
      
      ``double gamma = 1.0;``
      
      ``gamma = gamma * -1.0 + x / y;``

      - :-1.0: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-op-4

      Given the following, what value is stored in variable delta?
      
      ``int delta = 0, x = 5, y = 6, z = 2;``
      
      ``delta = x % y * z % y;``

      - :4: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-op-5

      Given the following, if ``iota`` contains the value 32, what must be the value stored in variable ``eta``?
      
      ``int eta = ??;``
      
      ``int iota = (eta + 5) * (5 % eta + 2);``

      - :3: Correct
        :x: Incorrect