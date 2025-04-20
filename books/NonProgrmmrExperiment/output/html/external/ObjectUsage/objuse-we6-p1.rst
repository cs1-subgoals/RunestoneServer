ObjUse-WE6-P1
------------------

.. qnum::
   :prefix: Q
   :start: 15

    
.. topic:: Subgoals for Calling a Method

   1. Classify method as static method or instance method
      
      a. If static, use the class name

      b. If instance, must have or create an instance 
        
   2. Write (instance / class) dot method name and ( )

   3. Determine whether parameter(s) are appropriate
      
      a. Number of parameters passed must match method declaration

      b. Data types of parameters passed must match method declaration (or be assignable)
   
   4. Determine what the method will return (if anything: data type, void, print, change state of object) and where it will be stored (nowhere, somewhere)

   5. Evaluate right hand side (RHS) of assignment (if there is one). Value is dependent on method's purpose

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: ObjUse-WE6-P1

   For the following questions, fill in the blanks with NO spaces.
   
   For example, use ``Math.pow(x,y)`` rather than ``Math.pow(x, y)``

   .. fillintheblank:: fill-ObjUse-WE6-P1-15

      Fill in the blank to print the absolute value of the variable theta.	
      
      System.out.println(|blank|);

      - :Math\.abs\(theta\): Correct
        :x: Incorrect
        
   .. fillintheblank:: fill-ObjUse-WE6-P1-16

      Fill in the blank to print the value of 16 raised to the power of 5.
      
      System.out.println(|blank|);

      - :Math\.pow\(16,5\): Correct
        :x: Incorrect
        
   .. fillintheblank:: fill-ObjUse-WE6-P1-17

      Fill in the blank to print the maximum value of alpha and beta.
      
      System.out.println(|blank|);

      - :Math\.max\(alpha,beta\): Correct
        :x: Incorrect
        
.. activecode:: ac-objuse-we6-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }