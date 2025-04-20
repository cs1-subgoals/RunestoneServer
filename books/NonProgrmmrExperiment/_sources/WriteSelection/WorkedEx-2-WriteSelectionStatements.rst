Worked Example: Write Selection Statements
==============================================

.. topic:: Subgoals for Writing Selection Statements

   **If Statement**

   1. Define how many mutually exclusive paths are needed 

   2. Order from most restrictive/selective group to least restrictive 

   3. Write if statement with Boolean expression  

   4. Follow with true bracket including action 
  
   5. Follow with else bracket

   6. Repeat until all groups and actions are accounted for 

   **OR Switch Statement**

   1. Determine variable / expression for mutually exclusive ranges 

   2. Write switch statement based on variable / expression

   3. Each range is a 'case'

   4. Include break statements and default case if needed
   
   
You can watch this video or read through the content below it.

.. youtube:: RBL8S0dczO0
   :divid: video-selection-we8-writeifstatements
   :align: center
   
   
``Problem: Write the Java selection statements to solve the following specifications:``

   If integer variable currentNumber is odd, change its value so that it is now 4 times currentNumber plus 1; otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd).
      

.. topic:: SG1: Define how many mutually exclusive paths are needed 
    
   In this case, the problem says to do one action if variable is odd, and a different action otherwise.  
   
   Integer variable can only be odd or even, so there are 2 mutually exclusive paths.  An if statement is best approach
    

.. topic:: SG2: Order from most restrictive/selective group to least restrictive 
   
   Since there are only 2 branches, order should not matter

 
.. topic:: SG3: Write if statement with Boolean expression

   To determine if currentNumber is odd, we can check the remainder after dividing by 2 (modulo): ``if (currentNumber % 2 == 1)``

 
.. topic:: SG4: Follow with true bracket including action

   In the true branch, change value to 4 times + 1

   .. code-block:: java 

      if (currentNumber % 2 == 1)
      {
	     currentNumber = currentNumber * 4 + 1;
      }


.. topic:: SG5 : Follow with else bracket 

   In the else branch, change value to half current value. Note that integer division automatically *truncates* i.e. rounds down.

   .. code-block:: java

      if (currentNumber % 2 == 1)
   	  { 
	     currentNumber = currentNumber * 4 + 1;
      }
      else
      {
	     currenNumber /= 2;
      }


.. topic:: SG6: Repeat until all groups and actions are accounted for 

   Not used – only two branches


.. topic:: Equivalent solution using the other ordering of the range/case groups. 

   .. code-block:: java

      if (currentNumber % 2 == 0)
	  {
         currentNumber /= 2;
	  }
      else
	  {
         currentNumber = currentNumber * 4 + 1;
	  }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we2-p1.rst