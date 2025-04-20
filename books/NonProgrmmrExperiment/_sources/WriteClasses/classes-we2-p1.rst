WrClasses-WE2-P1
----------------------

.. qnum::
   :prefix: Q
   :start: 9

    
.. topic:: Subgoals for Writing a Class 2/4

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
   

-----------------------------------------------------------------------------------------------------------------------------------------------------

.. topic:: Classes-WE2-P1

   Consider the SongType class you began in an earlier exercise, as illustrated in the following UML diagram.
   
   .. figure:: Figures/song-type-1.PNG
      :alt: UML
   
   
   .. parsonsprob:: parsons-Classes-WE2-P1-9
   
      Put the code in the right order to complete the default constructor.
      -----
      public class SongType{
      =====
         //attributes declared here
         //...
         
         //default constructor
         public SongType(){
      =====
            title = "";
            artist = "";
            length = 0;
      =====
         }
      }
      
      
   .. parsonsprob:: parsons-Classes-WE2-P1-10
   
      Put the code in the right order to complete the specific overloaded constructor.
      -----
      public class SongType{
      =====
         //attributes declared here
         //...
         
         //overloaded constructor
         public SongType(String n, String a, double ln){
      =====
            title = "";
            artist = "";
            length = 0;
      =====
         }
      }
   

   .. mchoice:: m-Classes-WE2-P1-11
      :answer_a: Constructors must be named the same name as the class
      :answer_b: Default constructors have no parameters
      :answer_c: Classes can only have a single constructor
      :answer_d: Constructors must be public
      :answer_e: Constructors have no return type, not even void
      :correct: c

      Which of the following is NOT true about constructors?
      
      
   .. mchoice:: m-Classes-WE2-P1-12
      :answer_a: valid
      :answer_b: invalid
      :answer_c: cannot be determined
      :correct: b

      Two constructors are shown for the Point class below. Is this code valid?
      
      .. code-block:: java
      
         public class Point {
            private int x;
            private int y;
            
            public Point (int one, int two) {/*LOGIC*/}
            public Point (int a, int b) {/*LOGIC*/}
         }
   
   
.. activecode:: ac-classes-we2-p1
   :language: java

   public class main{
      public static void main(String args[]){      

      }
   }