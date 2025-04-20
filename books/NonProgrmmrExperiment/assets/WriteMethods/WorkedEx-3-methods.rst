Worked Example: Writing Methods
==================================================

.. topic:: Subgoals for Writing Methods

   1. Define method header based on problem

   2. Define return statement at the end
      
   3. Define method body/logic

      a. Determine types of logic (expression, selection, loop, etc)
      b. Define internal variables
      c. Write statements
      

--------------------------------------------------------------------------------------------------------------------------------------

Problem: Write a public method that does not return anything but accepts as parameters 2 Strings and prints out a cheerful sentence with the input in it.


---------------------------------------------------------------------------------------------------------

.. topic:: SG1: Define method header based on problem

   .. code-block:: java

      public void cheerful (String a, String b)
    
.. topic:: SG2: Define return statement at the end

   the ``return;`` statement is optional for void return type.

   .. code-block:: java

      public void cheerful (String a, String b)
      {
         return;
      }

.. topic:: SG3: Define method body/logic 

   a. Determine types of logic (expression, selection, loop, etc.) 
    
   b. Define internal variables 
    
   c. Write statements 
   
   The instructions require us to concatenate a String expression for printing. One variable to store the message could be useful.
   
   .. code-block:: java
   
      public void cheerful (String a, String b)
      {
         String message = a + " is happy clap your hands, " + b;
         System.out.println(messsage);
         return;
      }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      methods-we3-p1.rst