Worked Example: Write Switch Statements
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

.. youtube:: xIMZEyPmKbE
   :divid: video-selection-we9-writeifstatements
   :align: center
   
   
``Problem A: Write the Java selection statements to solve the following specifications:``

   Write the statements to print out the name of the month equivalent to the value stored in the integer variable month.
      

.. topic:: SG1: Determine variable / expression for mutually exclusive ranges 
    
   In this case there are 12 different months. Each value is represented by a unique value (1 to 12).  So a switch statement will work. We want to base it off of the integer variable month.
    

.. topic:: SG2: Write switch statement based on variable / expression
   
   .. code-block:: java
   
      switch (month)
      {


      }

 
.. topic:: SG3: Each range is a 'case'

   .. code-block:: java
   
      switch (month)
      {
         case 1: System.out.println("January");
         case 2: System.out.println("February");
         case 3: System.out.println("March");
         case 4: System.out.println("April");
         case 5: System.out.println("May");
         case 6: System.out.println("June");
         case 7: System.out.println("July");
         case 8: System.out.println("August");
         case 9: System.out.println("September");
         case 10: System.out.println("October");
         case 11: System.out.println("November");
         case 12: System.out.println("December");
      }

 
.. topic:: SG4: Include break statements and default case if needed

   We only want 1 month to print, without falling through to the next case, so every case needs a break.

   .. code-block:: java
   
      switch (month)
      {
         case 1: System.out.println("January"); break;
         case 2: System.out.println("February"); break;
         case 3: System.out.println("March"); break;
         case 4: System.out.println("April"); break;
         case 5: System.out.println("May"); break;
         case 6: System.out.println("June"); break;
         case 7: System.out.println("July"); break;
         case 8: System.out.println("August"); break;
         case 9: System.out.println("September"); break;
         case 10: System.out.println("October"); break;
         case 11: System.out.println("November"); break;
         case 12: System.out.println("December"); break;
         default: System.out.println("Invalid value of month.");
      }


``Problem B: Write the Java selection statements to solve the following specifications:``

   Write the statements to print out the letter grade equivalent of your quiz grade. 
   90 – 100 (inclusive) is an A, 
   80 - 89 (inclusive) is a B, 
   70 - 79 (inclusive) is a C, 
   60 - 69 (inclusive) is a D, 
   and below 60 is an F.
   
.. topic:: SG1: Define how many mutually exclusive paths are needed 

   In this case, there are 5 mutually exclusive paths (one for each letter grade). 
   
   You may use a switch statement, but note that you will have to give each numeric grade as a case since relational (<, >, ==) are not allowed in case statements.
   
   Or you can use nested if statements. We will do that first, or you can skip to the alternative solution below.


.. topic:: SG2: Order from most restrictive/selective group to least restrictive 

   In this case most restrictive is for an A (90+), then B, then C, etc.
   

.. topic:: SG3: Write if statement with Boolean expression  

   .. code-block:: java

      if (quizGrade >= 90)
      

.. topic:: SG4: Follow with true bracket including action 

   .. code-block:: java

      if (quizGrade >= 90) {
        System.out.println("A");
      }
      
  
.. topic:: SG5: Follow with else bracket

   Note: For a "B" grade, we do not need to check that the quizGrade is within the upper bound (<90). We know it is, because if it wasn't, execution would have selected the first true branch. We only need to check the lower bound (>=80)

   .. code-block:: java

      if (quizGrade >= 90) {
         System.out.println("A");
      }
      else if (quizGrade >= 80) {  
	     System.out.println("B");
      }
      

.. topic:: SG6: Repeat until all groups and actions are accounted for 

   .. code-block:: java
   
      if (quizGrade >= 90) {
         System.out.println("A");
      } else if (quizGrade >= 80) {   
         System.out.println("B");
      } else if (quizGrade >= 70) {
         System.out.println("C");
      } else if (quizGrade >= 60) {
         System.out.println("D");
      } else {
         System.out.println("F");
      }


.. topic:: Equivalent Switch Statement: 
   
   .. code-block:: java
 
      switch (quizGrade) {
         case 90: case 91: case 92: case 93: case 94:  
         case 95: case 96: case 97: case 98: case 99: 
         case 100: 
            System.out.println("A"); 
            break;

         case 80: case 81: case 82: case 83: case 84: 
         case 85: case 86: case 87: case 88: case 89: 
            System.out.println("B"); 
            break;

         case 70: case 71: case 72: case 73: case 74:  
         case 75: case 76: case 77: case 78: case 79:  
            System.out.println("C"); 
            break;  

         case 60: case 61: case 62: case 63: case 64:  
         case 65: case 66: case 67: case 68: case 69:  
            System.out.println("D"); 
            break;

         default: 
            System.out.println("F");
      }
      
      
.. topic:: Practice Pages

   .. toctree::
      :maxdepth: 1

      select-we3-p1.rst