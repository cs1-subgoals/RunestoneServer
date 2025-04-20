Selection-WE2-P1
---------------------

.. qnum::
   :prefix: Q
   :start: 6

    
.. topic:: Subgoals for Evaluating Selection Statements

   1. Diagram which statements go together.
   
   2. For if-statement, determine whether expression is true or false.
   
   3. If true, follow true branch. If false, follow else branch (OR do nothing if there is no else branch).

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Select-WE2-P1

   Each question below is independent, but they all use this given setup
   
   .. code-block:: java
      
      int alpha = 2, beta = 1, delta = 3, eta = 0, gamma = 0;
      double omega = 2.5, theta = -1.3, kappa = 3.0, lambda = 0.0, rho = 0.0;
   

   .. mchoice:: m-Select-WE2-P1-6
      :answer_a: 0 is true
      :answer_b: 0 is false
      :answer_c: There is no output because a compiler error occurs
      :answer_d: There is no output because an exception occurs
      :correct: c

      What is the output of the following code?
      
      .. code-block:: java
      
         int x = 0;
         if (x = 0)  /* look closely! */
            System.out.println("0 is true");
         else
            System.out.println("0 is false");
      
   
   .. mchoice:: m-Select-WE2-P1-7
      :answer_a: it is true
      :answer_b: it is false
      :answer_c: There is no output because a compiler error occurs
      :answer_d: There is no output because an exception occurs
      :correct: b

      What is the output of the following code?
      
      .. code-block:: java
      
         if (false) 
            System.out.println("it is true");
         else
            System.out.println("it is false");
   
   
   .. mchoice:: m-Select-WE2-P1-8
      :answer_a: Never
      :answer_b: Always
      :answer_c: There is no output because a compiler error occurs
      :answer_d: There is no output because an exception occurs
      :correct: b

      What is the output of the following code?
      
      .. code-block:: java
      
         if (12 < 12) 
            System.out.println("Never");
         else
            System.out.println("Always");
   
   
   .. mchoice:: m-Select-WE2-P1-9
      :answer_a: O.K.
      :answer_b: Not O.K.
      :answer_c: There is no output because a compiler error occurs
      :answer_d: There is no output because an exception occurs
      :correct: a

      What is the output of the following code?
      
      .. code-block:: java
      
         double var1 = 15.0;
         double var2 = 25.12;
         if (2 * var1 >= var2) 
            System.out.println("O.K.");
         else
            System.out.println("Not O.K.");
   

.. activecode:: ac-select-we2-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }