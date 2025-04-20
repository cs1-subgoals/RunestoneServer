Assessment: Pre/Post Operators
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

.. timed:: assess-expr-prepost
   :nofeedback:

   .. fillintheblank:: assess-exp-pp-1

      Given the following, what value is stored in variable alpha?
      
      ``int a = 0, b = 1, c = 2, d = 3, alpha;``
      
      ``alpha = ++a + b--``

      - :2: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-pp-2

      Given the following, what value is stored in variable beta?
      
      ``int a = 0, b = 1, c = 2, d = 3;``
      
      ``int alpha, beta;``
      
      ``alpha = c-- * ++b;``
      
      ``beta = alpha - d++ + b * a;``

      - :1: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-pp-3

      Given the following, what value is stored in variable gamma?
      
      ``int a = 0, b = 1, c = 2, d = 3;``
      
      ``int gamma;``
      
      ``gamma = ++a + ++b + c--;``

      - :5: Correct
        :x: Incorrect
        
   .. mchoice:: assess-exp-pp-4
      :answer_a: 1.5
      :answer_b: 2.5
      :answer_c: 1
      :answer_d: 2
      :answer_e: Compiler error - will not compile
      :correct: e

      Given the following, what value is stored in variable detla?
      
      ``int a = 0, b = 1, c = 2, d = 3, delta;``
      
      ``delta = (d / c)++ - (a % ++b);``
      
   .. mchoice:: assess-exp-pp-5
      :multiple_answers:
      :answer_a: eta++;
      :answer_b: eta + 1;
      :answer_c: ++eta;
      :answer_d: ++eta--;
      :answer_e: eta = eta + 1;
      :correct: a,c,e

      Which of the following are syntactically valid ways to increment the value of ``eta`` by one? Select all that apply.