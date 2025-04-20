Assessment: Swap
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

.. timed:: assess-expr-swap
   :nofeedback:

   .. fillintheblank:: assess-exp-swap-1

      After executing the following code, the value in variable ``a`` is |blank| and the value in variable ``b`` is |blank|.
      
      ``int a = 1;``
      
      ``int b = 2;``
      
      ``a = 3;``

      - :3: Correct
        :x: Incorrect
      - :2: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-swap-2

      After executing the following code, the value in variable ``r`` is |blank| and the value in variable ``s`` is |blank|.
      
      ``int r = 2;``
      
      ``int s = 4;``
      
      ``r = s;``

      - :4: Correct
        :x: Incorrect
      - :4: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-swap-3

      After executing the following code, the value in variable ``p`` is |blank| and the value in variable ``q`` is |blank|.
      
      ``int p = 1;``
      
      ``int q = 8;``
      
      ``q = p;``
      
      ``p = q;``

      - :1: Correct
        :x: Incorrect
      - :1: Correct
        :x: Incorrect
        
   .. fillintheblank:: assess-exp-swap-4
      
      After executing the following code, the value in variable ``x`` is |blank|, the value in variable ``y`` is |blank|,  and the value in variable ``z`` is |blank|.
      
      ``int x = 7;``
      
      ``int y = 5;``
      
      ``int z = 3;``
      
      ``x = y;``
      
      ``y = z;``
      
      ``z = x;``

      - :5: Correct
        :x: Incorrect
      - :3: Correct
        :x: Incorrect
      - :5: Correct
        :x: Incorrect
      
   .. mchoice:: assess-exp-swap-5
      :answer_a: d = temp; b = a;
      :answer_b: d = c; b = a;
      :answer_c: d = c; b = temp;
      :answer_d: d = a; b = temp;
      :answer_e: d = a; b = c;
      :correct: c

      Suppose there are four ``integer`` variables ``a``, ``b``, ``c``, and ``d`` as depicted below. The code beside the diagram is intended to move the values in those variables one place **clockwise**, but two statements are missing. Choose the option that has the correct 2 statements.
      
      .. figure:: Figures/swap-assess-diagram.png
         :alt: 4-variable swap