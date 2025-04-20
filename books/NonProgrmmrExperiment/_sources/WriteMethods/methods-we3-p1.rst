WrMethods-WE3-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 46

    
.. topic:: Subgoals for Writing Methods

   1. Define method header based on problem

   2. Define return statement at the end
      
   3. Define method body/logic

      a. Determine types of logic (expression, selection, loop, etc)
      b. Define internal variables
      c. Write statements
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Methods-WE3-P1

   .. parsonsprob:: parsons-methods-WE3-P1-1

      Put the code in the right order to create a program that has a public method that returns a String and accepts an integer parameter and returns a flavor of ice cream. There is also a main program that calls the method twice.
      -----
      import java.util.*;
      public class main{
         public static String flavors (int one) {
      =====
            String flavor;
      =====
            if (one == 1)
               flavor = "chocolate";
      =====
            else if (one == 2)
               flavor = "vanilla";
      =====
            else 
               flavor = "strawberry";
      =====
            return flavor;
         }
      =====
      
         public static void main(String[] args){
      =====
            System.out.println(flavors(1));
            System.out.println(flavors(5));
      =====
         }
      }
      
   .. parsonsprob:: parsons-methods-WE3-P1-2

      Put the code in the right order to create a program that returns a String and accepts as parameters a double and a String, and concatenates the two values as a temperature along with its base scale. There is also a main program that calls the method twice, once with Celsius and once with Fahrenheit.
      -----
      import java.util.*;
      public class main{
         public static String temps (double t, String base) {
      =====
            String temp;
      =====
            temp = "temperature is " + t + " " + base;
      =====
            return temp;
         }
      =====
      
         public static void main(String[] args){
      =====
            System.out.println(temps(32.5, "F"));
            System.out.println(temps(0.05, "C"));
      =====
         }
      }
      
   .. parsonsprob:: parsons-methods-WE3-P1-3

      Put the code in the right order to create a program that returns a double, and accepts as parameters 3 integers, and calculates the average of the inputs. There is also a main program that calls the method twice with different values.
      -----
      import java.util.*;
      public class main{
         public static double avg (int one, int two, int three) {
      =====
            int sum = one + two + three;
      =====
            return sum / 3.0;
         }
      =====
      
         public static void main(String[] args){
      =====
            System.out.println(avg(1, 2, 5));
            System.out.println(avg(2, 4, 10));
      =====
         }
      }
      

.. activecode:: ac-methods-we3-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }