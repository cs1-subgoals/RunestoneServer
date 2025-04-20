Assessment: Boolean Relational Operators
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

.. timed:: assess-expr-bool1
   :nofeedback:

   .. mchoice:: assess-exp-bool1-1
      :answer_a: true
      :answer_b: false
      :correct: b

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = x <= z;``
        
   .. mchoice:: assess-exp-bool1-2
      :answer_a: true
      :answer_b: false
      :correct: a

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = y >= z;``
        
   .. mchoice:: assess-exp-bool1-3
      :answer_a: true
      :answer_b: false
      :correct: a

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = x > z + y;``
        
   .. mchoice:: assess-exp-bool1-4
      :answer_a: true
      :answer_b: false
      :correct: a

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = z < y - z;``
        
   .. mchoice:: assess-exp-bool1-5
      :answer_a: true
      :answer_b: false
      :correct: b

      Given the following, what value is stored in variable ``answer``?
      
      ``int x = 5, y = 3, z = 1;``
      
      ``boolean answer;``
      
      ``answer = ((x * y) + (x * z)) != ((z * x) + (y * x));``