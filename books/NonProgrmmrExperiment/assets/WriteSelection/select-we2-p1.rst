WriteSelection-WE2-P1
------------------------

.. qnum::
   :prefix: Q
   :start: 5

    
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


-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: WrSelect-WE2-P1

   .. parsonsprob:: parsons-WrSelect-WE2-P1-5
      :language: java
      
      Put the code in the right order to create a program that will generate an integer value between 0 and 25, print the value, and if the value is greater than 18, print a message saying "This is an overload"; otherwise print a message saying "Not an overload".
      -----
      import java.util.*;
      public class main {
         public static void main(String[] args) {
      =====
            Random r = new Random();
            int x = r.nextInt(26);
            System.out.println(x);
      =====
            if (x > 18)
      =====
               System.out.println("This is an overload.");
      =====
            else
      =====
               System.out.println("Not an overload.");
      =====
         }
      }
   
   
   .. parsonsprob:: parsons-WrSelect-WE2-P1-6
      :language: java
      
      Put the code in the right order to create a program that will generate an integer value between 3 and 7, print the value, and if the value is equal to 5 then set the character variable classType equal to 'G', and print a message saying "graduate student"; otherwise set classType equal to 'U' and print a message saying "undergraduate".
      -----
      import java.util.*;
      public class main {
         public static void main(String[] args){
      =====
            Random r = new Random();
            char classType = 'x';
            int x = 3 + r.nextInt(5);
            System.out.println(x);
      =====
            if (x == 5) {
      =====
               classType = 'G';
               System.out.println("graduate student");
      =====
            }
            else {
      =====
               classType = 'U';
               System.out.println("undergraduate student");
            }
      =====
         }
      }
   
   
   .. parsonsprob:: parsons-WrSelect-WE2-P1-7
      :language: java
      
      Put the code in the right order to create a program that will generate the value for a year (1500 to 3000 inclusive) and print the value. Then it will print *true* if the year is a leap year, otherwise the program prints *false*. A leap year is a multiple of 4, with one exception: if the year is a multiple of 100 but *not* 400, then it is *not* a leap year. For example, the year 1900 was not a leap year, but the year 2000 was indeed a leap year.
      -----
      import java.util.*;
      public class main {
         public static void main(String[] args){
      =====
            Random r = new Random();
            int x = 1500 + r.nextInt(1501);
            boolean result = false;
      =====
            System.out.println(x);
      =====
            if (x % 4 == 0)
      =====
               if (x % 100 == 0)
      =====
                  if (x % 400 == 0)
                     result = true;
                  else
                     result = false;
      =====
               else 
                  result = true;
      =====
            else
               result = false;
      =====
            System.out.println(result);
      =====
         }
      }

.. activecode:: ac-writeselect-we2-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }