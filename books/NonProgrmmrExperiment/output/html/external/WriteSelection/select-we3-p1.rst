WriteSelection-WE3-P1
-------------------------

.. qnum::
   :prefix: Q
   :start: 8

    
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

.. topic:: WrSelect-WE3-P1

   Table for Q8
   
   +-------------------------------------+----------+
   | Distance                            | Cost     |
   +=====================================+==========+
   | 0 through 100                       | 5.00     |
   +-------------------------------------+----------+
   | More than 100 but not more than 500 | 8.00     |
   +-------------------------------------+----------+
   | More than 500 but less than 1,000   | 10.00    |
   +-------------------------------------+----------+
   | 1,000 or more                       | 12.00    |
   +-------------------------------------+----------+

   .. parsonsprob:: parsons-WrSelect-WE3-P1-8
      :language: java
      
      Put the code in the right order to create a program that will generate a value 0 to 1500 inclusive, assign a value to double variable ``cost`` depending on the value of integer variable ``distance`` as shown in the table above, and then print both values. 
      -----
      impot java.util.*;
      public class main {
         public static void main(String[] args) {
      =====
            Random r = new Random();
            int distance = r.nextInt(1501);
            double cost = 0.0;
      =====
            if (distance <= 100)
      =====
               cost = 5;
      =====
            else if (distance <= 500)
      =====
               cost = 8;
      =====
            else if (distance < 1000)
      =====
               cost = 10;
      =====
            else
      =====
               cost = 12;
      =====
            System.out.println("Distance: " + distance + "; Cost: $" + cost);
      =====
         }
      }
   
   .. parsonsprob:: parsons-WrSelect-WE3-P1-9
      :language: java
      
      Put the code in the right order to create a program that will generate an integer between 1 and 7, print the value, and display the name of the weekday where 1 is Sunday and 7 is Saturday.
      -----
      impot java.util.*;
      public class main {
         public static void main(String[] args) {
      =====
            Random r = new Random();
            int x = 1 + r.nextInt(7);
            String result = "";
            System.out.println(x);
      =====
            switch (x) {
      =====
               case 1: result = "Sunday"; break;
               case 2: result = "Monday"; break;
               case 3: result = "Tuesday"; break;
               case 4: result = "Wednesday"; break;
               case 5: result = "Thursday"; break;
               case 6: result = "Friday"; break;
               case 7: result = "Saturday"; break;
      =====
            }
      =====
            System.out.println(result);
      =====
         }
      }
      
   .. parsonsprob:: parsons-WrSelect-WE3-P1-10
      :language: java
      
      Put the code in the right order to create a program that will generate an integer between 65 and 122 inclusive and then convert that code to a character through a cast. The program should then print the character value and print "Vowel" or "Consonant" depending on the character value. If the character is not a letter (between a and z or A and Z), then an error message should be printed. Vowels are considered to be {a, e, i, o, u}.
      -----
      impot java.util.*;
      public class main {
         public static void main(String[] args) {
      =====
            Random r = new Random();
            int value = r.nextInt(57) + 65;
            char ch = (char)value;
            System.out.println(ch);
      =====
            if (('a' <= ch && <= 'z') || ('A' <= ch && ch <= 'Z')) {
      =====
               if (ch == 'a' || ch == 'A' || ch == 'e' || ch == 'E'
                     || ch == 'i' || ch == 'I' || ch == 'o' || ch == 'O'
                     || ch == 'u' || ch == 'U')
      =====
                  System.out.println("Vowel");
      =====
               else
                  System.out.println("Consonant");
      =====
            }
      =====
            else
               System.out.println("Error");
      =====
         }
      }

.. activecode:: ac-writeselect-we3-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }