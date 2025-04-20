Arrays-WE1-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Evaluating Arrays

   1. Set up array from 0 to size-1 


   2. Evaluate data type of statements against array


   3. Trace statements, updating slots as you go 
       
      A. Remember assignment subgoals 
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Arrays-WE1-P1

   .. fillintheblank:: fill-Arrays-WE1-P1-1

      Assume the following declarations:
      
      .. code-block:: java
      
         String [] alpha;
         alpha = new String[4];
         
      Evaluate these statements:
      
      .. code-block:: java
      
         alpha[0] = "apple";
         alpha[1] = "Banana";
         alpha[2] = alpha[0].substring(2);
         alpha[3] = alpha[alpha[1].indexOf('n')];
         
      Give the contents of array ``alpha`` after the execution of the above statements:
      
      alpha[0] = "|BLANK|"
      
      alpha[1] = "|BLANK|"
      
      alpha[2] = "|BLANK|"
      
      alpha[3] = "|BLANK|"
       
         
      - :apple: Correct
        :x: Incorrect
      - :Banana: Correct
        :x: Incorrect
      - :ple: Correct
        :x: Incorrect
      - :ple: Correct
        :x: Incorrect
   
   
   .. fillintheblank:: fill-Arrays-WE1-P1-2

      Assume the following declarations:
      
      .. code-block:: java
      
         int [] beta;
         beta = new int[3];
         
      Evaluate these statements:
      
      .. code-block:: java
      
         beta[1] = 22;
         beta[0] = beta[1] - 11;
         beta[2] = beta[0] + beta[1];
         
      Give the contents of array ``alpha`` after the execution of the above statements:
      
      beta[0] = "|BLANK|"
      
      beta[1] = "|BLANK|"
      
      beta[2] = "|BLANK|"
       
         
      - :11: Correct
        :x: Incorrect
      - :22: Correct
        :x: Incorrect
      - :33: Correct
        :x: Incorrect


   .. mchoice:: m-Arrays-WE1-P1-3
      :answer_a: double [] gamma = new double[5];
      :answer_b: gamma[0] = 14;
      :answer_c: gamma[1] = gamma[0];
      :answer_d: gamma[gamma[0]] = 42;
      :answer_e: gamma[5] = 22;
      :correct: d

      Which line produces the *first* compiler error?
   

.. activecode:: ac-arrays-we1-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }