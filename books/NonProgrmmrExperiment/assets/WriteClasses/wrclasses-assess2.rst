Assessment: Writing Classes 2
---------------------------------------------

.. qnum::
   :prefix: Q
   :start: 1

    
.. topic:: Subgoals for Writing a Class 4/4

   1. Name it 


   2. Differentiate class-level (static) vs. instance/object-level variables  

   3. Differentiate class-level (static) vs. instance/object behaviors/methods 
   

   4. Define class variables (static) as needed '
   
      A. Name 
      B. Data Type 
      C. public / private / final 
      
      
   5. Define instance variables (that you want to be interrelated)  

      A. Name 
      B. Data Type 
      C. private 
      
      
   6. Create constructor (behavior) that creates initial state of object  

      A. public
      B. Same name as class
      C. No return type
      D. Default - no parameters
      E. Logic - initialize all variables
      F. Repeat as needed, adding parameters 
      
   
   7.  Create 1 accessor and 1 mutator behaviors per attribute

      A. Accessors 

         a. Name is get_<attr_name> 
         b. Public 
         c. Return type same data type as attribute
         d. No parameters 
         e. Logic - return value

      B. Mutators 
      
         a. Name is set_<attr_name>
         b. Public
         c. Return type is void 
         d. Parameter is same data type as attribute
         e. Logic validates input parameter and sets attribute value
         
   8. Write toString method
   
      A. public
      B. Returns String
      C. No parameters
      D. Logic - convert needed attributes to a format that can be printed 
   
   9. Write equals method 
   
      A. public 
      B. Returns boolean
      C. Parameter - instance of the class
      D. Logic - compare attributes for equity
      
   10. Create additional methods as needed 

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. timed:: assess-wrclasses-2
   :nofeedback:

   .. mchoice:: assess-wrclasses-2-1
      :answer_a: containsArt("rattrap", "similar", "today")
      :answer_b: containsArt("start", "article", "Bart")
      :answer_c: containsArt("harm", "chortle", "crowbar")
      :answer_d: containsArt("matriculate", "carat", "arbitrary")
      :answer_e: containsArt("darkroom", "cartoon", "articulate")
      :correct: a

      Consider the following method, which is intended to return ``true`` if at least one of the three strings ``s1``, ``s2``, or ``s2`` contains the substring ``"art"``.  Otherwise, the method should return ``false``.
      
      .. code-block:: java

         public boolean containsArt (String s1, String s2, String s3) {
            String all = s1 + s2 + s3;
            return (all.indexOf("art") != -1);
         }
      
      Which of the following method calls demonstrates that the method does NOT work as intended?


   .. mchoice:: assess-wrclasses-2-2
      :answer_a: I only
      :answer_b: I and II only
      :answer_c: I and III only
      :answer_d: II and III only
      :answer_e: I, II and III
      :correct: d

      Considering the following class, which of the following methods can be added to the SomeMethods class without causing a compiler error?
      
      .. code-block:: java

         public class SomeMethods {
            public void one(int first) {
               /* implementation not shown */ }

            public void one(int first, int second) {
               /* implementation not shown */ }

            public void one(int first, String second) {
               /* implementation not shown */ }
         } // end SomeMethods

      I. public void one(int value) …
      II. public void one(String first, int second) …
      III. public void one(int first, int second, int third) … 
   
   
   .. mchoice:: assess-wrclasses-2-3
      :answer_a: 100 100 100
      :answer_b: 300 100 100
      :answer_c: 300 100 300
      :answer_d: 300 300 100
      :answer_e: 300 300 300
      :correct: c
      
      Considering the following class declaration:
      
      .. code-block:: java

         public class SomeClass {
            private int num;

            SomeClass (int n) {
               num = n;
            }

            public void increment (int more) {
               num = num + more;
            }

            public int getNum() {
               return num;
            }
         }

      The following code segment appears in another class. What is the resulting output?
      
      .. code-block:: java

         SomeClass one = new SomeClass(100);
         SomeClass two = new SomeClass(100);
         SomeClass three = one;

         one.increment(200);
         System.out.printf("d d d", one.getNum(), two.getNum(), three.getNum());

   .. mchoice:: assess-wrclasses-2-4
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: II and III only
      :answer_e: I, II and III
      :correct: e
      
      Considering the following instance variables and incomplete method that are part of a class that represents an item. Method ``updateAge`` is used to update the variables based on the parameter ``extraMonths`` that represents the number of months to be added to the age.
      
      .. code-block

         private int years;  // age of item
         private int months;  // age of item 0 <= months <= 11
            // item can be 1 year 3 months old (or 15 months)

         public void updateAge (int extraMonths) { //extraMonths >= 0
            /* body of updateAge */
         }

         Which of the following code segments could be used to replace ``/* body of updateAge */`` so that the method will work as intended?
         
      .. figure:: Figures/classes-assess2-q4.png
         :alt: code segments
         
   .. mchoice:: assess-wrclasses-2-5
      :answer_a: I only
      :answer_b: II only
      :answer_c: III only
      :answer_d: II and III only
      :answer_e: I, II and III
      :correct: e
      
      Considering the following instance variables and method that appear in a class representing student information.
      
      .. code-block:: java

         private int assignmentCompleted;  
         private double testAverage;  

         public boolean isPassing( ) {  
            /* body of isPassing */
         }

      A student can pass a programming course if at least one of the following conditions is met:
      
      - The student has a test average that is greater than or equal to 90.
      - The student has a test average that is greater than or equal to 75 and has at least 4 completed assignments.

      Which of the following code segments could be used to replace ``/* body of isPassing */`` so that the method will work as intended?
      
      .. figure:: Figures/classes-assess2-q5.png
         :alt: code segments