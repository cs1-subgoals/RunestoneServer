Selection-WE3-P1
---------------------

.. qnum::
   :prefix: Q
   :start: 10

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Select-WE3-P1

   Use this given setup
   
   .. code-block:: java
      
      int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
      

   .. fillintheblank:: fill-Select-WE3-P1-10
   
      After executing the following code, the value in variable ``alpha`` is |blank| and the value in variable ``gamma`` is |blank|.
   
      .. code-block:: java
      
         if (alpha > beta)
            alpha = alpha + 2;
         if (alpha > delta)
            gamma = alpha + 5;

      - :4: Correct
        :x: Incorrect. 
      - :9: Correct
        :x: Incorrect.


.. activecode:: ac-select-we3-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }