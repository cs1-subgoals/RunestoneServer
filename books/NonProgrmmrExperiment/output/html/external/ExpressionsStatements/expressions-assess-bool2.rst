Assessment: Boolean Logical Operators
---------------------------------------------

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

.. timed:: assess-expr-bool2
   :nofeedback:

   .. mchoice:: assess-exp-bool2-1
      :answer_a: true
      :answer_b: false
      :correct: b

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = (x < y) && (z < y);``
        
   .. mchoice:: assess-exp-bool2-2
      :answer_a: true
      :answer_b: false
      :correct: a

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = (x < y) || (z < y);``
        
   .. mchoice:: assess-exp-bool2-3
      :answer_a: true
      :answer_b: false
      :correct: a

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = (x <= 5) && (y >= 2);``
        
   .. mchoice:: assess-exp-bool2-4
      :answer_a: true
      :answer_b: false
      :correct: b

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = (y == z) || (z == x);``
        
   .. mchoice:: assess-exp-bool2-5
      :answer_a: true
      :answer_b: false
      :correct: a

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = (x <= 3) || ((z <= y) && (z == 1));``
      
   