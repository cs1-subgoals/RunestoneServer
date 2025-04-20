Assessment: Writing Methods
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Writing Methods

   1. Define method header based on problem

   2. Define return statement at the end
      
   3. Define method body/logic

      a. Determine types of logic (expression, selection, loop, etc)
      b. Define internal variables
      c. Write statements

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-methods-1
   :nofeedback:
   
   .. fillintheblank:: assess-methods-1-1
   
      Fill in the blanks for a public method header that would work for this call:
      
      .. code-block:: java
         
         int fob;
         fob = obj.trip(4.1, "alphabet", 8);
      
      .. code-block:: java
      
         ___A___ ___B___ trip (___C___ one, ___D___ two, ___E___ three) 
         { 
            /* logic */ 
         }
         
      | Blank A: |blank|
      | Blank B: |blank|
      | Blank C: |blank|
      | Blank D: |blank|
      | Blank E: |blank|
      
      - :public:  Correct
        :x:  Incorrect. 
      - :int: Correct
        :x:  Incorrect.
      - :double:  Correct
        :x:  Incorrect. 
      - :String:  Correct
        :x:  Incorrect.
      - :int:  Correct
        :x:  Incorrect.
   
   .. fillintheblank:: assess-methods-1-2
   
      Fill in the blanks for a public method header that would work for this call:
      
      .. code-block:: java
         
         obj.advance();
      
      .. code-block:: java
      
         ___A___ ___B___ advance () { /* logic */ }
         
      | Blank A: |blank|
      | Blank B: |blank|
      
      - :public:  Correct
        :x:  Incorrect. 
      - :void: Correct
        :x:  Incorrect.
   
   .. fillintheblank:: assess-methods-1-3
   
      Fill in the blanks for a private method header that returns a String and accepts two integer parameters.
      
      .. code-block:: java
      
         ___A___ ___B___ calculate (___C___ one, ___D___ two) 
         { 
            /* logic */ 
         }
         
      | Blank A: |blank|
      | Blank B: |blank|
      | Blank C: |blank|
      | Blank D: |blank|
      
      - :private:  Correct
        :x:  Incorrect. 
      - :String: Correct
        :x:  Incorrect.
      - :int:  Correct
        :x:  Incorrect. 
      - :int:  Correct
        :x:  Incorrect.
        
   .. fillintheblank:: assess-methods-1-4
   
      Fill in the blanks for a private method header that returns nothing and takes no parameters.
      
      .. code-block:: java
      
         ___A___ ___B___ nada () { /* logic */ }
         
      | Blank A: |blank|
      | Blank B: |blank|
      
      - :private:  Correct
        :x:  Incorrect. 
      - :void: Correct
        :x:  Incorrect.
